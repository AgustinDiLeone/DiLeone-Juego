import sys
from nivel_uno import NivelUno
from nivel_dos import NivelDos
from config import *
from API.GUI_form_prueba import *

pygame.init()

PANTALLA = pygame.display.set_mode(SIZE_SCREEN)
pygame.display.set_caption("BEN 10")
RELOJ = pygame.time.Clock()

# ICONO  ###############################################################3
icono = pygame.image.load(r"RECURSOS\ben_parado.png")
pygame.display.set_icon(icono)

# MUSICA ############################################################3
#pygame.mixer.music.load("RECURSOS\musica.mp3")
#pygame.mixer.music.play(-1)
#pygame.mixer.music.set_volume(0.1)

# FUENTE ##############################################################
fuente = pygame.font.SysFont("Arco Font",70)
cronometro = pygame.time.get_ticks

form_prueba = FormPrueba(PANTALLA, 150, 150, 900,350,"gold","black", 5, True)

while True:
    RELOJ.tick(FPS)
    PANTALLA.fill("green")
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    form_prueba.update(lista_eventos)

    pygame.display.update()