from flask import render_template, request, session, \
    flash, redirect
from flask.views import MethodView
from config import USERNAME, PASSWORD


class Login(MethodView):
    def get(self, error=None):
        return render_template('login.html', error=error)
    def post(self):
        error = None
        if request.form['username'] != USERNAME:
            error = 'Invalid username'
        elif request.form['password'] != PASSWORD:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
        return self.get(error)
