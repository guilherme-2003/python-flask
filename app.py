#coding utf-8
from flask import Flask, render_template
app = Flask("projeto")

@app.route("/")
def ola_mundo():
    return render_template("alo.html")

app.run()
