from app import app
import database
from app import app
from sqlite3 import dbapi2 as sqlite3
from flask import request, session, g, redirect, url_for, abort, \
    render_template, flash
from datetime import datetime
import os
from werkzeug.utils import secure_filename



@app.route('/')
@app.route('/index')
def index():
    db = database.get_db()
    sql_query = "select * from entries order by entries.id desc"
    cur = db.execute(sql_query)
    posts = cur.fetchall()
    return render_template("show_posts.html", posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))


@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    if not session.get('logged_in'):
        abort(401)
    if request.method == 'POST':
        db = database.get_db()
        current_data = str(datetime.today())[:19] #format yyyy-mm-dd hh-mm-ss
        #Uploading audio files
        audio_file = request.files['upload-audio']
        audio_filename = ''
        if audio_file.filename != '':
            audio_filename = secure_filename(audio_file.filename)
            audio_file.save(os.path.join(app.config['UPLOAD_AUDIO'], audio_filename))

        db.execute("insert into entries (slug, title, short_text, full_text, timestamp, audio) values (?, ?, ?, ?, ?, ?)",
                   ['post '+current_data, request.form['post-title'], request.form['post-short'],
                    request.form['post-full'], current_data, audio_filename])
        db.commit()
        flash('New entry was successfully posted')
        return redirect('index')
    return render_template('add_post.html', title_page='Add new post')


@app.route('/edit_post/<slug_post>', methods=['GET', 'POST'])
def edit_post(slug_post):
    db = database.get_db()
    sql_query = "select * from entries where entries.slug='{0}'".format(slug_post)
    cur = db.execute(sql_query)
    post = cur.fetchall()
    if request.method == 'POST':
        db.execute("update entries set title=?, short_text=?, full_text=? where slug=?", [request.form['post-title'], 
            request.form['post-short'], request.form['post-full'], slug_post])
        db.commit()
        return redirect(url_for('index'))
    return render_template('edit_post.html', post=post)




@app.route('/posts/<slug_post>')
def read_post(slug_post):
    """Show whole post """
    db = database.get_db()
    sql_query  = "select * from entries where entries.slug='{0}'".format(slug_post)
    cur = db.execute(sql_query)
    post = cur.fetchall()
    return render_template("read_post.html", posts=post, audio_dir=app.config['UPLOAD_AUDIO'])
