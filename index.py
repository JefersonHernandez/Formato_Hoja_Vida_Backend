from Conexion import Conexion
from flask import Flask
from flask import render_template, request, jsonify
from Sistema import Sistema
from flask_cors import CORS
from Excepciones import UniqueViolation
app = Flask(__name__)
cors = CORS(app)

db = Sistema()
def usuarioExiste(usuario):
    """retorna True si el usuario existe en la base de datos"""
    try:
        if db.login(usuario):
            return True
        else:
            return False
    except Exception as e:
        print('Exception usuarioExiste')
    finally:
        pass

def esUsuarioValido(usuario,clave):
    """retorna True si las credenciales del usuario coinciden con las registradas en la base de datos"""
    try:
        if db.login(usuario)[0][0] == clave:
            return True
        else:
            return False
    except Exception as e:
        print('Exception esUsuarioValido')
    finally:
        pass

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
   try:
        if 'fecha_nacimiento' not in content:
            raise  ValueError('Por favor seleccione una fecha de nacimiento')
        if 'select-pais-nacimiento' not in content:
            raise ValueError('Por favor seleccione un pais de nacimiento')
        if 'select-departamento-nacimiento' not in content:
            raise  ValueError('Por favor seleccione una departamento de nacimiento')
        if 'select-municipio-nacimiento' not in content:
            raise ValueError('Por favor seleccione una municipio de nacimiento')
        if 'select-departamento-correspondencia' not in content:
            raise  ValueError('Por favor seleccione una departamento de correspondencia')
        if 'select-municipio-correspondencia' not in content:
            raise ValueError('Por favor seleccione una municipio de correspondencia')
        usuario_sesion = content['d_sesion']
        clave_sesion = content['c_sesion']
        if esUsuarioValido(usuario_sesion,clave_sesion):
            if content['check_libreta'] == 'true':
                try:
                    print(content)
                    datosLibreta = (content['numero_libreta'],content['clase_libreta'], content['distrito_militar'],usuario_sesion)
                    res = db.guardarInfoLibreta(datosLibreta,content['numero_libreta'])
                    print('res')
                    #print(res)
                    print('res')
                except Exception as e:
                    print(e)
                    print('error al guardar libreta')
                finally:
                    pass

            else:
                #SI LA PERSONA NO TIENE LIBRETA MILITAR SE REALIZA ESTE BLOQUE
                print('no tiene libreta militar')
            datosPersona = (content['nombre_persona'],content['pApellido'],content['sApellido'],content['tDocumento'],content['sexo'])
            datosNacionaldiad = (content['nacionalidad-pais'], usuario_sesion)
            datosNacimiento = (content['fecha_nacimiento'],content['select-pais-nacimiento'],content['select-departamento-nacimiento'],content['select-municipio-nacimiento'],usuario_sesion)
            datosCorrespondencia = (content['direccion-correspondencia'],content['select-pais-correspondencia'],content['select-departamento-correspondencia'],content['select-municipio-correspondencia'],content['telefono-correspondencia'],content['email-correspondencia'],usuario_sesion)
            try:
                db.guardarInfoNacionalidad(datosNacionaldiad)
            except UniqueViolation as e:
                pass
            #db.guardarInfoNacionalidad(datosNacionaldiad)
            db.guardarInfoNacimiento(datosNacimiento)
            db.guardarInfoCorrespondencia(datosCorrespondencia)
            db.guardarInfoPersona(datosPersona,usuario_sesion)
            return 'true'
        else:
            return 'false'
   except Exception as e:
       return str(e)
   finally:
       pass

