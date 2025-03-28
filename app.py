import time
import re
from flask import Flask,request, render_template, send_from_directory
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

@app.route('/banco-login')
def banco():
    timestamp = time.time()
    return render_template('bank/index.html',timestamp=timestamp)

@app.route('/conta-bancaria')
def conta():
    timestamp = time.time()
    return render_template('bank/count.html',timestamp=timestamp)

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

#///////////// LOGIN ////////////////////////
'''
@app.route('/banco-login', methods=['GET','POST'])
def verify_email():
    
    
    pattern = r"^\b\w+@\w+\.\w+\b$"
    enter_email = request.form.get('email')
    if not enter_email:
        return render_template('/bank/index.html',error="nenhum email fornecido.")
    
     validação no formato de email
    if re.fullmatch(pattern, enter_email):
        return render_template('/bank/index.html', input=enter_email)
    else: return render_template('/bank/index.html', error="email invalido")'''

@app.route('/banco-login',methods=['GET','POST'])
def login():
    email = "thalles@1"
    password = "1234"
    in_email = request.form.get('email')
    in_pass = request.form.get('password')

    if in_email == email and in_pass == password:
        return render_template('/bank/count.html')
    else:
        return render_template('/bank/index.html',error='Email ou senha incorretos')
   

    