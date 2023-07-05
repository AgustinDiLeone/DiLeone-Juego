import pygame, sys,time
from modo import *
from config import *
from personaje import Personaje
from enemigo import Enemigo
from especiales import Especial
from plataformas import plataforma
from SQL.sql import traer_id_ultimo, ultimo_puntaje,actualizar_puntos


class Nivel():
    def __init__(self,pantalla,personaje_principal,lista_plataformas,imagen_fondo,enemigo,omnitrix,corazones,sierra,veneno) -> None:
        self.slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.img_fondo = imagen_fondo
        self.enemigo = enemigo
        self.omnitrix = omnitrix
        self.corazones = corazones
        self.sierra = sierra
        self.veneno = veneno
        self.comienzo = time.time()
        self.tiempo_transcurrido = 0
        self.flag_puntos_tiempo = True

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
            try:
                platform.update(self.slave)
            except:
                print("Error en la actualizacion de las plataformas")
        
        try:
            self.jugador.update(self.slave,self.plataformas,self.enemigo,self.omnitrix,self.corazones,self.sierra,self.veneno)
        except:
            print("Error en la actualizacion del personaje")
        
        for x in self.enemigo:
            try:
                x.update(self.slave)
            except:
                print("Error en la actualizacion del enemigo")
        
        for x in self.omnitrix:
            try:
                x.update(self.slave)
            except:
                print("Error en la actualizacion del omnitrix")
    
        for x in self.corazones:
            try:
                x.update(self.slave)
            except:
                print("Error en la actualizacion de los corazones")

        for x in self.veneno:
            try:
                x.update(self.slave)
            except:
                print("Error en la actualizacion del veneno")
        
        for x in self.sierra:
            try:
                x.update(self.slave)
            except:
                print("Error en la actualizacion de la sierra")
        # FUENTE ##############################################################
        fuente = pygame.font.SysFont("Arco Font",70)
        # FORMULARIOS   #########################################################
        info1 = pygame.Rect(0,0,WIDTH,75)
        pygame.draw.rect(self.slave, "black",info1 ,100)

        self.tiempo_transcurrido = time.time() - self.comienzo
        if self.tiempo_transcurrido >= 60:
            self.jugador.esta_vivo = False
            self.jugador.vidas = 0
        else:
            if self.tiempo_transcurrido > 50:
                tiempo = fuente.render(f"00:0{int(60-self.tiempo_transcurrido)}", True, "White")
            else:
                tiempo = fuente.render(f"00:{int(60-self.tiempo_transcurrido)}", True, "White")
            try:
                self.slave.blit(tiempo, (500,20))
            except:
                print("Error en la actualizacion del tiempo")
        score = fuente.render(f"Score:{self.jugador.puntuacion}", True, "White")
        try:
            self.slave.blit(score, (912,20))
        except:
            print("Error en la actualizacion del puntaje")
        try:
            self.jugador.mostrar_vidas(self.slave)
        except:
            print("Error en la actualizacion de las vidas")

    def update(self,lista_eventos):
        if self.jugador.gano:
            win = pygame.image.load(r"RECURSOS\fondo_gano.png")
            win = pygame.transform.scale(win,(WIDTH,HEIGHT))
            self.slave.blit(win, (0,0))
            tiempo_restante = 60 - int(self.tiempo_transcurrido)
            if self.flag_puntos_tiempo:
                # SUMAR Y ACTUALIZAR PUNTOS ####################
                ultimo_id = traer_id_ultimo()
                ultimo_puntos = ultimo_puntaje(ultimo_id)
                puntos = tiempo_restante * 100
                puntaje = ultimo_puntos + puntos
                actualizar_puntos(puntaje,ultimo_id)
                self.flag_puntos_tiempo = False
                self.puntos_obtenidos_tiempo = puntos
            # FUENTE ##############################################################
            fuente = pygame.font.SysFont("Arco Font",70)
            # FORMULARIOS   #########################################################
            info1 = pygame.Rect(0,0,350,75)
            pygame.draw.rect(self.slave, "black",info1 ,100)
            puntos = fuente.render(f"+{self.puntos_obtenidos_tiempo} score", True, "White")
            self.slave.blit(puntos,(50,20))
            
        else:
            if self.jugador.esta_vivo:
                self.leer_inputs()
                self.leer_eventos(lista_eventos)
                self.actualizar_pantalla()
                self.dibujar_rectangulos()
            else:
                lose = pygame.image.load(r"RECURSOS\fondo_lose.png")
                lose = pygame.transform.scale(lose,(WIDTH,HEIGHT))
                self.slave.blit(lose, (0,0))

