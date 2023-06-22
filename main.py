import pygame, sys
from modo import *
from personaje import personaje
from config import *
from plataformas import plataforma
from API.GUI_form_prueba import *

pygame.init()

PANTALLA = pygame.display.set_mode(SIZE_SCREEN)
pygame.display.set_caption("BEN 10")
RELOJ = pygame.time.Clock()

# FONDO ############################################

fondo = pygame.image.load(r"RECURSOS\fondo_ben.jpg")
fondo = pygame.transform.scale(fondo, SIZE_SCREEN)
PANTALLA.blit(fondo, (0,0))

# ICONO  ###############################################################3
icono = pygame.image.load(r"RECURSOS\ben_parado.png")
pygame.display.set_icon(icono)

# MUSICA ############################################################3
#pygame.mixer.music.load("RECURSOS\musica.mp3")
#pygame.mixer.music.play(-1)
#pygame.mixer.music.set_volume(0.1)

# FUENTE ##############################################################
fuente = pygame.font.SysFont("Arial",30)
texto = fuente.render("mi primer juego", False, "black")

# BEN    #################################################################
correr = [
    pygame.image.load(r"RECURSOS\ben_correr.png"),
    pygame.image.load(r"RECURSOS\ben_correr_01.png"),
    pygame.image.load(r"RECURSOS\ben_correr_02.png"),
    pygame.image.load(r"RECURSOS\ben_correr_03.png"),
]
quieto = [
    pygame.image.load(r"RECURSOS\ben_parado.png")
]
saltando = [
    pygame.image.load(r"RECURSOS\ben_saltando.png")
]

lista_acciones = [quieto, correr, saltando]

ben = personaje(PANTALLA,quieto[0], (20,45), 80, 550, 10, -15, lista_acciones)

# PLATAFORMA   ########################################################

piso = plataforma(PANTALLA,r"RECURSOS\37623.png", (WIDTH,75),0,HEIGHT-75)

plataforma_x = plataforma(PANTALLA,r"RECURSOS\37623.png", (400,50),0,260)
plataformas_y = plataforma(PANTALLA,r"RECURSOS\37623.png", (500,50),735,460)
plataformas_a = plataforma(PANTALLA,r"RECURSOS\37623.png", (200,50),425,370)
plataforma_z = plataforma(PANTALLA,r"RECURSOS\37623.png", (600,50),435,150)
plataforma_d = plataforma(PANTALLA,r"RECURSOS\37623.png", (600,52),364,574)

lista_plataformas = [piso, plataforma_x,plataformas_y, plataforma_z,plataforma_d,plataformas_a]

# FORMULARIOS   #########################################################3

form_prueba = FormPrueba(PANTALLA, 150, 150, 900,350,"gold","black", 5, True)

#####################################################
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
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            print(x,y)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit(0)
    elif (keys[pygame.K_UP] or keys[pygame.K_w]  or keys[pygame.K_SPACE]) and (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
        ben.saltar()
        ben.mover_derecha()
    elif (keys[pygame.K_UP] or keys[pygame.K_w]  or keys[pygame.K_SPACE]) and (keys[pygame.K_LEFT] or keys[pygame.K_a]):
        ben.saltar(True)
        ben.mover_izquierda()
    elif keys[pygame.K_UP] or keys[pygame.K_w]  or keys[pygame.K_SPACE]:
        ben.saltar()
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        ben.mover_derecha()
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        ben.mover_izquierda()
    else:
        ben.quieto()

    PANTALLA.blit(fondo, (0,0))

    for platform in lista_plataformas:
        platform.update()
        
    ben.update()
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
        
    form_prueba.update(lista_eventos)
    pygame.display.update()
