class Auto:
    def __init__(self, color="Blanco"):
        self.color = color
        self.velMaxima = 100
    def dameColor(self):
        return self.color

a = Auto()
ferrari = Auto("Rojo")
a.dameColor()
ferrari.dameColor()

ferrari.velMaxima
ferrari.velMaxima = 400


ferrari.tieneParlantes = True
a.tieneLucesDeNeon = True
