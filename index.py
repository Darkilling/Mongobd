from flask import *
from conectar import *

db = conexion()
app = Flask(__name__)
@app.route('/')

def home():
    
    restaurantes = db.restaurants
    find = restaurantes.find() # db.restaurants.find()

    return render_template('index.html', restaurantes = find)

@app.route('/vecindario')
def vecindario():

    vecindarios = db.neighborhoods
    find = vecindarios.find()
    
    return render_template('vecindario.html', vecindarios = find )

if __name__ == '__main__':
    app.run(debug=True)