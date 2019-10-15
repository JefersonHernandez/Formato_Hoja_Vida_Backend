from typing import re
from Conexion import Conexion
from flask import Flask
from flask import render_template, redirect, request, url_for, jsonify
from Sistema import Sistema
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)

db = Sistema()
def usuarioExiste(usuario):
    """retorna True si el usuario existe en la base de datos"""
    respuesta = db.login(usuario)
    if respuesta:
        print('si existe')
        return True
    else:
        'no existe'
        return False

def esUsuarioValido(usuario,clave):
    """retorna True si las credenciales del usuario coinciden con las registradas en la base de datos"""
    respuesta = db.login(usuario)
    if respuesta[0][0] == clave:
        return True
    else:
        return False


def isUserValid(usuario,clave):
    respuesta = db.login(usuario)
    if respuesta:
        if respuesta[0][0] == clave:
            return True
        else:
            return False
    else:
        print('usuario invalido en isUserValid')
        return 'false'
"""
def validarUsuario(usuario,clave):
    respuesta = db.login(usuario)
    if respuesta:
        if respuesta[0][0] == clave:
            usuario_temporal = '1094'
            #usuario_estatico.setUser(usuario)
            #print(usuario_estatico.getUser())
            #print('mi jkkkkkkkkkkkk')
            #usuario_estatico.usuario = usuario
            return 'true'
        else:
            return 'false'
    else:
        return 'usuario no registrado'

@app.route('/login', methods=['GET', 'POST'])
def login():
    content = request.values
    return validarUsuario(content['documento'],content['clave'])
"""

@app.route('/obtenerPaises', methods=['GET','POST'])
def obtenerPaises():
    return jsonify(db.obtenerPaises())

@app.route('/traer_distrito_militar', methods=['GET','POST'])
def obtenerDistritoMilitar():
    return jsonify(db.obtenerDistritosMilitares())

@app.route('/info_libreta', methods=['GET','POST'])
def guardarInfoLibreta():
    content = request.values
    info_libreta = (content['numero_libreta'], content['clase_libreta'], content['distrito_militar'])
    return str(db.guardarInfoLibreta(info_libreta))

@app.route('/info_nacionalidad', methods=['GET','POST'])
def guardarInfoNacionalidad():
    content = request.values
    return str(db.guardarInfoNacionalidad((content['nacionalidad-pais'], content['documento'])))

@app.route('/info_personal', methods=['GET','POST'])
def guardarDatosPersona():
    content = request.values
    info_persona =(content['nombre_persona'],content['pApellido'],content['sApellido'],content['documento'],content['tDocumento'],content['sexo'])
    return str(db.guardarInfoPersona(info_persona))

@app.route('/obtenerDepartamentos', methods=['GET','POST'])
def obtenerDepartamentos():
    content = request.values
    return jsonify(db.obtenerDepartamentos(content['select-pais-nacimiento']))

@app.route('/obtenerDepartamentosCorrespondencia', methods=['GET','POST'])
def obtenerDepartamentosCorrespondencia():
    content = request.values
    return jsonify(db.obtenerDepartamentos(content['select-pais-correspondencia']))

@app.route('/obtenerMunicipios', methods=['GET','POST'])
def obtenerMunicipios():
    content = request.values
    return jsonify(db.obtenerMunicipios(content['select-departamento-nacimiento']))

@app.route('/obtenerMunicipiosCorrespondencia', methods=['GET','POST'])
def obtenerMunicipiosCorrespondencia():
    content = request.values
    return jsonify(db.obtenerMunicipios(content['select-departamento-correspondencia']))
    #return jsonify(Conexion.sqlGetData('SELECT MUNICIPIO.nombre, MUNICIPIO.codigo_municipio FROM MUNICIPIO WHERE MUNICIPIO.codigo_departamento ='+"'54'"))

@app.route('/info_nacimiento', methods=['GET','POST'])
def guardarInfoNacimiento():
    content = request.values
    info_persona =(content['documento'],content['select-pais-nacimiento'],content['select-departamento-nacimiento'],content['select-municipio-nacimiento'],content['fecha_nacimiento'])
    return str(db.guardarInfoNacimiento(info_persona))

@app.route('/info_correspondencia', methods=['GET','POST'])
def guardarInfoCorrespondencia():
    content=request.values
    info_persona =(content['documento'],content['direccion-correspondencia'],content['email-correspondencia'],content['telefono-correspondencia'],content['select-pais-correspondencia'],content['select-departamento-correspondencia'],content['select-municipio-correspondencia'])
    return str(db.guardarInfoCorrespondencia(info_persona))

###GUARDA TODO LA INFORMACION DE LA PERSONA EN LA BASE DE DATOS###
@app.route('/informacion_persona',methods=['GET','POST'])
def informacionPersonal():
   content = request.values
   usuario_sesion = content['d_sesion']
   clave_sesion = content['c_sesion']
   if isUserValid(usuario_sesion,clave_sesion):
       if content['check_libreta'] == 'true':
           datosLibreta = (content['numero_libreta'], content['clase_libreta'], content['distrito_militar'],content['numero_libreta'])
           db.guardarInfoLibreta(datosLibreta)

       datosPersona = (content['nombre_persona'],content['pApellido'],content['sApellido'],content['tDocumento'],content['sexo'])
       datosLibreta = ''
       datosNacionaldiad = (content['nacionalidad-pais'], usuario_sesion)
       datosNacimiento = (content['fecha_nacimiento'],content['select-pais-nacimiento'],content['select-departamento-nacimiento'],content['select-municipio-nacimiento'],usuario_sesion)
       datosCorrespondencia = (content['direccion-correspondencia'],content['select-pais-correspondencia'],content['select-departamento-correspondencia'],content['select-municipio-correspondencia'],content['telefono-correspondencia'],content['email-correspondencia'],usuario_sesion)
       print(usuario_sesion)
       print(content['documento'])

       db.guardarInfoPersona(datosPersona,usuario_sesion)
       print('paso')
       db.guardarInformacion(datosPersona, datosLibreta, datosNacionaldiad, datosNacimiento, datosCorrespondencia,usuario_sesion)
       return 'true'
   else:
       return 'false'

@app.route('/login_por_json',methods=['GET','POST'])
def login_por_json():
    content = request.values
    if usuarioExiste(content['documento']):
        print('se paso')
        if esUsuarioValido(content['documento'],content['clave']):
            return 'true'
        else:
            return 'false'
    else:
        print('user no existe 2')
        return 'false'

@app.route('/crear_cuenta',methods=['GET','POST'])
def crearCuenta():
    content = request.values
    if usuarioExiste(content['documento']):
        return 'false'
    else:
        db.crearCuenta((content['documento'],content['clave']))
    return 'true'
@app.route('/carga_datos_personales',methods=['GET','POST'])
def cargaDatosPersonales():
    content = request.values
    if esUsuarioValido(content['documento'],content['clave']):
        db_respuesta = db.cargaDatosPersonales(content['documento'])
        db_respuesta = db_respuesta[0]
        my_json = {
        'nombre' : db_respuesta[0],
        'primer_apellido' : db_respuesta[1],
        'segundo_apellido' : db_respuesta[2],
        'documento' : db_respuesta[3],
        'codigo_tipo_documento' : db_respuesta[4],
        'sexo' : db_respuesta[5]
        }
        return my_json
    else:
        return 'false'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    #app.run()
