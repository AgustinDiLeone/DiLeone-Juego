import pygame
from pygame.locals import *

from API.GUI_button_image import *
from API.GUI_form import *
from API.GUI_contenedor_nivel import FormContenedorNivel
from manejador_niveles import *

class FormMenuPlay(Form):
    def __init__(self, screen, x, y, w, h, color_background,path_image, color_border="Black", active=True, ):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        self.manejador_niveles = Manejador_niveles(self._master)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image

        self.btn_level_1 = Button_Image(self._slave,x,y,100,100,100,150,"API\home.png",self.entrar_nivel,"nivel_uno")
        self.btn_level_2 = Button_Image(self._slave,x,y,250,100,100,150,"API\home.png",self.entrar_nivel,"nivel_dos")
        #self.btn_level_3 = Button_Image(self._slave,x,y,250,100,100,150,"API\home.png",self.entrar_nivel,"nivel_dos")
        self.btn_home = Button_Image(self._slave,x,y,400,400,50,50,"API\home.png",self.btn_home_click,"")
        
        self.lista_widgets.append(self.btn_level_1)
        self.lista_widgets.append(self.btn_level_2)
        #self.lista_widgets.append(self.btn_level_3)
        self.lista_widgets.append(self.btn_home)

    def on(self, param):
        print("hola", param)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)
    
    def entrar_nivel(self,nombre_nivel):
        nivel = self.manejador_niveles.get_niveles(nombre_nivel)
        form_contenedor_nivel = FormContenedorNivel(self._master,nivel)
        self.show_dialog(form_contenedor_nivel)

    def btn_home_click(self,param):
        self.end_dialog()
