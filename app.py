from flask import Flask, render_template

app = Flask(__name__,template_folder="src/pages")

@app.route('/')
def home():
    return render_template('home/index.html')

@app.route('/animals')
def animal():
    return render_template('animals/index.html')

@app.route('/banco')
def banco():
    return render_template('bank/index.html')

@app.route('/garage')
def cars():
    return render_template('cars/index.html')

@app.route('/locations')
def loc():
    return render_template('elocations/index.html')

@app.route('/conversor')
def conversor():
    return render_template("etemperature/index.html")

if __name__ == '__main__':
    app.run(debug=True)
