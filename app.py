from flask import Flask, request, jsonify, render_template

x=1

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


def get_args():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return a, b, None
    except (TypeError, ValueError):
        return (None, None,
                "Invalid input. Please provide numbers for 'a' and 'b'.")


@app.route('/add')
def add():
    a, b, error = get_args()
    if error:
        return jsonify({"error": error}), 400
    return jsonify({"result": a + b})


@app.route('/subtract')
def subtract():
    a, b, error = get_args()
    if error:
        return jsonify({"error": error}), 400
    return jsonify({"result": a - b})


@app.route('/multiply')
def multiply():
    a, b, error = get_args()
    if error:
        return jsonify({"error": error}), 400
    return jsonify({"result": a * b})


@app.route('/divide')
def divide():
    a, b, error = get_args()
    if error:
        return jsonify({"error": error}), 400
    if b == 0:
        return jsonify({"error": "Division by zero is not allowed."}), 400
    return jsonify({"result": a / b})


@app.route('/modulo')
def modulo():
    a, b, error = get_args()
    if error:
        return jsonify({"error": error}), 400
    if b == 0:
        return jsonify({"error": "Modulo by zero is not allowed."}), 400
    return jsonify({"result": a % b})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
