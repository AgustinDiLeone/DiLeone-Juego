import pygame, sys,time
from modo import *
from config import *
from personaje import Personaje
from enemigo import Enemigo
from especiales import Especial

from plataformas import plataforma
#from API.GUI_form_prueba import *

class Nivel():
    def __init__(self,pantalla,personaje_principal,lista_plataformas,imagen_fondo,enemigo,omnitrix,corazones) -> None:
        self.slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.img_fondo = imagen_fondo
        self.enemigo = enemigo
        self.omnitrix = omnitrix
        self.corazones = corazones
        self.comienzo = time.time()
        

    def leer_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit(0)
        elif (keys[pygame.K_UP] or keys[pygame.K_w]  or keys[pygame.K_SPACE]) and (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            self.jugador.mover_derecha()
            self.jugador.saltar()
        elif (keys[pygame.K_UP] or keys[pygame.K_w]  or keys[pygame.K_SPACE]) and (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            self.jugador.mover_izquierda()
            self.jugador.saltar()
        elif keys[pygame.K_UP] or keys[pygame.K_w]  or keys[pygame.K_SPACE]:
            self.jugador.saltar()
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.jugador.mover_derecha()
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.jugador.mover_izquierda()
        else:
            self.jugador.quieto()
        if keys[pygame.K_p]:
            ahora = pygame.time.get_ticks()
            if ahora - self.jugador.ultimo_disparo > self.jugador.retrazo_disparo:
                self.jugador.disparar(self.slave)
                self.jugador.ultimo_disparo = ahora
    
    def leer_eventos(self,lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

    def dibujar_rectangulos(self):
        if get_mode() == True:
            for plataforma in self.plataformas:
                for x in plataforma.rectangulos:
                    pygame.draw.rect(self.slave, "green",x,2)
            for lado in self.jugador.lado_personaje:
                pygame.draw.rect(self.slave, "green",lado,2)

    def actualizar_pantalla(self):
        self.slave.blit(self.img_fondo, (0,0))

        for platform in self.plataformas: 
            platform.update(self.slave)

        self.jugador.update(self.slave,self.plataformas,self.enemigo,self.omnitrix,self.corazones)

        self.enemigo.update(self.slave)

        for x in self.omnitrix:
            x.update(self.slave)
    
        for x in self.corazones:
            x.update(self.slave)
        # FUENTE ##############################################################
        fuente = pygame.font.SysFont("Arco Font",70)
        # FORMULARIOS   #########################################################3
        info1 = pygame.Rect(0,0,WIDTH,75)
        pygame.draw.rect(self.slave, "black",info1 ,100)

        tiempo_transcurrido = time.time() - self.comienzo
        tiempo = fuente.render(f"00:{int(60-tiempo_transcurrido)}", True, "White")
        
        score = fuente.render(f"Score:{self.jugador.puntuacion}", True, "White")
        self.slave.blit(tiempo, (500,20))
        self.slave.blit(score, (912,20))
        self.jugador.mostrar_vidas(self.slave)

    def update(self,lista_eventos):
        if self.jugador.gano:
            fuente = pygame.font.SysFont("Arco Font",70)
            info1 = pygame.Rect(380,250,500,200)
            pygame.draw.rect(self.slave, "red",info1 ,100)            
            win = fuente.render(f"Has ganado :)", True, "black")
            self.slave.blit(win, (470,320))
        else:
            if self.jugador.esta_vivo:
                self.leer_inputs()
                self.leer_eventos(lista_eventos)
                self.actualizar_pantalla()
                self.dibujar_rectangulos()
            else:
                fuente = pygame.font.SysFont("Arco Font",70)
                info1 = pygame.Rect(380,250,500,200)
                pygame.draw.rect(self.slave, "red",info1 ,100)            
                lose = fuente.render(f"Has perdido :(", True, "black")
                self.slave.blit(lose, (470,320))

