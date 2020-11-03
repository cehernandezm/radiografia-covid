import os
from flask import Flask,jsonify,request
import json
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.debug = True 
CORS(app)




################################################### RUTAS ##############################################

@app.route("/",methods=['GET'])
def index():
    data = abrirArchivo(direccion + 'cpu-module')
    if (data == 0):
        response = jsonify({'status':400, 'data':'no existe un archivo de informacion para el cpu'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    
    data = json.loads(data)
    hz = data["HZ"]
    total = data["tiempo"]
    segundos = data["segundos"]

    porcentaje = ((total / hz) / segundos) * 100

    #print(data)

    dataMemoria = abrirArchivo(direccion + 'memoria-module')
    if (dataMemoria == 0):
            response = jsonify({'status':400, 'data':'no existe un archivo de informacion para la memoria'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
    
    dataMemoria = json.loads(dataMemoria)
    #print(dataMemoria)
    
    response = jsonify({
        'status':200, 
        'cpu': porcentaje,
        'total' : dataMemoria['total'],
        'libre' : dataMemoria['libre'],
        'ram' : dataMemoria['uso']
        })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response







if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)