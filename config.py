from configparser import ConfigParser


def config(archivo='db.ini', seccion='postgresql'):
    # crea el parcer y lee el archivo
    parser = ConfigParser()
    parser.read(archivo)

    # obtener la seccion de conexion a la base de datos
    data_base = {}
    if parser.has_section(seccion):
        params = parser.items(seccion)
        for param in params:
            data_base[param[0]] = param[1]
        return data_base
    else:
        raise Exception('Secccion {0} no encontrada en el archivo {1}'.format(seccion, archivo))
