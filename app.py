from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Esse é meu primeiro site!!"

@app.route("/contatos")
def contatos():
    return render_template("base.html")

@app.route("/about")
def sobre():
    return render_template("about.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return nome_usuario

if __name__ == "__main__":
    app.run(debug=True)
