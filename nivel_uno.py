import pygame
from pygame.locals import *
from nivel import *
from config import *


class NivelUno(Nivel):
    def __init__(self, pantalla) -> None:
        # FONDO ############################################
        img_fondo = pygame.image.load(r"RECURSOS\fondo_0.jpg")
        img_fondo = pygame.transform.scale(img_fondo, SIZE_SCREEN)

        # ICONO  ###############################################################3
        icono = pygame.image.load(r"RECURSOS\ben_parado.png")
        pygame.display.set_icon(icono)

        # MUSICA ############################################################3
        #pygame.mixer.music.load("RECURSOS\musica.mp3")
        #pygame.mixer.music.play(-1)
        #pygame.mixer.music.set_volume(0.1)

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

        personaje_principal = Personaje(pantalla,quieto[0], (20,45), 80, 550, 10, -15, lista_acciones)

        # PLATAFORMA   ########################################################

        piso = plataforma(pantalla,r"RECURSOS\piso_pasto.png", (WIDTH,82),0,HEIGHT-82)

        plataforma_a = plataforma(pantalla,r"RECURSOS\piso_pasto.png", (300,50),0,260)
        plataforma_b = plataforma(pantalla,r"RECURSOS\piso_pasto.png", (500,50),900,200)
        plataforma_c = plataforma(pantalla,r"RECURSOS\piso_pasto.png", (300,50),0,450)
        plataforma_d = plataforma(pantalla,r"RECURSOS\piso_pasto.png", (500,50),1070,500)
        plataforma_e = plataforma(pantalla,r"RECURSOS\piso_pasto.png", (600,50),425,380)
        plataforma_f = plataforma(pantalla,r"RECURSOS\piso_pasto.png", (400,52),364,574)
        plataforma_g = plataforma(pantalla,r"RECURSOS\piso_pasto.png", (200,50),600,250)
        plataforma_h = plataforma(pantalla,r"RECURSOS\piso_pasto.png", (75,50),450,200)

        lista_plataformas = [piso, plataforma_a,plataforma_b,plataforma_c,plataforma_d,plataforma_e,plataforma_f,plataforma_g,plataforma_h]

        # ENEMIGOS #############################################################

        correr_00 = [
            pygame.image.load(r"RECURSOS\enemigo_20.png"),
            pygame.image.load(r"RECURSOS\enemigo_21.png")
        ]
        quieto_00 = [
            pygame.image.load(r"RECURSOS\enemigo_20.png")
        ]
        enemigo_00_movimientos = [quieto_00,correr_00]

        enemigo = Enemigo(pantalla, quieto_00[0],(60,90),900,300,enemigo_00_movimientos,990,430)
        enemigo_2 = Enemigo(pantalla, quieto_00[0],(60,90),100,180,enemigo_00_movimientos,240,0)
        enemigo_3 = Enemigo(pantalla, quieto_00[0],(60,90),1000,125,enemigo_00_movimientos,1140,900)
        enemigos = [enemigo,enemigo_2,enemigo_3]
        # OMNITRIX 
        omni = pygame.image.load("RECURSOS\omnitrix.png")
        imagen_omnitrix = [
            omni,
            omni,
            pygame.transform.flip(omni,True,False),
            pygame.transform.flip(omni,True,False)
        ]
        omnitrix_1 = Especial(470,150,pantalla,imagen_omnitrix)
        omnitrix_2 = Especial(1120,460,pantalla,imagen_omnitrix)
        omnitrix = [omnitrix_1,omnitrix_2]

        # CORAZON
        cora = pygame.image.load("RECURSOS\corazon.png")
        imagen_corazon = [
            cora,
            cora,
            pygame.transform.flip(cora,True,False),
            pygame.transform.flip(cora,True,False)
        ]
        corazon = Especial(1100,150,pantalla,imagen_corazon)
        corazon_1 = Especial(50,400,pantalla,imagen_corazon)
        corazones = [corazon,corazon_1]
        # Sierra 
        sierra = []
        # Veneno 
        veneno = []
        
        super().__init__(pantalla, personaje_principal, lista_plataformas, img_fondo, enemigos, omnitrix, corazones,sierra,veneno)