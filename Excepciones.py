class UniqueViolation(Exception):
    """docstring for ."""

    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return repr(self.valor)

class UsuarioInvalido(Exception):

    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return repr(self.valor)

class UsuarioNoExiste(Exception):

    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return repr(self.valor)