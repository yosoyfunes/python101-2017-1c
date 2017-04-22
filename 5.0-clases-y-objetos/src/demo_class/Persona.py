class Persona(object):
    def __init__(self, nombre, apellido=None, *args):
        self.nombre = nombre
        self.apellido =  apellido

    def dame_nombre(self):
        return self.nombre
