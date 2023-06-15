import pygame
from  config import *

class personaje():
    def __init__(self, imagen, size:tuple, x, y, velocidad,potencia_salto) -> None:
        self.imagen = pygame.image.load(imagen)
        self.imagen = pygame.transform.scale(self.imagen,size)
        self.imagen_invertida = pygame.transform.flip(self.imagen, True, False)
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_right = pygame.Rect(self.rect.right -6, self.rect.top, 6, self.rect.height)
        self.rect_left = pygame.Rect(self.rect.left, self.rect.top,6, self.rect.height)
        self.rect_top = pygame.Rect(self.rect.left, self.rect.top, self.rect.width, 6)
        self.rect_bottom = pygame.Rect(self.rect.left, self.rect.bottom -6, self.rect.width, 6)
        self.lado_personaje = [self.rect, self.rect_bottom, self.rect_left, self.rect_right, self.rect_top]
        self.velocidad = velocidad
        self.gravedad = 1
        self.potencia_salto = potencia_salto*-1
        self.esta_saltando = False
        self.desplazamiento_y = 0
        self.limite_velocidad_caida = 15

    def mover_personaje(self, velocidad):
        for lado in range(len(self.lado_personaje)):
            self.lado_personaje[lado].x += velocidad

    def mover_personaje_vertical(self, velocidad):
        for lado in range(len(self.lado_personaje)):
            self.lado_personaje[lado].y += velocidad

    def animar_personaje(self, pantalla, rectangulo):
        largo = len(acciones)
        if contador_pasos >= largo:
            contador_pasos = 0

        pantalla.blit(acciones[contador_pasos],rectangulo)
        contador_pasos += 1

    def mover_derecha(self):
        if self.rect.x < WIDTH-self.rect.width:
            self.mover_personaje(self.velocidad)
        #self.animar_personaje()

    def mover_izquierda(self):
        if self.rect.x > 0:
            self.mover_personaje(self.velocidad*-1)
        #self.animar_personaje()
    
    def quieto(self):
        self.animar_personaje()
    
    def saltar(self):
        if not self.esta_saltando:
            self.esta_saltando = True
            self.desplazamiento_y = self.potencia_salto  

    def aplicar_gravedad(self, plataformas):
        if self.esta_saltando:
            #self.animar_personaje
            self.mover_personaje_vertical(self.desplazamiento_y)
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
        for piso in plataformas:
            if self.rect_bottom.colliderect(piso.rect_top):
                self.rect.bottom = piso.rect.top + 5
                self.esta_saltando = False
                self.desplazamiento_y = 0
                break
            else:
                self.esta_saltando = True
