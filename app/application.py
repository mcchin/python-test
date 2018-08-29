from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World, Update wsgi"

if __name__ == '__main__':
    app.run(debug=True)
