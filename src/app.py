from flask import Flask, jsonify


app = Flask(__name__)


def add(a, b):
    return a + b


@app.get("/")
def home():
    return jsonify(
        message="Hello from my Python app!",
        example="2 + 3 = 5",
        status="running",
    )


@app.get("/add/<int:a>/<int:b>")
def add_numbers(a, b):
    return jsonify(
        a=a,
        b=b,
        result=add(a, b),
    )


if __name__ == "__main__":
    app.run()
