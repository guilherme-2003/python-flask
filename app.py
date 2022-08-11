#coding utf-8
from flask import Flask, render_template
app = Flask("projeto")

@app.route("/")
def ola_mundo():
    nome = "Guilherme Paulela"
    produtos = [
        {"nome": "Ração", "preco": 199.99}, 
        {"nome": "Playstation", "preco": 1999.99}]

    return render_template("alo.html", n=nome, aProdutos=produtos)

app.run()
