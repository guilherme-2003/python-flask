#coding utf-8

# Rota raiz
from flask import Flask, render_template, request, session, redirect, url_for
app = Flask("projeto")
# Criando uma chave de criptografia
app.secret_key = "AOHFASIDHUSID#*#)!H@#BWQHBad0ia0s"

@app.route("/")
def ola_mundo():
    nome = "Guilherme Paulela"
    produtos = [
        {"nome": "Ração", "preco": 199.99}, 
        {"nome": "Playstation", "preco": 1999.99}]

    return render_template("alo.html", n=nome, aProdutos=produtos), 200

# Nova rota teste
@app.route("/teste")
@app.route("/teste/<variavel>")
def funcao_teste(variavel = ""):
    return "Nova rota teste<br>Variável: {}".format(variavel), 200

# Rota formulario
@app.route("/form")
def form():
    return render_template("form.html"), 200

# Rota tratamento do formulário
@app.route("/form_recebe", methods=["GET", "POST"])
def form_recebe():
    nome = ""
    if request.method == "POST":
        nome = request.form["nome"]
        return f"Nome: {nome}", 200
    else:
        return "Não pode chamar direto no GET", 200

# Rota form de login
@app.route('/login')
def login():
    return render_template("login.html"), 200

# Rota para validar o formulário
@app.route("/login_validar", methods=["POST"])
def login_validar():
    if request.form["usuario"] == "gui" and request.form["senha"] == "123":
        session["usuario"] = request.form["usuario"]
        session["codigo"] = 1
        return redirect(url_for("acesso_restrito"))
    else:
        return "Usuário/senha inválidos! Por favor digite novamente.", 200

# Rota para área restrita
@app.route("/restrito")
def acesso_restrito():
    if session["codigo"] == 1:
        return f"Bem vindo a área restrita!<br>Usuário: {session['usuario']}<br>Código: {session['codigo']}", 200
    else:
        return "Acesso inválido", 200

app.run()

