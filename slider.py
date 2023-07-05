import pygame
from especiales import Especial

class Slider(Especial):
    def __init__(self,x,y, pantalla, imagen,limite_mayor,limite_menor,orientacion="horizontal") -> None:
        super().__init__(x,y, pantalla, imagen)
        self.posicion = "derecha"
        self.limite_mayor = limite_mayor
        self.limite_menor = limite_menor
        self.orientacion = orientacion
        if self.orientacion == "vertical":
            self.posicion = "arriba"
    
    def escaler_imagen(self):
        self.imagen = pygame.transform.scale(self.imagen,(60,50))   
    
    def animar(self):
        largo = len(self.animacion)
        if self.accion >= largo:
            self.accion = 0
        self.imagen = self.animacion[self.accion]
        self.escaler_imagen()
        self.accion += 1

    def mover(self):
        self.direccion()
        if self.posicion == "derecha":
            self.rect.x += 15
        elif self.posicion == "izquierda":
            self.rect.x -= 15
    
    def direccion(self):
        if self.rect.x >= self.limite_mayor:
            self.posicion = "izquierda"
        elif self.rect.x <= self.limite_menor:
            self.posicion = "derecha"
    
    def mover_vertical(self):
        self.direccion_vertical()
        if self.posicion == "abajo":
            self.rect.y -= 15
        elif self.posicion == "arriba":
            self.rect.y += 15
    
    def direccion_vertical(self):
        if self.rect.y >= self.limite_mayor:
            self.posicion = "abajo"
        elif self.rect.y <= self.limite_menor:
            self.posicion = "arriba"
    
    def update(self,slave):
        if self.activo:
            if self.orientacion == "horizontal":
                self.mover()
            else:
                self.mover_vertical()
            self.animar()
            slave.blit(self.imagen, self.rect)