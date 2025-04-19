import time, re,os
from backend.classes.Car import Car
from datetime import timedelta
from data.db import db, init_db
from data.models import User
from dotenv import load_dotenv
from flask import Flask,request,jsonify,redirect, session,url_for,render_template, send_from_directory
from flask_cors import CORS

#defining source folders
app = Flask(__name__,template_folder="src/templates/",static_folder="src/static")
CORS(app) #habilita requisições js

#conections
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # evita warnings

init_db(app)

#secret-key
load_dotenv()
app.secret_key = os.getenv("SECRET_KEY")
#life time session
app.permanent_session_lifetime = timedelta(minutes=2)

#global message error
error='Email ou senha incorretos'
#///////////////////////  ROUTES  ///////////////////////////////

#Page home:
@app.route('/')
def home():
    timestamp = time.time()
    return render_template('home/index.html',timestamp=timestamp)
########################

#All about page animals
@app.route('/animals')
def animal():
    timestamp = time.time()
    return render_template('animals/index.html',timestamp=timestamp)
##########################

#All about page bank
@app.route('/banco-login')
def banco():
    timestamp = time.time()
    return render_template('bank/index.html',timestamp=timestamp)

@app.route('/timeout')
def timeout():
    timestamp = time.time()
    return render_template('bank/timeout.html',timestamp=timestamp)
#############################

#All about page garage
@app.route('/garage')
def cars():
    timestamp = time.time()
    return render_template('cars/index.html',timestamp=timestamp)

@app.route('/garage',methods=['POST'])
def enviar_carros():
    data = request.json
    marca = data.get("marca")
    modelo = data.get("modelo")
    ano = data.get("ano")
    carro = Car(marca,modelo,ano)
    view_carro = jsonify({"carro": {"Marca":carro.marca, "Modelo": carro.modelo, "Ano":carro.ano}})
    return view_carro

#########################

#All about page locations
@app.route('/locations')
def loc():
    timestamp = time.time()
    return render_template('elocations/index.html',timestamp=timestamp)

#################################

#All about page conversor
@app.route('/conversor')
def conversor():
    timestamp = time.time()
    return render_template("etemperature/index.html",timestamp=timestamp)

 #############################  

#///////////// FUNCTIONS OF LOGIN ////////////////////////
@app.route('/sign-in',methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        newemail = request.form.get('newemail')
        newpassword = request.form.get('newpassword')
        passpattern = r"^.{4}$"
        email_pattern = r"^\b\w+@\w+\.\w+\b$"
        if re.fullmatch(email_pattern, newemail) and re.fullmatch(passpattern, newpassword):
            user = User.query.filter_by(email=newemail).first()
            if user:
                return render_template('bank/signin.html', error="Usuário já existe")
            else:
                new_user = User(email=newemail, password=newpassword)
                db.session.add(new_user)
                db.session.commit()
                print(new_user)
                return redirect(url_for('login'))
        else:
            return render_template('bank/signin.html', error="Formato do email ou senha inválido")
    return render_template('bank/signin.html')

@app.route('/banco-login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        passpattern = r"^.{4}$"
        pattern = r"^\b\w+@\w+\.\w+\b$"
    
        if re.fullmatch(pattern, email) and re.fullmatch(passpattern,password):
            user = User.query.filter_by(email=email).first()
            if user and user.password == password:
                session["user"] = email
                return redirect(url_for('count'))
            else: 
                return render_template('bank/index.html',error=error)
        else:
            return render_template('/bank/index.html',error="Formato de email ou senha inválido")
    
    return render_template('/bank/index.html')
   
@app.route('/conta-bancaria')
def count():
    if "user" in session:
        return render_template('/bank/count.html')
    return redirect(url_for('timeout'))

@app.route('/logout')
def logout():
    session.pop("user",None)
    return redirect(url_for('login'))

app.run(debug=True)