import pygame
from pygame.locals import *
from nivel import *
from config import *
from slider import *


class NivelTres(Nivel):
    def __init__(self, pantalla) -> None:
        self.pantalla = pantalla
        # FONDO ############################################
        img_fondo = pygame.image.load(r"RECURSOS\fondo_3.jpg")
        img_fondo = pygame.transform.scale(img_fondo, SIZE_SCREEN)

        # ICONO  ###############################################################3
        icono = pygame.image.load(r"RECURSOS\ben_parado.png")
        pygame.display.set_icon(icono)

        
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

        piso = plataforma(pantalla,r"RECURSOS\piso_tierra.png", (WIDTH,82),0,HEIGHT-82)

        plataforma_a = plataforma(pantalla,r"RECURSOS\piso_tierra.png", (300,50),0,500)
        plataforma_b = plataforma(pantalla,r"RECURSOS\piso_tierra.png", (500,50),315,380)
        plataforma_c = plataforma(pantalla,r"RECURSOS\piso_tierra.png", (200,50),0,280)
        plataforma_d = plataforma(pantalla,r"RECURSOS\piso_tierra.png", (500,50),370,200)
        plataforma_e = plataforma(pantalla,r"RECURSOS\piso_tierra.png", (720,50),900,300)
        plataforma_f = plataforma(pantalla,r"RECURSOS\piso_tierra.png", (720,50),830,540)

        lista_plataformas = [piso, plataforma_a,plataforma_b,plataforma_c,plataforma_d,plataforma_e,plataforma_f]

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

        enemigo = Enemigo(pantalla, quieto_00[0],(60,90),480,300,enemigo_00_movimientos,770,315,5)

        enemigos = [enemigo]
        
        # OMNITRIX 
        omni = pygame.image.load("RECURSOS\omnitrix.png")
        imagen_omnitrix = [
            omni,
            omni,
            pygame.transform.flip(omni,True,False),
            pygame.transform.flip(omni,True,False)
        ]
        omnitrix_1 = Especial(1120,500,pantalla,imagen_omnitrix)
        omnitrix_2 = Especial(48,450,pantalla,imagen_omnitrix)
        omnitrix_3 = Especial(84,240,pantalla,imagen_omnitrix)
        omnitrix_4 = Especial(570,330,pantalla,imagen_omnitrix)
        omnitrix = [omnitrix_1,omnitrix_2,omnitrix_3,omnitrix_4]

        # CORAZON
        cora = pygame.image.load("RECURSOS\corazon.png")
        imagen_corazon = [
            cora,
            cora,
            pygame.transform.flip(cora,True,False),
            pygame.transform.flip(cora,True,False)
        ]
        corazon = Especial(1100,150,pantalla,imagen_corazon)
        corazon_1 = Especial(600,140,pantalla,imagen_corazon)
        corazones = [corazon,corazon_1]
    
        
        # VENENO
        imagen_veneno = [
            pygame.image.load("RECURSOS\sprite_veneno.png"),
            pygame.image.load("RECURSOS\sprite_veneno2.png"),
            pygame.image.load("RECURSOS\sprite_veneno3.png"),
            pygame.image.load("RECURSOS\sprite_veneno4.png")
        ]
        veneno = Especial(500,580,self.pantalla,imagen_veneno)
        veneno_1 = Especial(455,130,self.pantalla,imagen_veneno)
        venenos = [veneno,veneno_1]

        # SIERRA
        sierra = [pygame.image.load("RECURSOS\sprite_sierra.png"),
                pygame.image.load("RECURSOS\sprite_sierra_2.png")]


        sierra_1 = Slider(460,600,self.pantalla,sierra,1160,300)
        sierra_2 = Slider(880,520,self.pantalla,sierra,1160,830)
        sierra_3 = Slider(260,320,self.pantalla,sierra,500,80,"vertical")
        sierra_4 = Slider(-20,200,self.pantalla,sierra,300,75,"vertical")
        sierra_5 = Slider(900,270,self.pantalla,sierra,1160,900)
        sierras = [sierra_1,sierra_2,sierra_3,sierra_4,sierra_5]
        
        super().__init__(pantalla, personaje_principal, lista_plataformas, img_fondo, enemigos, omnitrix, corazones,sierras,venenos)