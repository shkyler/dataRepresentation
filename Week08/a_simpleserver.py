# simple flask server
from flask import Flask
from flask_cors import CORS

# i needed to define 'app' first
app = Flask(__name__, static_url_path='',static_folder='.')

CORS(app)

@app.route('/')
def index():
    return"Hello, World!"

@app.route('/car/<int:id>')
def getCar(id):
  return "You want car " + str(id)

if __name__ == '__main__':
  app.run(debug=True)