@app.route('/login_por_json',methods=['GET','POST'])
def login_por_json():
    try:
        content = request.values
        if usuarioExiste(content['documento']):
            if esUsuarioValido(content['documento'],content['clave']):
                return 'true'
            else:
                return 'false'
        else:
            return 'false'
    except Exception as e:
        print('Exception login_por_json')
    finally:
        pass

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
    try:
        if esUsuarioValido(content['documento'],content['clave']):
            datos_personales = db.cargaDatosPersonales(content['documento'])[0]
            nombre_departamento_nacimiento = db.obtenerNombreDepartamento(datos_personales[8])[0] if datos_personales[8] != None else 'null'
            nombre_departamento_correspondencia = db.obtenerNombreDepartamento(datos_personales[11])[0] if datos_personales[11] != None else 'null'
            nombre_municipio_nacimiento = db.obtenerNombreMunicipio(datos_personales[9])[0] if datos_personales[9] != None else 'null'
            nombre_municipio_correspondencia = db.obtenerNombreMunicipio(datos_personales[12])[0] if datos_personales[12] != None else 'null'
            nombre_pais_correspondencia = db.obtenerNombrePais(datos_personales[10])[0] if datos_personales[10] != None else 'null'
            nombre_pais_nacimiento = db.obtenerNombrePais(datos_personales[7])[0] if datos_personales[7] != None else 'null'
            my_json = {
            'nombre' : (datos_personales[0] if datos_personales[0] != None else 'null'),
            'primer_apellido' : (datos_personales[1] if datos_personales[1] != None else 'null'),
            'segundo_apellido' : (datos_personales[2] if datos_personales[2] != None else 'null'),
            'documento' : (datos_personales[3] if datos_personales[3] != None else 'null'),
            'codigo_tipo_documento' : (datos_personales[4] if datos_personales[4] != None else 'null'),
            'sexo' : (datos_personales[5] if datos_personales[5] != None else 'null'),
            'fecha_nacimiento' : (datos_personales[6] if datos_personales[6] != None else 'null'),
            'codigo_pais_nacimiento' : (datos_personales[7] if datos_personales[7] != None else 'null'),
            'codigo_departamento_nacimiento' : (datos_personales[8] if datos_personales[8] != None else 'null'),
            'codigo_municipio_nacimiento' : (datos_personales[9] if datos_personales[9] != None else 'null'),
            'codigo_pais_correspondencia' : (datos_personales[10] if datos_personales[10] != None else 'null'),
            'codigo_departamento_correspondencia' : (datos_personales[11] if datos_personales[11] != None else 'null'),
            'codigo_municipio_correspondencia' : (datos_personales[12] if datos_personales[12] != None else 'null'),
            'telefono_correspondencia' : (datos_personales[13] if datos_personales[13] != None else 'null'),
            'email_correspondencia': (datos_personales[14] if datos_personales[14] != None else 'null'),
            'direccion_correspondencia' : (datos_personales[15] if datos_personales[15] != None else 'null'),
            'nombre_departamento_nacimiento' : (nombre_departamento_nacimiento[0] if nombre_departamento_nacimiento[0] != None else 'null'),
            'nombre_municipio_nacimiento' : (nombre_municipio_nacimiento[0] if nombre_municipio_nacimiento[0] != None else 'null'),
            'nombre_departamento_correspondencia' : (nombre_departamento_correspondencia[0] if nombre_departamento_correspondencia[0] != None else 'null'),
            'nombre_municipio_correspondencia' : (nombre_municipio_correspondencia[0] if nombre_municipio_correspondencia[0] != None else 'null'),
            'nombre_pais_correspondencia' : (nombre_pais_correspondencia[0] if nombre_pais_correspondencia[0] != None else 'null'),
            'nombre_pais_nacimiento' : (nombre_pais_nacimiento[0] if nombre_pais_nacimiento[0] != None else 'null')
            }
            return my_json
        else:
            return 'false'
    except Exception as e:
        print('Exception Carga Datos Personales '+e)
        return 'false'
    finally:
        pass

