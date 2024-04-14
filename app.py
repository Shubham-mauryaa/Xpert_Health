import csv
from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
import diseaseprediction

app = Flask(__name__)
with open('templates/Testing.csv', newline='') as f:
    reader = csv.reader(f)
    symptoms = next(reader)
    symptoms = symptoms[:len(symptoms) - 1]

UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "cairoders-ednalan"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/scan')
def scan():
    return render_template('scanner.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        return render_template('scanner.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    # print('display_image filename: ' + filename)
    print("hello")
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/1')
def result():
    return render_template('1.html')

@app.route('/symptomchecker', methods=['GET'])
def dropdown():
    return render_template('includes/default.html', symptoms=symptoms)


@app.route('/disease_predict', methods=['POST'])
def disease_predict():
    selected_symptoms = []
    if (request.form['Symptom1'] != "") and (request.form['Symptom1'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom1'])
    if (request.form['Symptom2'] != "") and (request.form['Symptom2'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom2'])
    if (request.form['Symptom3'] != "") and (request.form['Symptom3'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom3'])
    if (request.form['Symptom4'] != "") and (request.form['Symptom4'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom4'])
    if (request.form['Symptom5'] != "") and (request.form['Symptom5'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom5'])

    disease = diseaseprediction.dosomething(selected_symptoms)
    return render_template('disease_predict.html', disease=disease, symptoms=symptoms)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('index.html')

@app.route('/diseases')
def diabetes():
    return render_template('diseases.html')

@app.route('/acidity')
def acidity():
    return render_template('acidity.html')

@app.route('/acne')
def acne():
    return render_template('acne.html')

@app.route('/allergy')
def allergy():
    return render_template('allergy.html')

@app.route('/anxiety')
def anxiety():
    return render_template('anxiety.html')

@app.route('/bodyache')
def bodyache():
    return render_template('bodyache.html')

@app.route('/catract')
def catract():
    return render_template('catract.html')

@app.route('/conjuctivitis')
def conjuctivitis():
    return render_template('conjuctivitis.html')

@app.route('/depresion')
def depresion():
    return render_template('depresion.html')

@app.route('/fever')
def fever():
    return render_template('fever.html')

@app.route('/foodpoision')
def foodpoision():
    return render_template('foodpoision.html')

@app.route('/kidneystone')
def kidneystone():
    return render_template('kidneystone.html')

@app.route('/lungcancer')
def lungcancer():
    return render_template('lungcancer.html')

@app.route('/nausea')
def nausea():
    return render_template('nausea.html')

if __name__ == '__main__':
    app.run(debug=True)
