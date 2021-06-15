from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Congratulations, it's a web app!"

@app.route("/")
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"
