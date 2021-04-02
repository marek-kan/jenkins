import flask

app = flask.Flask(__name__)

@app.route('/')
def home():
    return 'Hello world!'

def run_app():
    app = flask.Flask(__name__)
    app.run(port='9999')

def get_app():
    return app
    
if __name__ == '__main__':
    run_app()