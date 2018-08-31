import os
import settings
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World, Update wsgi" + ":" + os.getenv('ABC')

if __name__ == '__main__':
    app.run(debug=True)
