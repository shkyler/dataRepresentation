# simple flask server
from flask import Flask

# i needed to define 'app' first
app = Flask(__name__, static_url_path='',static_folder='.')

@app.route('/car')
def getAll():
    return "in get all cars"

@app.route('/car/<int:id>')
def getCar(id):
  return "You want car " + str(id)

if __name__ == '__main__':
  app.run(debug=True)