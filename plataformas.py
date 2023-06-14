import pygame

class plataforma():
    def __init__(self, imagen,size, x,y) -> None:
        self.imagen = pygame.image.load(imagen)
        self.imagen = pygame.transform.scale(self.imagen, size)
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_right = pygame.Rect(self.rect.right -6, self.rect.top, 6, self.rect.height)
        self.rect_left = pygame.Rect(self.rect.left, self.rect.top,6, self.rect.height)
        self.rect_top = pygame.Rect(self.rect.left, self.rect.top, self.rect.width, 6)
        self.rect_botton = pygame.Rect(self.rect.left, self.rect.bottom -6, self.rect.width, 6)



