from nivel_uno import *
from config import *

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

nivel_actual = NivelUno(PANTALLA)

while True:
    RELOJ.tick(FPS)
    
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    print(cronometro) 
    nivel_actual.update(lista_eventos)

    pygame.display.update()