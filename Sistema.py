from Conexion import Conexion
import psycopg2


class Sistema(object):
    """doc"""

    def guardarInfoCorrespondencia(self, datos):
        sql = "INSERT INTO CORRESPONDENCIA (codigo_persona, direccion, email, telefono,codigo_pais,codigo_departamento,codigo_municipio) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        return Conexion.sqlExecute(sql, datos)

    def getPersona(self, documento):
        sql = "SELECT * FROM PERSONA WHERE DOCUMENTO = " + documento
        datos = Conexion.sqlGetData(sql)
        print(datos)

    def login(self, documento, clave):
        sql = "SELECT clave FROM PERSONA WHERE documento = " + documento
        return Conexion.sqlGetData(sql)

    def obtenerPaises(self):
        sql = "SELECT PAIS.nombre, PAIS.codigo FROM PAIS"
        return Conexion.sqlGetData(sql)

    def guardarInfoPersona(self,datos):
        sql = "INSERT INTO PERSONA (nombre, primer_apellido, segundo_apellido, documento, codigo_tipo_documento, sexo) VALUES(%s,%s,%s,%s,%s,%s)"
        return Conexion.sqlExecute(sql, datos)

    def guardarInfoLibreta(self,datos):
        sql = "INSERT INTO LIBRETA_MILITAR (numero, clase, codigo_distrito) VALUES(%s,%s,%s)"
        return Conexion.sqlExecute(sql, datos)

    def guardarInfoNacionalidad(self,datos):
        sql = "INSERT INTO NACIONALIDAD (codigo_pais, documento_persona) VALUES(%s,%s)"
        return Conexion.sqlExecute(sql, datos)

    def obtenerDistritosMilitares(self):
        sql = "SELECT DISTRITO_MILITAR.nombre FROM DISTRITO_MILITAR"
        return Conexion.sqlGetData(sql)

    def obtenerDepartamentos(self, codigo_pais):
        sql = "SELECT DEPARTAMENTO.nombre, DEPARTAMENTO.codigo_departamento FROM DEPARTAMENTO WHERE DEPARTAMENTO.codigo_pais =  '"+codigo_pais+"'"
        return Conexion.sqlGetData(sql)

    def obtenerMunicipios(self, codigo_departamento):
        sql = "SELECT MUNICIPIO.nombre, MUNICIPIO.codigo_municipio FROM MUNICIPIO WHERE MUNICIPIO.codigo_departamento =  '"+codigo_departamento+"'"
        return Conexion.sqlGetData(sql)

    def guardarInfoNacimiento(self,datos):
        sql = "INSERT INTO LUGAR_NACIMIENTO (documento_persona, codigo_pais, codigo_departamento, codigo_municipio, fecha_nacimiento) VALUES(%s,%s,%s,%s,%s)"
        return Conexion.sqlExecute(sql, datos)
