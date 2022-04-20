from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Esse é meu primeiro site!!"

@app.route("/contatos")
def contatos():
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=True)
