import pygame, sys
from modo import *
from personaje import personaje
from enemigo import enemigo
from especiales import Especial
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
fuente = pygame.font.SysFont("Arco Font",70)

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

piso = plataforma(PANTALLA,r"RECURSOS\piso_piedra.png", (WIDTH,82),0,HEIGHT-82)

plataforma_x = plataforma(PANTALLA,r"RECURSOS\piso_piedra.png", (400,50),0,260)
plataformas_y = plataforma(PANTALLA,r"RECURSOS\piso_piedra.png", (500,50),735,460)
plataformas_a = plataforma(PANTALLA,r"RECURSOS\piso_piedra.png", (200,50),425,370)
plataforma_z = plataforma(PANTALLA,r"RECURSOS\piso_piedra.png", (600,50),435,150)
plataforma_d = plataforma(PANTALLA,r"RECURSOS\piso_piedra.png", (600,52),364,574)

lista_plataformas = [piso, plataforma_x,plataformas_y, plataforma_z,plataforma_d,plataformas_a]

# ENEMIGOS #############################################################

correr_00 = [
    pygame.image.load(r"RECURSOS\enemigo_01.png"),
    pygame.image.load(r"RECURSOS\enemigo_02.png"),
    pygame.image.load(r"RECURSOS\enemigo_03.png"),
    pygame.image.load(r"RECURSOS\enemigo_04.png"),
]
quieto_00 = [
    pygame.image.load(r"RECURSOS\enemigo_00.png")
]
enemigo_00_movimientos = [quieto_00,correr_00]

enemigo_00 = enemigo(PANTALLA, quieto_00[0],(60,90),900,300,enemigo_00_movimientos,1000,430)


# FORMULARIOS   #########################################################3

info1 = pygame.Rect(0,0,WIDTH,100)

#form_prueba = FormPrueba(PANTALLA, 150, 150, 900,350,"gold","black", 5, True)
tick = pygame.USEREVENT + 0
pygame.time.set_timer(tick,1000)
disparo_enemigo = pygame.USEREVENT + 1
pygame.time.set_timer(disparo_enemigo,1500)
cronometro = 0
tiempo = fuente.render(f"00:0{cronometro}", True, "White")

# omnitrix 
omni = pygame.image.load("RECURSOS\omnitrix.png")
imagen_omnitrix = [
    omni,
    pygame.transform.flip(omni,True,False)
]
omnitrix = Especial(500,320,PANTALLA,imagen_omnitrix)

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
            if evento.key == pygame.K_DELETE:
                #form_prueba.update(lista_eventos)
                pass
            if evento.key == pygame.K_p:
                ben.disparar()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            
        if evento.type == tick:
            if cronometro == 60:
                cronometro = 0
                tiempo = fuente.render(f"00:0{cronometro}", True, "White")
            else:
                cronometro += 1
                if cronometro < 10:
                    tiempo = fuente.render(f"00:0{cronometro}", True, "White")
                else:
                    tiempo = fuente.render(f"00:{cronometro}", True, "White")
        if evento.type == disparo_enemigo:
            enemigo_00.disparar()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit(0)
    #elif keys[pygame.K_p]:
        #ben.disparar()
    elif (keys[pygame.K_UP] or keys[pygame.K_w]  or keys[pygame.K_SPACE]) and (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
        ben.saltar()
        ben.mover_derecha()
    elif (keys[pygame.K_UP] or keys[pygame.K_w]  or keys[pygame.K_SPACE]) and (keys[pygame.K_LEFT] or keys[pygame.K_a]):
        ben.saltar()
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
    
    ben.update(lista_plataformas,enemigo_00,omnitrix)
    enemigo_00.update(ben)
    omnitrix.update()
    

    if get_mode() == True:
        pygame.draw.rect(PANTALLA, "black",omnitrix.rect ,2)
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
        
    pygame.draw.rect(PANTALLA, "black",info1 ,100)
    score = fuente.render(f"Score:{ben.puntuacion}", True, "White")
    PANTALLA.blit(tiempo, (530,35))
    PANTALLA.blit(score, (912,35))
    #form_prueba.update(lista_eventos)
    pygame.display.update()
