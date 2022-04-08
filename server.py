import os
from flask import Flask, flash, request, redirect, url_for, render_template
from flask import send_from_directory
from werkzeug.utils import secure_filename
from recommend import *

UPLOAD_FOLDER = os.path.abspath('uploads')
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

Filename = ''

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
# 	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/upload', methods=["GET", "POST"])
def upload():
		global Filename
		if request.method == 'POST':
			if 'image' not in request.files:
				flash('No file part')
				return redirect(request.url)
			image = request.files['image']

			if image.filename == '':
				flash('No selcted file')
				return redirect(request.url)
			if image and allowed_file(image.filename):
				filename = secure_filename(image.filename)
				Filename = filename
				image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
				return redirect('/')
		return render_template("/upload_image.html")

@app.route('/my-link/')
def my_link():
	recommend(UPLOAD_FOLDER+'/'+Filename)
	return redirect('/')


if __name__ == '__main__':
	app.run(debug=True)