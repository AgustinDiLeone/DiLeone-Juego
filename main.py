import pygame, random, sys
from modo import *
from personaje import personaje


W,H = 800,600
screen_size = (W,H)
FPS = 20

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(screen_size)
pygame.display.set_caption("BEN 10")

#FONDO ############################################

fondo = pygame.image.load(r"RECURSOS\fondo.png")
fondo = pygame.transform.scale(fondo, screen_size)
PANTALLA.blit(fondo, (0,0))

#ICONO 
icono = pygame.image.load("RECURSOS\ico.png")
pygame.display.set_icon(icono)

#MUSICA
pygame.mixer.music.load("RECURSOS\musica.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

#fuente
fuente = pygame.font.SysFont("Arial",30)
texto = fuente.render("mi primer juego", False, "black")

#homero
ben = personaje("RECURSOS\derecha.png", (100,150), 200,300)

while True:
    RELOJ.tick(FPS)
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit(0)
    elif keys[pygame.K_RIGHT]:
        que_hace = "derecha"
    elif keys[pygame.K_LEFT]:
        que_hace = "izquierda"
    elif keys[pygame.K_UP]:
        que_hace = "saltar"
    else:
        que_hace = "quieto"

    if get_mode() == True:
        pygame.draw.rect(PANTALLA, "blue",ben.rect ,2)
        pygame.draw.rect(PANTALLA, "red",ben.rect_botton,2)
        pygame.draw.rect(PANTALLA, "black",ben.rect_left,2)
        pygame.draw.rect(PANTALLA, "green",ben.rect_right,2)
        pygame.draw.rect(PANTALLA, "purple",ben.rect_top,2)

    pygame.display.update()
