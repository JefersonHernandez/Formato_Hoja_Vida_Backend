from typing import re
from Conexion import Conexion
from flask import Flask
from flask import render_template, redirect, request, url_for, jsonify

from Sistema import Sistema
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)
"""@app.route('/login', methods=['GET', 'POST'])
def login():
    sistema = Sistema()
    content = request.values
    clave_db = sistema.login(content['username'], content['pass'])
    if clave_db[0][0] == content['pass']:
        return 'usuario valido'
    else:
        return 'usuario o contraseña invalido'
"""
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

@app.route('/obtenerDepartamentos', methods=['GET','POST'])
def obtenerDepartamentos():
    print('==========================')
    content = request.values
    print(content)
    print('==========================')
    sistema = Sistema()
    return jsonify(sistema.obtenerDepartamentos(content['select-pais-nacimiento']))

@app.route('/obtenerDepartamentosCorrespondencia', methods=['GET','POST'])
def obtenerDepartamentosCorrespondencia():
    print('===>')
    print('==========>')
    print('=======================>')
    content = request.values
    print(content)
    sistema = Sistema()
    return jsonify(sistema.obtenerDepartamentos(content['select-pais-correspondencia']))

@app.route('/obtenerMunicipios', methods=['GET','POST'])
def obtenerMunicipios():
    print('==========================')
    content = request.values
    print(content)
    print('==========================')
    sistema = Sistema()
    return jsonify(sistema.obtenerMunicipios(content['select-departamento-nacimiento']))

@app.route('/obtenerMunicipiosCorrespondencia', methods=['GET','POST'])
def obtenerMunicipiosCorrespondencia():
    content = request.values
    print(content)
    sistema = Sistema()
    return jsonify(sistema.obtenerMunicipios(content['select-departamento-correspondencia']))
    #return jsonify(Conexion.sqlGetData('SELECT MUNICIPIO.nombre, MUNICIPIO.codigo_municipio FROM MUNICIPIO WHERE MUNICIPIO.codigo_departamento ='+"'54'"))

@app.route('/info_nacimiento', methods=['GET','POST'])
def guardarInfoNacimiento():
    content = request.values
    print(content)
    print('DOCUMENTO_PRUEBA1212' +'2')
    info_persona =('2',content['select-pais-nacimiento'],content['select-departamento-nacimiento'],content['select-municipio-nacimiento'],content['fecha_nacimiento'])
    sistema = Sistema()
    return str(sistema.guardarInfoNacimiento(info_persona))

@app.route('/info_correspondencia', methods=['GET','POST'])
def guardarInfoCorrespondencia():
    content = request.values
    #print('DOCUMENTO_PRUEBA111' +'2')
    print(content)
    #print('DOCUMENTO_PRUEBA' +'2')
    info_persona =('7',content['direccion-correspondencia'],content['email-correspondencia'],content['telefono-correspondencia'],content['select-pais-correspondencia'],content['select-departamento-correspondencia'],content['select-municipio-correspondencia'])
    #info_persona =('2',content['select-pais-nacimiento'],content['select-departamento-nacimiento'],content['select-municipio-nacimiento'],content['fecha_nacimiento'])
    sistema = Sistema()
    return str(sistema.guardarInfoCorrespondencia(info_persona))

###################TEST#############################
@app.route('/login',methods = ['GET', 'POST'])
def login():
    content = request.values
    clave_prueba = '0000'
    if content['clave'] == clave_prueba:
        return 'usuario existe'
    else:
        return 'usuario no existe'

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=port, debug=True)
    app.run()
