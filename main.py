import sys,os
from config import *
from API.GUI_form_prueba import *
from SQL.sql import traer_id_ultimo,actualizar_nombre
os.system("cls")
pygame.init()

PANTALLA = pygame.display.set_mode(SIZE_SCREEN)
pygame.display.set_caption("BEN 10")
RELOJ = pygame.time.Clock()

# ICONO  ###############################################################3
icono = pygame.image.load(r"RECURSOS\ben_parado.png")
pygame.display.set_icon(icono)

# FUENTE ##############################################################
fuente = pygame.font.SysFont("Arco Font",70)
cronometro = pygame.time.get_ticks
form_prueba = FormPrueba(PANTALLA, 0, 0, PANTALLA.get_width(),PANTALLA.get_height())

# BASE DE DATOS #######################################################
crear_personaje()
mensaje_antiguo = ""

while True:
    RELOJ.tick(FPS)
    PANTALLA.fill("black")
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
    try:
        form_prueba.update(lista_eventos)
    except:
        print("Error en la actualizacion del juego")
    if form_prueba.ingreso_txt_box() != "" and form_prueba.ingreso_txt_box() != mensaje_antiguo:
        mensaje_antiguo = form_prueba.ingreso_txt_box()
        ultimo_id = traer_id_ultimo()
        actualizar_nombre(mensaje_antiguo,ultimo_id)

    pygame.display.update()