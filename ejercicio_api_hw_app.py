from flask import Flask, request
from sqlalchemy import create_engine
import pandas as pd

# Dirección de la base de datos SQLite
churro = "sqlite:///dbnamehw.db"
engine = create_engine(churro)

# Inicializa la app de Flask
app = Flask(__name__)

# Ruta para obtener todos los libros (ejemplo básico)
@app.route('/api/v0/resources/books/all', methods=['GET'])
def get_books():
    query = "SELECT * FROM books"
    results = pd.read_sql(query, con=engine)
    return results.to_html()

# Ruta para obtener datos con filtro opcional
@app.route("/get_data", methods=['GET'])
def get_data():
    filtro = request.args.get("filtro", None)
    if filtro:
        query = f"SELECT * FROM datos WHERE col2 = '{filtro}' LIMIT 1000"
    else:
        query = "SELECT * FROM datos LIMIT 1000"
    results = pd.read_sql(query, con=engine)
    return results.to_html()

# Ruta de prueba para verificar la conexión
@app.route("/hola", methods=['GET'])
def connect():
    return "Todo ok"

# Ruta de bienvenida
@app.route("/", methods=['GET'])
def welcome():
    return '''<h1 style="color:red">Welcome</h1>'''

# Ejecuta la app
if __name__ == "__main__":
    app.run(debug=True)

