import pygame

class Especial(pygame.sprite.Sprite):
    def __init__(self,x,y, pantalla, imagen) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.pantalla = pantalla
        self.imagen = imagen[0]
        self.escaler_imagen()   
        self.animacion = imagen
        self.rect = self.imagen.get_rect()        
        self.activo = True 
        self.rect.y = y
        self.rect.x = x
        self.accion = 0
    
    def escaler_imagen(self):
        self.imagen = pygame.transform.scale(self.imagen,(60,50))   
    
    def animar(self):
        if self.accion == 0:
            self.accion = 1
            self.imagen = self.animacion[0]
            self.escaler_imagen()
        else:
            self.accion = 0
            self.imagen = self.animacion[1]
            self.escaler_imagen()

    def update(self):
        if self.activo:
            self.animar()
            self.pantalla.blit(self.imagen, self.rect)