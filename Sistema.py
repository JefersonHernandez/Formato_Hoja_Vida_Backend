from Conexion import Conexion
import psycopg2


class Sistema(object):
    """doc"""

    def guardarInfoCorrespondencia(self, datos):
        #sql = "INSERT INTO CORRESPONDENCIA (codigo_persona, direccion, email, telefono,codigo_pais,codigo_departamento,codigo_municipio) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        sql = "UPDATE PERSONA SET direccion_correspondencia=%s,codigo_pais_correspondencia=%s,codigo_departamento_correspondencia=%s,codigo_municipio_correspondencia=%s,telefono_correspondencia=%s,email_correspondencia=%s WHERE documento = %s"
        return Conexion.sqlExecute(sql, datos)

    def getPersona(self, documento):
        sql = "SELECT * FROM PERSONA WHERE DOCUMENTO = " + documento
        datos = Conexion.sqlGetData(sql)
        print(datos)

    def login(self, documento):
        sql = "SELECT clave FROM PERSONA WHERE documento = '"+documento+"'"
        return Conexion.sqlGetData(sql)

    def obtenerPaises(self):
        sql = "SELECT PAIS.nombre, PAIS.codigo FROM PAIS"
        return Conexion.sqlGetData(sql)

    def guardarInfoPersona(self,datos,documento):
        sql = "UPDATE PERSONA SET nombre=%s,primer_apellido=%s,segundo_apellido=%s,codigo_tipo_documento=%s,sexo=%s WHERE documento ='"+documento+"'"
        return Conexion.sqlExecute(sql, datos)

    def crearLibreta(self,datos):
        sql ="INSERT INTO LIBRETA_MILITAR (numero,tipo,codigo_distrito,documento_persona) values(%s,%s,%s,%s)"
        Conexion.sqlExecute(sql, datos)

    def guardarInfoLibreta(self,datos,numero):
        print(datos)
        sql = "UPDATE LIBRETA_MILITAR SET numero=%s,tipo=%s,codigo_distrito=%s ,documento=%s where numero ='"+numero+"'"
        return Conexion.sqlExecute(sql, datos)

    def guardarInfoNacionalidad(self,datos):
        sql = "INSERT INTO NACIONALIDAD (codigo_pais, documento_persona) VALUES(%s,%s)"
        return Conexion.sqlExecute(sql, datos)

    def obtenerDistritosMilitares(self):
        sql = "SELECT DISTRITO_MILITAR.nombre, DISTRITO_MILITAR.codigo FROM DISTRITO_MILITAR"
        return Conexion.sqlGetData(sql)

    def obtenerDepartamentos(self, codigo_pais):
        sql = "SELECT DEPARTAMENTO.nombre, DEPARTAMENTO.codigo FROM DEPARTAMENTO WHERE DEPARTAMENTO.codigo_pais =  '"+codigo_pais+"'"
        return Conexion.sqlGetData(sql)

    def obtenerMunicipios(self, codigo_departamento):
        sql = "SELECT MUNICIPIO.nombre, MUNICIPIO.codigo FROM MUNICIPIO WHERE MUNICIPIO.codigo_departamento =  '"+codigo_departamento+"'"
        return Conexion.sqlGetData(sql)

    def guardarInfoNacimiento(self,datos):
        sql = "UPDATE PERSONA SET fecha_nacimiento =%s,codigo_pais_nacimiento=%s,codigo_departamento_nacimiento=%s,codigo_municipio_nacimiento=%s WHERE documento = %s"
        return Conexion.sqlExecute(sql, datos)

    def crearCuenta(self,datos):
        sql = 'INSERT INTO PERSONA (documento,clave) VALUES (%s,%s)'
        return Conexion.sqlExecute(sql,datos)

    def cargaDatosPersonales(self,documento):
        sql = "SELECT PERSONA.nombre, PERSONA.primer_apellido, PERSONA.segundo_apellido,PERSONA.documento,PERSONA.codigo_tipo_documento,PERSONA.sexo,PERSONA.fecha_nacimiento,PERSONA.codigo_pais_nacimiento,PERSONA.codigo_departamento_nacimiento,PERSONA.codigo_municipio_nacimiento,PERSONA.codigo_pais_correspondencia,PERSONA.codigo_departamento_correspondencia,PERSONA.codigo_municipio_correspondencia,PERSONA.telefono_correspondencia,PERSONA.email_correspondencia,PERSONA.direccion_correspondencia FROM PERSONA WHERE PERSONA.documento = '"+documento+"'"
        return Conexion.sqlGetData(sql)

    def obtenerNombreDepartamento(self, codigo_departamento):
        sql ="SELECT DEPARTAMENTO.nombre FROM DEPARTAMENTO  WHERE DEPARTAMENTO.codigo = '"+codigo_departamento+"'"
        return Conexion.sqlGetData(sql)

    def obtenerNombreMunicipio(self, codigo_municipio):
        sql = "SELECT MUNICIPIO.nombre FROM MUNICIPIO WHERE MUNICIPIO.codigo ='"+codigo_municipio+"'"
        return Conexion.sqlGetData(sql)

    def obtenerNombrePais(self, codigo_pais):
        sql = "SELECT PAIS.nombre FROM PAIS WHERE PAIS.codigo ='"+codigo_pais+"'"
        return Conexion.sqlGetData(sql)

    def obtenerLibreta(self, documento):
        sql = "SELECT LIBRETA_MILITAR.numero, LIBRETA_MILITAR.tipo, LIBRETA_MILITAR.codigo_distrito FROM LIBRETA_MILITAR WHERE LIBRETA_MILITAR.documento ='"+documento+"'"
        return Conexion.sqlGetData(sql)
    def obtenerDistritoMilitar(self, codigo_distrito):
        sql =" SELECT DISTRITO_MILITAR.nombre FROM DISTRITO_MILITAR WHERE DISTRITO_MILITAR.codigo ='"+codigo_distrito+"'"
        return Conexion.sqlGetData(sql)
    def obtenerNacionalidades(self, documento):
        sql = "SELECT PAIS.codigo, PAIS.nombre FROM PAIS WHERE PAIS.codigo = (SELECT NACIONALIDAD.codigo_pais FROM NACIONALIDAD WHERE NACIONALIDAD.documento_persona = '"+documento+"')"
        return Conexion.sqlGetData(sql)

    def obtenerEducacionBasica(self, documento):
        sql = "SELECT EDUCACION_BASICA.titulo, EDUCACION_BASICA.grado, EDUCACION_BASICA.fecha_grado FROM EDUCACION_BASICA WHERE EDUCACION_BASICA.documento ='"+documento+"'"
        return Conexion.sqlGetData(sql)
    def obtenerEducacionSuperior(self, documento):
        sql = "SELECT EDUCACION_SUPERIOR.titulo, EDUCACION_SUPERIOR.modalidad,EDUCACION_SUPERIOR.semestres_aprobados,EDUCACION_SUPERIOR.graduado, EDUCACION_SUPERIOR.fecha_terminacion, EDUCACION_SUPERIOR.tarjeta_profesional FROM EDUCACION_SUPERIOR WHERE EDUCACION_SUPERIOR.documento ='"+documento+"'"
        return Conexion.sqlGetData(sql)
    def guardarEducacionSuperior(self,datos):
        sql = "INSERT INTO EDUCACION_SUPERIOR (titulo, modalidad, semestres_aprobados,graduado,fecha_terminacion,tarjeta_profesional, documento) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        return Conexion.sqlExecute(sql, datos)
    def guardarEducacionBasica(self,datos):
        sql = "INSERT INTO EDUCACION_BASICA(documento,titulo, grado,fecha_grado) VALUES(%s,%s,%s,%s)"
        return Conexion.sqlExecute(sql, datos)
    def actualizarEducacionBasica(self,datos):
        sql = "UPDATE EDUCACION_BASICA SET titulo=%s, grado=%s,fecha_grado=%s where documento=%s"
        return Conexion.sqlExecute(sql, datos)
    def obtenerEmpleos(self, documento):
        sql = "SELECT EMPLEOS.nombre_empresa,EMPLEOS.gubernamental,EMPLEOS.codigo_pais,EMPLEOS.codigo_departamento,EMPLEOS.codigo_municipio,EMPLEOS.correo,EMPLEOS.fecha_ingreso,EMPLEOS.fecha_retiro,EMPLEOS.telefono,EMPLEOS.contrato,EMPLEOS.dependencia,EMPLEOS.direccion,EMPLEOS.documento FROM  EMPLEOS WHERE EMPLEOS.documento ='"+documento+"'"
        return Conexion.sqlGetData(sql)
