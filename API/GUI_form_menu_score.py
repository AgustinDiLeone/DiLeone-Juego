import pygame
from pygame.locals import *

from API.GUI_button_image import *
from API.GUI_form import *
from API.GUI_label import *

class FormMenuScore(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border,active,path_image,
                score,margen_y,margen_x, espacio) -> None:
        super().__init__(screen, x, y, w, h, color_background, color_border,active)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))

        self._slave = aux_image
        self.score = score

        self.magen_y = margen_y
        
        label_jugador = Label(self._slave, x=margen_x + 10, y = 20, w=w/2-margen_x-10, h=50, text="jugador", 
                        font="Verdana", font_size=30,font_color="White",path_image= r"API\bar.png")
        label_personaje = Label(self._slave, x=margen_x + 10 + w/2-margen_x-10, y=20, w=w/2-margen_x-10, h=50, 
                                text="Puntaje",font="Verdana", font_size=30,font_color="White",path_image= r"API\bar.png")
        
        self.lista_widgets.append(label_jugador)
        self.lista_widgets.append(label_personaje)

        pos_inicial_y = margen_y

        for j in self.score:
            pos_inicial_x = margen_x
            for n,s in j.items():
                cadena = ""
                cadena = f"{s}"
                jugador = Label(self._slave,pos_inicial_x,pos_inicial_y, w/2-margen_x,100, cadena,"Verdana",30,"White","API\Table.png")
                self.lista_widgets.append(jugador)
                pos_inicial_x += w/2 - margen_x
            pos_inicial_y += 100 + espacio

        self._btn_home = Button_Image(self._slave,x,y,w-70,h-70,50,50,"API\home.png",self.btn_home_click,"","","Verdana",15,"Green","red","blue")

        self.lista_widgets.append(self._btn_home)

    def btn_home_click(self,param):
        self.end_dialog()

    def update(self,lista_eventos):
        if self.active:
            for wid in self.lista_widgets:
                wid.update(lista_eventos)
            self.draw()
