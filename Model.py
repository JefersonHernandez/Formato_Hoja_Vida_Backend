import datetime
import psycopg2
class Persona(object):

    def __init__(self, nombre, primer_apellido, segundo_apellido, fecha_nacimiento, habilitado,
        documento, id_tipo_doc, id_pais, id_correspondenc, id_edu_basica):
        self.nombre = nombre
        self.primerApellido = primer_apellido
        self.segundoApellido = segundo_apellido
        self.fechaNacimiento = fecha_nacimiento
        self.esHabil = habilitado
        self.documento = documento
        self.tipoDocumento = id_tipo_doc
        self.pais = id_pais
        self.correspondencia = id_correspondenc
        self.educacionBasica = id_edu_basica



class PersonaDao(object):

    def __init__(self):
        pass

    def saveData(self, persona):
        #guarda los datos de la persona en la base de datos
        cur = Conexion.abrirConexion()
        #2 cedula
        #sql script
        sql = """INSERT INTO PERSONA (nombre, primer_apellido, segundo_apellido, fecha_nacimiento, habilitado,
        documento, id_tipo_doc, id_pais, id_correspondenc, id_edu_basica) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)"""

        datos = (persona.nombre, persona.primerApellido, persona.segundoApellido, persona.fechaNacimiento,
        persona.esHabil, persona.documento, persona.tipoDocumento, persona.pais, persona.correspondencia,
        persona.educacionBasica)
        try:
            res = Conexion.conexion.cur.execute(sql, datos)
            print(res.fecthone())
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            Conexion.cerrarConexion()
        #sav
class usuario_estatico(object):
    """docstring for usuario_estatico."""
    usuario = 'None'
    
    @staticmethod
    def getUser():
        usuario_estatico.usuario

    def setUser(user):
        usuario_estatico.usuario=user
