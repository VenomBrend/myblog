from flask import render_template
from flask.templating import render_template

from app import app
import database




from app import app
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash



@app.route('/')
@app.route('/index')
def index():
    db = database.get_db()
    sql_query = "select * from entries"
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


@app.route('/add_post')
def add_post():
    return render_template('add_post.html')


@app.route('/posts/<slug_post>')
def read_post(slug_post):
    db = database.get_db()
    sql_query  = "select * from entries where entries.slug='{0}'".format(slug_post)


    cur = db.execute(sql_query)
    post = cur.fetchall()
    return render_template("read_post.html", posts=post)