@app.route('/carga_libreta',methods=['GET','POST'])
def cargaLibreta():
    content = request.values
    try:
        if esUsuarioValido(content['documento'],content['clave']):
            datos_libreta = db.obtenerLibreta(content['documento'])
            nombre_distrito = db.obtenerDistritoMilitar(datos_libreta[0][2]) if datos_libreta else 'null'
            nacionalidad = db.obtenerNacionalidades(content['documento'])
            if datos_libreta:
                libreta ={
                'numero' : datos_libreta[0][0],
                'tipo' : datos_libreta[0][1],
                'codigo_distrito' : datos_libreta[0][2],
                'nombre_distrito' : nombre_distrito[0][0],
                'codigo_pais_nacionalidad' : nacionalidad[0][0],
                'nombre_pais_nacionalidad' : nacionalidad[0][1]
                }
                print(datos_libreta)
                return libreta
            else:
                print('npo hubo libreta')
                return 'false'
        else:
            return 'false'
    except Exception as e:
        print('Error Libreta' + e)
        return 'false'
    finally:
        pass

@app.route('/carga_datos_educacion_basica', methods=['GET','POST'])
def cargaDatosEducacion():
    content = request.values
    try:
        if esUsuarioValido(content['documento'],content['clave']):
            educacion_basica = db.obtenerEducacionBasica(content['documento'])
            if educacion_basica:
                my_json={
                'titulo' : educacion_basica[0][0],
                'grado' : educacion_basica[0][1],
                'fecha_grado' :educacion_basica[0][2]
                }
                return my_json
            else:
                print('no hubo')
                return 'false'
        else:
            return 'false'
    except Exception as e:
        print('Exception Carga Datos Educacion '+e)
        return 'false'
    finally:
        pass

@app.route('/carga_datos_educacion_superior',methods=['GET','POST'])
def cargaDatosEducacionSuperior():
    content = request.values
    try:
        if esUsuarioValido(content['documento'],content['clave']):
            educacion_superior = db.obtenerEducacionSuperior(content['documento'])
            return jsonify(educacion_superior)
        else:
            return 'false'
    except Exception as e:
            print('Exception Carga Datos Educacion Superior '+e)
    finally:
            pass
@app.route('/guardar_educacion_superior',methods=['GET','POST'])
def guardarEducacionSuperior():
    try:
        content = request.values
        db.guardarEducacionSuperior((content['nombreEstudio'],content['selectModalidad'],content['semestresAprobados'],content['graduado'],content['fechaTerminacion'],content['numeroTarjeta'],content['d_sesion']))
        return 'true'
    except Exception as e:
        print('Exception Carga Datos Educacion Superior '+e)
        return 'false'
    finally:
        pass
@app.route('/guardar_educacion_basica',methods=['GET','POST'])
def guardarEducacionBasica():
    content = request.values#documento,titulo, grado,fecha_grado
    try:
        db.guardarEducacionBasica((content['d_sesion'],content['tituloBasica'],content['grado'],content['fechaGrado']))
        return 'true'
    except UniqueViolation as e:
        db.actualizarEducacionBasica((content['tituloBasica'],content['grado'],content['fechaGrado'],content['d_sesion']))
        return 'true'
    except Exception as e:
        return 'false'
    finally:
        pass

@app.route('/obtener_empleos',methods=['GET','POST'])
def obtenerEmpleos():
    content = request.values
    try:
        if esUsuarioValido(content['documento'],content['clave']):
            empleos = db.obtenerEmpleos(content['documento'])
            print(empleos)
            if empleos:
                return jsonify(empleos)
            else:
                return 'false'
        else:
            return 'false'
    except Exception as e:
        print('eror en ontener_empleos')
        print(e)
        return 'false'

@app.route('/obtener_tiempo_experiencia',methods=['GET','POST'])
def obtenerTiempoExperienciaLaboral():
    try:
        return 'false'
    except Exception as e:
        return 'false'

@app.route('/carga_datos_idiomas',methods=['GET','POST'])
def obtenerIdiomas():
    try:
        return 'false'
    except Exception as e:
        return 'false' 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
