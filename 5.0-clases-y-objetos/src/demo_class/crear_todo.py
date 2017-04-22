from Alumno import Alumno
from Profesor import Profesor
from Materia import Materia
from Clase import Clase

def crearAlumnos():
    return [Alumno(8,"Ricardo", "Fort")]

def crearProfesores():
    return [Profesor("roberto"), Profesor("Carlos")]

def crearMateria():
    return Materia("python101")

def main():
    python101 = Clase(crearAlumnos(), crearProfesores(), crearMateria())
    python101.imprimirAlumnos()

if __name__ == '__main__':
    main()
