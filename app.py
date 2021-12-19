from flask import Flask, jsonify, request
import pandas as pd

import config as cfg
import pipeline_predict as pp

app = Flask(__name__)

@app.route("/saludar")
def saludar():
    return jsonify({"username": "Stefanie"})

#ruta para predecir.
@app.route("/predecir", methods=['POST']) #Permite que desde la aplicación que se conecta al API, se puedan enviar parámetros
def predict_from_pp():
    json_data = request.get_json()
    dataframe = pd.json_normalize(json_data)
    data = dataframe

    #cambiar nombre
    data = data[cfg.FEATURES]
    data['is_canceled'] = data['is_canceled'].astype('O')
    data['is_repeated_guest'] = data['is_repeated_guest'].astype('O')
    resultado = pp.predict(data)
    print(resultado)
    return jsonify({"Prediccion": resultado})