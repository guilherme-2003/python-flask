#coding utf-8
from flask import Flask, render_template
app = Flask("projeto")

@app.route("/")
def ola_mundo():
    nome = "Guilherme Paulela"
    return render_template("alo.html", n=nome)

app.run()
