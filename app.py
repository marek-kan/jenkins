import flask

app = flask.Flask(__name__)

@app.route('/')
def home():
    return 'Hello world!'

if __name__ == '__main__':
    app.run(port=9999)