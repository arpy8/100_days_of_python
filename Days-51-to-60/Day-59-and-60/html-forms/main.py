from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    username = request.form['password']
    password = request.form['username']
    return f"<h1>Name : {username}, Password: {password}</h1>"


if __name__ == "__main__":
    app.run()
