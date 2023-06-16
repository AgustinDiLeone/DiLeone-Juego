import pygame, sys
from modo import *
from personaje import personaje
from config import *
from plataformas import plataforma


pygame.init()

PANTALLA = pygame.display.set_mode(SIZE_SCREEN)
pygame.display.set_caption("BEN 10")
RELOJ = pygame.time.Clock()

#FONDO ############################################

fondo = pygame.image.load(r"RECURSOS\fondo.png")
fondo = pygame.transform.scale(fondo, SIZE_SCREEN)
PANTALLA.blit(fondo, (0,0))

#ICONO  ###############################################################3
icono = pygame.image.load("RECURSOS\ico.png")
pygame.display.set_icon(icono)

#MUSICA ############################################################3
pygame.mixer.music.load("RECURSOS\musica.mp3")
#pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

#fuente ##############################################################
fuente = pygame.font.SysFont("Arial",30)
texto = fuente.render("mi primer juego", False, "black")

#ben #################################################################
correr = [
    pygame.image.load("RECURSOS/derecha.png"),
    pygame.image.load("RECURSOS/izquierda.png")
]
quieto = [pygame.image.load("RECURSOS/derecha.png")]

lista_acciones = [quieto, correr]

ben = personaje("RECURSOS\1.png", (100,150), 200, 300, 10, 15, lista_acciones,PANTALLA)

#PLATAFORMA ########################################################3
piso = plataforma("RECURSOS\images.jpg", (WIDTH,200),0,HEIGHT-200)

plataformas = plataforma("RECURSOS\images.jpg", (100,50),200,350)
plataforma_x = plataforma("RECURSOS\images.jpg", (70,50),500,420)


lista_plataformas = [piso, plataformas,plataforma_x]

pygame.draw.rect(PANTALLA, "brown",plataformas.rect ,2)
pygame.draw.rect(PANTALLA, "grey",piso.rect ,2)



#####################################################33
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
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        ben.mover_derecha()
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        ben.mover_izquierda()
    elif keys[pygame.K_UP] or keys[pygame.K_w]  or keys[pygame.K_SPACE]:
        ben.saltar()
    else:
        ben.quieto()

    
    PANTALLA.blit(fondo, (0,0))
    PANTALLA.blit(ben.imagen, ben.rect)
    for x in lista_plataformas:
        PANTALLA.blit(x.imagen, x.rect)
    
    
    ben.aplicar_gravedad(lista_plataformas)

    if get_mode() == True:
        pygame.draw.rect(PANTALLA, "blue",ben.rect ,2)
        pygame.draw.rect(PANTALLA, "red",ben.rect_bottom,2)
        pygame.draw.rect(PANTALLA, "black",ben.rect_left,2)
        pygame.draw.rect(PANTALLA, "green",ben.rect_right,2)
        pygame.draw.rect(PANTALLA, "purple",ben.rect_top,2)
        for x in lista_plataformas:
            pygame.draw.rect(PANTALLA, "black",x.rect,2)
            pygame.draw.rect(PANTALLA, "blue",x.rect ,2)
            pygame.draw.rect(PANTALLA, "red",x.rect_bottom,2)
            pygame.draw.rect(PANTALLA, "black",x.rect_left,2)
            pygame.draw.rect(PANTALLA, "green",x.rect_right,2)
            pygame.draw.rect(PANTALLA, "purple",x.rect_top,2)
        
    pygame.display.update()
