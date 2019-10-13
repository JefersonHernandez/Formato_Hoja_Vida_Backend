import psycopg2
from config import config


class Conexion:
    """clase que funciona como objeto para la conexion con la base de datos"""

    conexion = None

    @staticmethod
    def abrirConexion():
        try:
            print("abriendo conexion.")
            # lectura de los parametros de conexion
            params = config()
            # conexion al servidor de postgresql
            Conexion.conexion = psycopg2.connect(**params)
            # creacion del cursor
            cur = Conexion.conexion.cursor()
            print("conexion abierta.")
            return cur
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    @staticmethod
    def cerrarConexion():
        print("cerrando conexion.")
        # Cierre de la comunicación con PostgreSQL
        Conexion.conexion.close()
        print("conexion cerrada.")

    @staticmethod
    def commit():
        """perform the script commit to postgres"""
        estado = Conexion.conexion.commit()
        print(estado, '#######ESTADO')

    @staticmethod
    def sqlExecute(sql, datos):
        """retorna False si la operacion no se completed"""
        try:
            cur = Conexion.abrirConexion()
            cur.execute(sql, datos)
            print(datos)
            estado=Conexion.commit()
            print(estado)
            print('##@##')
            return 'Guardado.'
        except psycopg2.errors.ForeignKeyViolation as e:
            print('ForeignKeyViolation')
            return 'ForeignKeyViolation'
        except psycopg2.errors.UniqueViolation as e:
            print('UniqueViolation')
            return 'UniqueViolation'
        except psycopg2.Error as e:
            print(e+'error desconocido')
            return e
        finally:
            Conexion.cerrarConexion()

    @staticmethod
    def sqlGetData(sql):
        try:
            conn = Conexion.abrirConexion()
            conn.execute(sql)
            return conn.fetchall()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            Conexion.cerrarConexion()
