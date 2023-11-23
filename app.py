from flask import Flask

app = Flask(__name__)


@app.route('/f/<celsius>')
def convert_fahrenheit(celsius):
    return str(celsius_to_fahrenheit(float(celsius)))


@app.route('/c/<fahrenheit>')
def convert_celsius(fahrenheit):
    return str(fahrenheit_to_celsius(float(fahrenheit)))


def fahrenheit_to_celsius(fahrenheit):
    """Converts fahrenheit to celsius."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def celsius_to_fahrenheit(celsius):
    """Converts celsius to fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    app.run()
