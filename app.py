from flask import Flask, render_template, request
import random

app = Flask(__name__)

lower = "abcdefghijklmnopqrstuvwxyz"
higher = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "123456789"
symbols = "!@$%*;/,._-"
all_chars = lower + higher + numbers + symbols


def generate_password(length):
    return "".join(random.sample(all_chars, length))


@app.route("/", methods=["GET", "POST"])
def index():
    password = None

    if request.method == "POST":
        try:
            length = int(request.form.get("password_length"))
            password = generate_password(length)
        except ValueError:
            error_message = "Please enter a valid number for password length."

    return render_template("index.html", password=password)


if __name__ == "__main__":
    app.run(debug=True)
