from flask import Flask, render_template
import pass_gen

app = Flask(__name__)

@app.route("/")
def homepage():
    """
    Render the homepage.

    Returns the rendered HTML template for the homepage.
    """
    return render_template("index.html")

@app.route("/generate")
def generate_password():
    """
    Generate a random password.

    Returns the generated password as plain text.
    """
    password = pass_gen.Generetor.password_gen()
    return password

if __name__ == '__main__':
    app.run(debug=True)