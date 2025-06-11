import flask

app = flask.Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello, World!"

if __name__ == "__main__":
#    app.run(debug=True)
#    app.run(debug=True, port=6666)
#    app.run(debug=True, port=6666, host='0.0.0.0')
    app.run(debug=True, port=7777, host='0.0.0.0')
#    app.run(debug=True, host='0.0.0.0', port=5555)