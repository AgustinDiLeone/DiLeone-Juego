import pygame
from  config import *
from disparo import Disparo
#from main import *

class Personaje(pygame.sprite.Sprite):
    def __init__(self,pantalla, imagen, size:tuple, x, y, velocidad,potencia_salto, acciones, disparo=True) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.pantalla = pantalla
        self.imagen = imagen
        self.rect = self.imagen.get_rect()
        self.width = size[0]
        self.height = size[1]
        self.master_x = x
        self.master_y = y
        self.rect.x = self.master_x
        self.rect.y = self.master_y
        self.posicion = "derecha"
        self.velocidad = velocidad
        self.gravedad = 1
        self.potencia_salto = potencia_salto
        self.esta_saltando = False
        self.esta_en_piso = True
        self.choque_derecha = False
        self.choque_izquierda = False
        self.desplazamiento_y = 0
        self.limite_velocidad_caida = 15
        self.contador_pasos = 0
        self.acciones = acciones
        self.esta_vivo = True
        self.puntuacion = 0
        self.vidas = 3
        self.corazon = pygame.transform.scale(pygame.image.load("RECURSOS\corazon.png"),(50,40))
        self.lista_proyectiles = []
        self.path_disparo = disparo
        self.retrazo_disparo = 1000
        self.ultimo_disparo = pygame.time.get_ticks()

        self.crear_rectangulos()

    def crear_rectangulos(self):
        self.rect_right = pygame.Rect(self.rect.right -6, self.rect.top, 6, self.rect.height)
        self.rect_left = pygame.Rect(self.rect.left, self.rect.top,6, self.rect.height)
        self.rect_top = pygame.Rect(self.rect.left, self.rect.top, self.rect.width, 6)
        self.rect_bottom = pygame.Rect(self.rect.left, self.rect.bottom -6, self.rect.width, 6)
        self.lado_personaje = [self.rect, self.rect_bottom, self.rect_left, self.rect_right, self.rect_top]


    def reescalar_imagenes(self,lista,W,H):
        for list in lista:
            for i in range(len(list)):
                list[i] = pygame.transform.scale(list[i],(self.width, self.height))
    
    def girar_imagen(self):
        self.imagen = pygame.transform.flip(self.imagen, True, False)

    def mover_personaje(self, velocidad):
        for lado in range(len(self.lado_personaje)):
            self.lado_personaje[lado].x += velocidad

    def mover_personaje_vertical(self, velocidad):
        for lado in range(len(self.lado_personaje)):
            self.lado_personaje[lado].y += velocidad

    def animar_personaje(self, acciones):
        largo = len(acciones)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        self.imagen = acciones[self.contador_pasos]
        self.contador_pasos += 1

    def mover_derecha(self):
        self.posicion = "derecha"
        if self.rect.x < WIDTH-self.rect.width:
            self.mover_personaje(self.velocidad)
            if not self.esta_saltando:
                self.animar_personaje(self.acciones[1])

    def mover_izquierda(self):
        self.posicion = "izquierda"
        if self.rect.x > 0:
            self.mover_personaje(self.velocidad*-1)
            if not self.esta_saltando:
                self.animar_personaje(self.acciones[1])
                self.girar_imagen()

    def quieto(self):
        if not self.esta_saltando:
            if self.posicion == "derecha":
                self.animar_personaje(self.acciones[0])
            else:
                self.animar_personaje(self.acciones[0])
                self.girar_imagen()

    def saltar(self):
        if not self.esta_saltando:
            self.esta_saltando = True
            self.desplazamiento_y = self.potencia_salto 
            self.animar_personaje(self.acciones[2])
            if self.posicion == "izquierda":
                self.girar_imagen()

    def aplicar_gravedad(self, plataformas):
        if self.esta_saltando:
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
    
    def disparar(self):
        bala = Disparo(self.rect.x,self.rect.y,self.pantalla,r"RECURSOS\bola de fuego.png", self.posicion)
        self.lista_proyectiles.append(bala)

    def collision(self,personaje,omnitrix,corazones):
        if personaje.esta_vivo:
            if self.rect_bottom.colliderect(personaje.rect_top):
                personaje.esta_vivo = False
                self.puntuacion += 200
            elif self.rect.colliderect(personaje.rect):
                self.vidas -= 1
                self.muerte()
            for x in personaje.lista_proyectiles:
                if x.disparo_rect.colliderect(self.rect):
                    self.vidas -= 1
                    self.muerte()
                    x.disparo_activo = False
            for x in self.lista_proyectiles:
                if x.disparo_rect.colliderect(personaje.rect):
                    x.disparo_activo = False
                    personaje.esta_vivo = False
                    self.puntuacion += 100
        for x in omnitrix:
            if x.activo and self.rect.colliderect(x.rect):
                x.activo = False
                self.puntuacion += 100
        for x in corazones:
            if x.activo and self.rect.colliderect(x.rect):
                x.activo = False
                self.puntuacion += 50
                self.vidas += 1
    
    def muerte(self):
        self.rect.x = self.master_x
        self.rect.y = self.master_y
        self.crear_rectangulos()
        self.posicion = "derecha"

    def mostrar_vidas(self):
        if self.vidas >= 1:
            self.pantalla.blit(self.corazon,(100,20))
        if self.vidas >=2:
            self.pantalla.blit(self.corazon,(150,20))
        if self.vidas >=3:
            self.pantalla.blit(self.corazon,(200,20))

    def update(self,lista_plataformas,enemigo,omnitrix,corazones):
        if self.vidas == 0:
            self.esta_vivo == False
        else:
            self.pantalla.blit(self.imagen, self.rect)
            self.aplicar_gravedad(lista_plataformas)
            self.collision(enemigo,omnitrix,corazones)
            for x in self.lista_proyectiles:
                x.trayectoria()
                x.update()
                if x.disparo_rect.left == WIDTH:
                    self.lista_proyectiles.remove(x)



