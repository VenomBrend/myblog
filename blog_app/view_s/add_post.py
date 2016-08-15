from flask import session, abort, request
from flask.views import MethodView
import datetime
from ..database import get_db


class AddPost(MethodView):
    def get(self):
        if not session.get('logged_in'):
            abort(401)
    def post(self):
        if not session.get('logged_in'):
            abort(401)
        db = get_db()
        current_data = str(datetime.today())[:19]  # format yyyy-mm-dd hh-mm-ss




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