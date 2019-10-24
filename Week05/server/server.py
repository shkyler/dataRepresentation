# simple flask server
from flask import Flask

# i needed to define 'app' first
app = Flask(__name__)
@app.route('/')
def index():
    return"Hello, World!"

if __name__ == '__main__':
  app.run(debug=True)