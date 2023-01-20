from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/observatorio")
def observatorio():
    return render_template("observatorio.html")    

@app.route("/transporte")
def transporte():
    return render_template("transporte.html")

@app.route("/transito")
def transito():
    return render_template("transito.html")

@app.route("/infraestructura")
def infraestructura():
    return render_template("infraestructura.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")
    
if __name__ == "__main__":
    app.run(debug=True)