from flask import render_template
from flask.views import MethodView
from ..database import get_db

SQL_STRING = u"select * from entries order by entries.id desc"


class ShowPosts(MethodView):
    def show_all(self):
        db = get_db()
        cur = db.execute(SQL_STRING)
        posts = cur.fetchall()
        return render_template("show_posts.html", posts=posts)

