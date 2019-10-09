from typing import re

from flask import Flask
from flask import render_template, redirect, request, url_for, jsonify

from Sistema import Sistema
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)
@app.route('/login', methods=['GET', 'POST'])
def login():
    sistema = Sistema()
    content = request.values
    clave_db = sistema.login(content['username'], content['pass'])
    if clave_db[0][0] == content['pass']:
        return 'usuario valido'
    else:
        return 'usuario o contraseña invalido'

@app.route('/obtenerPaises', methods=['GET','POST'])
def obtenerPaises():
    sistema = Sistema()
    return jsonify(sistema.obtenerPaises())

@app.route('/traer_distrito_militar', methods=['GET','POST'])
def obtenerDistritoMilitar():
    sistema = Sistema()
    return jsonify(sistema.obtenerDistritosMilitares())

@app.route('/info_libreta', methods=['GET','POST'])
def guardarInfoLibreta():
    content = request.values
    info_libreta = (content['numero_libreta'], content['clase_libreta'], content['distrito_militar'])
    sistema = Sistema()
    return str(sistema.guardarInfoLibreta(info_libreta))

@app.route('/info_nacionalidad', methods=['GET','POST'])
def guardarInfoNacionalidad():
    content = request.values
    print(content['nacionalidad']+'nac')
    print(content['nacionalidad-pais']+'np')
    documento_prueba = '1209'
    aux = content['nacionalidad-pais']
    print('datos que van '+aux + documento_prueba)
    sistema = Sistema()
    return str(sistema.guardarInfoNacionalidad((aux, documento_prueba)))

@app.route('/info_personal', methods=['GET','POST'])
def guardarDatosPersona():
    content = request.values
    print(content)
    info_persona =(content['nombre_persona'],content['pApellido'],content['sApellido'],content['documento'],content['tDocumento'],content['sexo'])
    sistema = Sistema()
    return str(sistema.guardarInfoPersona(info_persona))

@app.route('/guardar_correspondencia', methods=['GET', 'POST'])
def guardarCorrespondencia():
    sistema = Sistema()
    content = request.values# el id de la correspondencia sera el mismo de persona
    datos = (content['documento'], content['direccion_correspondencia'], content['correo_correspondencia'])
    return str(sistema.guardadCorrespondencia(datos))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
