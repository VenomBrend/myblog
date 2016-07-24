<<<<<<< HEAD
=======
from flask import render_template
from flask.templating import render_template

>>>>>>> 0b07e3c036c097cdd4aaecc6170f4c8f27c002f4
from app import app
import database


from app import app
from sqlite3 import dbapi2 as sqlite3
from flask import request, session, g, redirect, url_for, abort, \
    render_template, flash
from datetime import datetime



@app.route('/')
@app.route('/index')
def index():
    db = database.get_db()
<<<<<<< HEAD
    sql_query = "select * from entries order by entries.id desc"
=======
    sql_query = "select * from entries"
>>>>>>> 0b07e3c036c097cdd4aaecc6170f4c8f27c002f4
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


<<<<<<< HEAD
@app.route('/add_post', methods={'GET', 'POST'})
def add_post():
    if not session.get('logged_in'):
        abort(401)
    if request.method == 'POST':
        db = database.get_db()
        current_data = str(datetime.today())[:19]
        db.execute("insert into entries (slug, title, short_text, full_text, timestamp) values (?, ?, ?, ?, ?)",
                   ['post '+current_data, request.form['post-title'], request.form['post-short'],
                    request.form['post-full'], current_data])
        db.commit()
        flash('New entry was successfully posted')
        return redirect('index')
=======
@app.route('/add_post')
def add_post():
>>>>>>> 0b07e3c036c097cdd4aaecc6170f4c8f27c002f4
    return render_template('add_post.html')


@app.route('/posts/<slug_post>')
def read_post(slug_post):
<<<<<<< HEAD
    """Show whole post """
=======
>>>>>>> 0b07e3c036c097cdd4aaecc6170f4c8f27c002f4
    db = database.get_db()
    sql_query  = "select * from entries where entries.slug='{0}'".format(slug_post)


    cur = db.execute(sql_query)
    post = cur.fetchall()
    return render_template("read_post.html", posts=post)
