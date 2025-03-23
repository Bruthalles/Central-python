import time
from flask import Flask,request, render_template, send_from_directory
from backend.programs.animals import catordog
app = Flask(__name__,template_folder="src/templates/",static_folder="src/static")

#///////////////////////  ROUTES  ///////////////////////////////      
@app.route('/')
def home():
    timestamp = time.time()
    return render_template('home/index.html',timestamp=timestamp)

@app.route('/animals')
def animal():
    timestamp = time.time()
    return render_template('animals/index.html',timestamp=timestamp)

@app.route('/banco')
def banco():
    timestamp = time.time()
    return render_template('bank/index.html',timestamp=timestamp)

@app.route('/garage')
def cars():
    timestamp = time.time()
    return render_template('cars/index.html',timestamp=timestamp)

@app.route('/locations')
def loc():
    timestamp = time.time()
    return render_template('elocations/index.html',timestamp=timestamp)

@app.route('/conversor')
def conversor():
    timestamp = time.time()
    return render_template("etemperature/index.html",timestamp=timestamp)

#obtendo resposta do form para verificação
@app.route('/animals',methods=['GET','POST'])
def processarcatordog():
    resultado = request.form.get('catordog').lower()
    return render_template('animals/index.html',resultado=resultado)

@app.route('/src/assets/')
def serve_assets(filename):
    return send_from_directory(filename)

#if __name__ == '__main__':
app.run(debug=True)
