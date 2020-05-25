from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("home2"))

@app.route("/home")
def home2():
    return "Welcome to home!"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home2"))

if __name__ == "__main__":
    app.run()