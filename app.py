from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello world!<br>Version1.0.1'

def run_app(port=8080):
    app = flask.Flask(__name__)
    app.run(port=port)

def get_app():
    return app
    
if __name__ == '__main__':
    run_app()