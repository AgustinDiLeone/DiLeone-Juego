import pygame
from pygame.locals import *
from config import*
from API.GUI_button import *
from API.GUI_slider import *
from API.GUI_textbox import *
from API.GUI_label import *
from API.GUI_form import *
from API.GUI_form_menu_score import *
from API.GUI_checkbox import *
from API.GUI_picture_box import *
from API.GUI_form_menu_play import *


class FormPrueba(Form):
    def __init__(self, screen, x, y, w, h, color_background="red", color_border="black", border_size=-1, active=True) -> None:
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.volumen = 0.2
        self.flag_play = True
        self.mensaje_antiguo = ""

        pygame.mixer.init()

        # CONTROLES ###############################################

        self.textbox = TextBox(self._slave,x,y,50,50,150,30,"gray","white","red",
                            "blue",2,font="Comic Sans",font_size=15,font_color="black")
        self.boton_play= Button(self._slave,x,y,100,100,100,50,"Red","blue", self.btn_play_click, "Nombre","Pausa","Verdana",15,"White")
        self.label_volume = Label(self._slave,650,190,100,50,"20%","Comic Sans", 15,"white", "API\Table.png")
        self.slider_volumen = Slider(self._slave,x,y,100,200,500,15,self.volumen,"black","green")
        self.boton_tabla = Button_Image(self._slave,x,y,255,100,50,50,"API\Menu_BTN.png",self.btn_tabla_click,"fghj")
        self.boton_jugar = Button_Image(self._slave,x,y,320,100,75,50,r"RECURSOS\boton_play.png",self.btn_jugar_click,"a")
        #self.checkbox = CheckBox(self._slave,x,y,100,230,50,50,r"API\boton_on.png",r"API\home.png")
        #self.picture_box = PictureBox(self._slave,300,230,100,50,"API\home.png")

        # AGREGAR #############################
        self.lista_widgets.append(self.textbox)
        self.lista_widgets.append(self.boton_play)
        self.lista_widgets.append(self.label_volume)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.boton_tabla)
        self.lista_widgets.append(self.boton_jugar)
        #self.lista_widgets.append(self.checkbox)
        #self.lista_widgets.append(self.picture_box)
        pygame.mixer.music.load("RECURSOS\cancion_fondo.mp3")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        self.render()
    
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widgets in self.lista_widgets:
                    widgets.update(lista_eventos)
                self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

    def ingreso_txt_box(self):
        return self.textbox.get_text()

    def render(self):
        self._slave.fill(self._color_background)

    def btn_jugar_click(self,param):
        frm_jugar = FormMenuPlay(self._master,self._master.get_width()/2-250,self._master.get_height()/2-250,
                                500,500,MAGENTA,"API\Window.png",WHITE,True)
        self.show_dialog(frm_jugar)
        
    def btn_play_click(self,param):
        if self.flag_play:
            pygame.mixer.music.pause()
            self.boton_play._font_color = "red"
            self.boton_play._color_background = "Cyan"
            self.boton_play.set_text("Play")
        else:
            pygame.mixer.music.unpause()
            self.boton_play._font_color = "White"
            self.boton_play._color_background = "Red"
            self.boton_play.set_text("Pause")
        self.flag_play = not self.flag_play

    def update_volumen(self,lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volume.set_text(f"{round(self.volumen *100)}%")
        pygame.mixer.music.set_volume(self.volumen)

    def btn_tabla_click(self,texto):
        form_puntaje = FormMenuScore(self._master,340,80,500,550,"Green","White",True,"API\Window.png",
                                    "dic_score",100,10,10)

        self.show_dialog(form_puntaje)