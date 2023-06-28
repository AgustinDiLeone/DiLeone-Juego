import pygame
from nivel_uno import NivelUno
from nivel_dos import NivelDos
#from nivel_dos import *

class Manejador_niveles:
    def __init__(self,pantalla) -> None:
        self.slave = pantalla
        self.niveles = {"nivel_uno":NivelUno, "nivel_dos": NivelDos}

    def get_niveles(self,nombre_nivel):
        return self.niveles[nombre_nivel](self.slave)