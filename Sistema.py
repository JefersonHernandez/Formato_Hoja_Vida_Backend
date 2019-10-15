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

    def guardarInfoLibreta(self,datos):
        print(datos)
        sql = "UPDATE LIBRETA_MILITAR SET numero=%s,tipo=%s,codigo_distrito=%s where numero = %s"
        print('paso')
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

    def guardarInformacion(self, datosPersona, datosLibreta,datosNacionaldiad,datosNacimiento,datosCorrespondencia,documento):
        print('###')
        #self.guardarInfoPersona(datosPersona,documento)
        #self.guardarInfoLibreta(datosLibreta)
        #print(datosNacimiento)
        print(datosPersona)
        print('llego')
        self.guardarInfoNacionalidad(datosNacionaldiad)
        print('llego 2')
        self.guardarInfoNacimiento(datosNacimiento)
        print('llego 3')
        self.guardarInfoCorrespondencia(datosCorrespondencia)
        print('llego 4')
    def crearCuenta(self,datos):
        sql = 'INSERT INTO PERSONA (documento,clave) VALUES (%s,%s)'
        return Conexion.sqlExecute(sql,datos)

    def cargaDatosPersonales(self,documento):
        sql = "SELECT PERSONA.nombre, PERSONA.primer_apellido, PERSONA.segundo_apellido,PERSONA.documento,PERSONA.codigo_tipo_documento,PERSONA.sexo FROM PERSONA WHERE PERSONA.documento = '"+documento+"'"
        return Conexion.sqlGetData(sql)
