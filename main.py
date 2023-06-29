import sys
from config import *
from API.GUI_form_prueba import *
from SQL.sql import sql_table, crear_table
from modo import cambiar_modo

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
form_prueba = FormPrueba(PANTALLA, 150, 150, 900,350,"blue","black", 5, True)

# BASE DE DATOS #######################################################
sentencia_5 = '''
            delete from  Jugadores
            
            '''
crear_table(sentencia_5)

sentencia_1 = '''
            insert into Jugadores(id,nombre,puntaje) values(1,"Jugador 1",0)
            '''
crear_table(sentencia_1)

mensaje_antiguo =""

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
            
    form_prueba.update(lista_eventos)
    if form_prueba.ingreso_txt_box() != "" and form_prueba.ingreso_txt_box() != mensaje_antiguo:
        print(form_prueba.ingreso_txt_box())
        mensaje_antiguo = form_prueba.ingreso_txt_box()
        sentencia = f'''
            update  Jugadores
            set nombre = "{form_prueba.ingreso_txt_box()}"
            where id = 1
            '''
        sql_table(sentencia)


    pygame.display.update()