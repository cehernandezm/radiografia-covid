import os
from flask import Flask, jsonify, request
import json
from flask_cors import CORS, cross_origin
import tensorflow as tf
from tensorflow import keras
import base64
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from datetime import datetime

app = Flask(__name__)
app.debug = True
CORS(app)
modelo = tf.keras.models.load_model(
    os.path.abspath(os.getcwd()) + '/api/keras_model/modelo')


################################################### RUTAS ##############################################

@app.route("/", methods=['POST'])
def index():
    imagen = request.json['imagen']
    database64 = (imagen.split(sep="base64,"))[1]
    img = base64.b64decode(database64)
    now = datetime.now()
    filename = os.path.abspath(os.getcwd(
    )) + '/api/upload/images/test-' + now.strftime("%d-%m-%Y-%H-%M-%S") + '.png'
    with open(filename, 'wb') as f:
        f.write(img)

    labels = ["COVID-19", "NORMAL", "Viral Pneumonia"]

    image_custom = ImageDataGenerator(
        rescale=1./255
    )
    test_dir = os.path.abspath(os.getcwd()) + '/api/upload'
    print(test_dir)
    generatorCustom = image_custom.flow_from_directory(
        directory=test_dir,
        batch_size=1,
        shuffle=False
    )

    y_prob = modelo.predict_generator(generatorCustom)
    y_pred = np.argmax(y_prob)

    print(y_prob)
    print(y_pred)
    os.remove(filename)
    response = jsonify({
        'status': 200,
        'msg' : labels[y_pred]
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
