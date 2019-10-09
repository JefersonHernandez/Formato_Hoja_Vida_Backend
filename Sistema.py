from Conexion import Conexion
import psycopg2


class Sistema(object):
    """doc"""

    def guardadCorrespondencia(self, datos):
        sql = "INSERT INTO CORRESPONDENCIA (id_correspondencia, direccion, email) VALUES (%s,%s,%s)"
        return Conexion.sqlExecute(sql, datos)

    def guardarPais(self,datos):
        sql = "INSERT INTO PAIS (codigo, nombre) VALUES (%s, %s)"
        aux = Conexion.sqlExecute(sql, datos)
        print('aux content => ', aux)

    def guardarPersona(self, datos):
        sql = "INSERT INTO PERSONA (nombre, primer_apellido, segundo_apellido, fecha_nacimiento, " \
              "documento, id_tipo_doc, id_pais, id_correspondenc, id_edu_basica, habilitado) " \
              "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        Conexion.sqlExecute(sql, datos)

    def getPersona(self, documento):
        sql = "SELECT * FROM PERSONA WHERE DOCUMENTO = " + documento
        datos = Conexion.sqlGetData(sql)
        print(datos)

    def login(self, documento, clave):
        sql = "SELECT clave FROM PERSONA WHERE documento = " + documento
        return Conexion.sqlGetData(sql)

    def guardarDatosPersonales(self, datos):
        sql = "INSERT INTO PERSONA (nombre, primer_apellido, segundo_apellido, fecha_nacimiento, " \
              "documento, id_tipo_doc, id_pais,id_edu_basica, habilitado, clave) " \
              "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        return Conexion.sqlExecute(sql, datos)

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
