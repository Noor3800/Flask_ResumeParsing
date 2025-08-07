# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/')
# def form_page():
#     return render_template('index.html')
#     # return "Hello, World!"

# @app.route('/about')
# def about():
#     return "This is the about page."

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
import os
from cv_parser import parse_resume_to_json  
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def form_page():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'resume' not in request.files:
        return render_template('index.html', data=None)  # corrected

    file = request.files['resume']
    if file.filename == '':
        return render_template('index.html', data=None)  # corrected

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    parse_resume_to_json(filepath, "cv_data.json")
    with open("cv_data.json") as f:
        data = json.load(f)

    return render_template('index.html', data=data)  # corrected


if __name__ == '__main__':
    app.run(debug=True)
