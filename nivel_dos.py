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

        plataforma_a = plataforma(self.pantalla,r"RECURSOS\piso_hielo.png", (350,50),0,300)
        plataforma_b = plataforma(self.pantalla,r"RECURSOS\piso_hielo.png", (350,50),900,300)
        plataforma_c = plataforma(self.pantalla,r"RECURSOS\piso_hielo.png", (350,50),450,400)
        plataforma_d = plataforma(self.pantalla,r"RECURSOS\piso_hielo.png", (300,50),0,500)
        plataforma_e = plataforma(self.pantalla,r"RECURSOS\piso_hielo.png", (300,50),900,500)
        plataforma_f = plataforma(self.pantalla,r"RECURSOS\piso_hielo.png", (250,50),500,200)        

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

        enemigo = Enemigo(self.pantalla, quieto_00[0],(60,90),145,250,enemigo_00_movimientos,290,0)
        enemigo_01 = Enemigo(self.pantalla, quieto_00[0],(60,90),85,450,enemigo_00_movimientos,240,0)
        enemigo_02 = Enemigo(self.pantalla, quieto_00[0],(60,90),551,350,enemigo_00_movimientos,740,450)

        enemigos = [enemigo, enemigo_01, enemigo_02]
        # OMNITRIX 
        omni = pygame.image.load("RECURSOS\omnitrix.png")
        imagen_omnitrix = [
            omni,
            omni,
            pygame.transform.flip(omni,True,False),
            pygame.transform.flip(omni,True,False)
        ]
        omnitrix_1 = Especial(70,220,self.pantalla,imagen_omnitrix)
        omnitrix_2 = Especial(1120,460,self.pantalla,imagen_omnitrix)
        omnitrix_3 = Especial(30,450,self.pantalla,imagen_omnitrix)
        omnitrix_4 = Especial(740,100,self.pantalla,imagen_omnitrix)
        omnitrix = [omnitrix_1,omnitrix_2,omnitrix_3,omnitrix_4]

        # CORAZON
        cora = pygame.image.load("RECURSOS\corazon.png")
        imagen_corazon = [
            cora,
            cora,
            pygame.transform.flip(cora,True,False),
            pygame.transform.flip(cora,True,False)
        ]
        corazon = Especial(1100,150,self.pantalla,imagen_corazon)
        corazon_1 = Especial(580,150,self.pantalla,imagen_corazon)
        corazones = [corazon,corazon_1]

        # VENENO
        imagen_veneno = [
            pygame.image.load("RECURSOS\sprite_veneno.png"),
            pygame.image.load("RECURSOS\sprite_veneno2.png"),
            pygame.image.load("RECURSOS\sprite_veneno3.png"),
            pygame.image.load("RECURSOS\sprite_veneno4.png")
        ]
        veneno = Especial(472,530,self.pantalla,imagen_veneno)
        veneno_2 = Especial(577,260,self.pantalla,imagen_veneno)
        veneno_3 = Especial(380,350,self.pantalla,imagen_veneno)
        veneno_4 = Especial(800,160,self.pantalla,imagen_veneno)
        veneno_5 = Especial(800,100,self.pantalla,imagen_veneno)
        venenos = [veneno,veneno_2,veneno_3,veneno_4,veneno_5]

        # SIERRA
        sierra = [pygame.image.load("RECURSOS\sprite_sierra.png"),
                pygame.image.load("RECURSOS\sprite_sierra_2.png")]
        sierra_1 = Slider(950,465,self.pantalla,sierra,1160,900)
        sierra_2 = Slider(1170,200,self.pantalla,sierra,300,80,"vertical")
        sierra_3 = Slider(1020,200,self.pantalla,sierra,220,80,"vertical")
        sierras = [sierra_1,sierra_2,sierra_3]
        
        super().__init__(pantalla, personaje_principal, lista_plataformas, img_fondo, enemigos, omnitrix, corazones,sierras,venenos)