from Persona import Persona

class Alumno(Persona, object):

    def __init__(self, promedio, *args):
        Persona.__init__(self, *args)
        self.promedio = 8
