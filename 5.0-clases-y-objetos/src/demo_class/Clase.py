class Clase:
    def __init__(self, alumnos, profesores, materia):
        self.alumnos = alumnos
        self.profesores = profesores
        self.materia = materia

    def imprimirAlumnos(self):
        for alumno in self.alumnos:
            print(alumno.dame_nombre())
