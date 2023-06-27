import pygame, sys,time
from modo import *
from personaje import Personaje
from enemigo import Enemigo
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

ben = Personaje(PANTALLA,quieto[0], (20,45), 80, 550, 10, -15, lista_acciones)

# PLATAFORMA   ########################################################

piso = plataforma(PANTALLA,r"RECURSOS\piso_piedra.png", (WIDTH,82),0,HEIGHT-82)

plataforma_a = plataforma(PANTALLA,r"RECURSOS\piso_piedra.png", (300,50),0,260)
plataforma_b = plataforma(PANTALLA,r"RECURSOS\piso_piedra.png", (500,50),900,200)
plataforma_c = plataforma(PANTALLA,r"RECURSOS\piso_piedra.png", (300,50),0,450)
plataforma_d = plataforma(PANTALLA,r"RECURSOS\piso_piedra.png", (500,50),1070,500)
plataforma_e = plataforma(PANTALLA,r"RECURSOS\piso_piedra.png", (600,50),425,380)
plataforma_f = plataforma(PANTALLA,r"RECURSOS\piso_piedra.png", (400,52),364,574)
plataforma_g = plataforma(PANTALLA,r"RECURSOS\piso_piedra.png", (200,50),600,250)
plataforma_h = plataforma(PANTALLA,r"RECURSOS\piso_piedra.png", (75,50),450,200)

lista_plataformas = [piso, plataforma_a,plataforma_b,plataforma_c,plataforma_d,plataforma_e,plataforma_f,plataforma_g,plataforma_h]

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

enemigo = Enemigo(PANTALLA, quieto_00[0],(60,90),900,300,enemigo_00_movimientos,990,430)


# FORMULARIOS   #########################################################3

info1 = pygame.Rect(0,0,WIDTH,75)

form_prueba = FormPrueba(PANTALLA, 150, 150, 900,350,"gold","black", 5, True)

tick = pygame.USEREVENT + 0
pygame.time.set_timer(tick,1000)
cronometro = 0
tiempo = fuente.render(f"00:0{cronometro}", True, "White")

# OMNITRIX 
omni = pygame.image.load("RECURSOS\omnitrix.png")
imagen_omnitrix = [
    omni,
    omni,
    pygame.transform.flip(omni,True,False),
    pygame.transform.flip(omni,True,False)
]
omnitrix_1 = Especial(80,220,PANTALLA,imagen_omnitrix)
omnitrix_2 = Especial(1120,460,PANTALLA,imagen_omnitrix)
omnitrix = [omnitrix_1,omnitrix_2]

# CORAZON
cora = pygame.image.load("RECURSOS\corazon.png")
imagen_corazon = [
    cora,
    cora,
    pygame.transform.flip(cora,True,False),
    pygame.transform.flip(cora,True,False)
]
corazon = Especial(1100,150,PANTALLA,imagen_corazon)
corazones = [corazon]

cronometro_1 = time.time()

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
            print(pygame.mouse.get_pos())

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit(0)
    elif keys[pygame.K_p]:
        ahora = pygame.time.get_ticks()
        if ahora - ben.ultimo_disparo > ben.retrazo_disparo:
            ben.disparar()
            ben.ultimo_disparo = ahora
    elif (keys[pygame.K_UP] or keys[pygame.K_w]  or keys[pygame.K_SPACE]) and (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
        ben.mover_derecha()
        ben.saltar()
    elif (keys[pygame.K_UP] or keys[pygame.K_w]  or keys[pygame.K_SPACE]) and (keys[pygame.K_LEFT] or keys[pygame.K_a]):
        ben.mover_izquierda()
        ben.saltar()
    elif keys[pygame.K_UP] or keys[pygame.K_w]  or keys[pygame.K_SPACE]:
        ben.saltar()
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        ben.mover_derecha()
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        ben.mover_izquierda()
    else:
        ben.quieto()
    
    tiempo_transcurrido = time.time() - cronometro_1
    tiempo = fuente.render(f"00:{int(60-tiempo_transcurrido)}", True, "White")

    PANTALLA.blit(fondo, (0,0))

    for platform in lista_plataformas:
        platform.update()
    
    ben.update(lista_plataformas,enemigo,omnitrix,corazones)
    enemigo.update()

    for x in omnitrix:
        x.update()
    for x in corazones:
        x.update()
    

    if get_mode() == True:
        form_prueba.update(lista_eventos)
        '''
        for x in lista_plataformas:,[ben]:#,enemigo_00],omnitrix:
            pygame.draw.rect(PANTALLA, "black",x.rect,2)
            pygame.draw.rect(PANTALLA, "blue",x.rect ,2)
            pygame.draw.rect(PANTALLA, "red",x.rect_bottom,2)
            pygame.draw.rect(PANTALLA, "black",x.rect_left,2)
            pygame.draw.rect(PANTALLA, "green",x.rect_right,2)
            pygame.draw.rect(PANTALLA, "purple",x.rect_top,2)
        '''
    pygame.draw.rect(PANTALLA, "black",info1 ,100)
    score = fuente.render(f"Score:{ben.puntuacion}", True, "White")
    vidas = fuente.render(f"Vidas:{ben.vidas}", True, "White")
    PANTALLA.blit(tiempo, (500,20))
    PANTALLA.blit(score, (912,20))
    ben.mostrar_vidas()
    #form_prueba.update(lista_eventos)
    pygame.display.update()
