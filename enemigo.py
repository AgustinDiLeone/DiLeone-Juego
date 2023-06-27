from personaje import personaje
from config import *

class enemigo(personaje):
    def __init__(self, pantalla, imagen, size: tuple, x, y,acciones,limite_mayor, limite_menor) -> None:
        super().__init__(pantalla, imagen, size, x, y, 10, 0, acciones)
        self.limite_mayor = limite_mayor
        self.limite_menor = limite_menor

    def direccion(self):
        if self.rect.x >= self.limite_mayor:
            self.posicion = "izquierda"
        elif self.rect.x <= self.limite_menor:
            self.posicion = "derecha"
    
    def mover(self):
        if self.esta_vivo:
            self.direccion()
            if self.posicion == "derecha":
                super().mover_derecha()
            elif self.posicion == "izquierda":
                super().mover_izquierda()
    
    def collision(self,personaje):
        for x in personaje.lista_proyectiles:
            if x.disparo_rect.colliderect(self.rect):
                self.esta_vivo = False
                personaje.lista_proyectiles.remove(x)

    def update(self):
        if self.esta_vivo == True:
            self.mover()
            self.pantalla.blit(self.imagen, self.rect)
            for x in self.lista_proyectiles:
                x.trayectoria()
                x.update()
                if x.disparo_rect.left == WIDTH or 0:
                    self.lista_proyectiles.remove(x)
        else:
            self.rect = None


