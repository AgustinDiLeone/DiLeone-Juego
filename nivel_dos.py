import pygame
from pygame.locals import *
from nivel import *
from config import *
from slider import *


class NivelDos(Nivel):
    def __init__(self, pantalla) -> None:
        self.pantalla = pantalla
        # FONDO ############################################
        img_fondo = pygame.image.load(r"RECURSOS\fondo_2.jpg")
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

        personaje_principal = Personaje(self.pantalla,quieto[0], (20,45), 80, 550, 10, -15, lista_acciones)

        # PLATAFORMA   ########################################################

        piso = plataforma(self.pantalla,r"RECURSOS\piso_hielo.png", (WIDTH,82),0,HEIGHT-82)

        plataforma_a = plataforma(self.pantalla,r"RECURSOS\piso_hielo.png", (400,50),0,260)
        plataforma_b = plataforma(self.pantalla,r"RECURSOS\piso_hielo.png", (700,50),260,430)
        plataforma_c = plataforma(self.pantalla,r"RECURSOS\piso_hielo.png", (700,50),1040,540)
        plataforma_d = plataforma(self.pantalla,r"RECURSOS\piso_hielo.png", (260,50),480,315)
        plataforma_e = plataforma(self.pantalla,r"RECURSOS\piso_hielo.png", (200,50),780,245)
        plataforma_f = plataforma(self.pantalla,r"RECURSOS\piso_hielo.png", (200,50),1000,200)

        lista_plataformas = [piso, plataforma_a,plataforma_b,plataforma_c,plataforma_d,plataforma_e,plataforma_f]

        # ENEMIGOS #############################################################

        correr_00 = [
            pygame.image.load(r"RECURSOS\enemigo_10.png"),
            pygame.image.load(r"RECURSOS\enemigo_11.png"),
            pygame.image.load(r"RECURSOS\enemigo_12.png"),
            pygame.image.load(r"RECURSOS\enemigo_13.png"),
        ]
        quieto_00 = [
            pygame.image.load(r"RECURSOS\enemigo_10.png")
        ]
        enemigo_00_movimientos = [quieto_00,correr_00]

        enemigo = Enemigo(self.pantalla, quieto_00[0],(60,90),530,380,enemigo_00_movimientos,900,260)


        # OMNITRIX 
        omni = pygame.image.load("RECURSOS\omnitrix.png")
        imagen_omnitrix = [
            omni,
            omni,
            pygame.transform.flip(omni,True,False),
            pygame.transform.flip(omni,True,False)
        ]
        omnitrix_1 = Especial(80,220,self.pantalla,imagen_omnitrix)
        omnitrix_2 = Especial(1120,460,self.pantalla,imagen_omnitrix)
        omnitrix = [omnitrix_1,omnitrix_2]

        # CORAZON
        cora = pygame.image.load("RECURSOS\corazon.png")
        imagen_corazon = [
            cora,
            cora,
            pygame.transform.flip(cora,True,False),
            pygame.transform.flip(cora,True,False)
        ]
        corazon = Especial(1100,150,self.pantalla,imagen_corazon)
        corazones = [corazon]

        # VENENO
        imagen_veneno = [
            pygame.image.load("RECURSOS\sprite_veneno.png"),
            pygame.image.load("RECURSOS\sprite_veneno2.png"),
            pygame.image.load("RECURSOS\sprite_veneno3.png"),
            pygame.image.load("RECURSOS\sprite_veneno4.png")
        ]
        veneno = Especial(860,190,self.pantalla,imagen_veneno)
        veneno_2 = Especial(577,260,self.pantalla,imagen_veneno)
        venenos = [veneno,veneno_2]

        # SIERRA
        sierra = [pygame.image.load("RECURSOS\sprite_sierra.png"),
                pygame.image.load("RECURSOS\sprite_sierra_2.png")]
        sierra_1 = Slider(0,240,self.pantalla,sierra,350,0)
        sierras = [sierra_1]
        
        super().__init__(pantalla, personaje_principal, lista_plataformas, img_fondo, enemigo, omnitrix, corazones,sierras,venenos)