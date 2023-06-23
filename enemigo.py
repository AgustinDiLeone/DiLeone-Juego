from personaje import personaje

class enemigo(personaje):
    def __init__(self, pantalla, imagen, size: tuple, x, y,acciones,limite_mayor, limite_menor) -> None:
        super().__init__(pantalla, imagen, size, x, y, 10, 0, acciones)
        self.limite_mayor = limite_mayor
        self.limite_menor = limite_menor

    def direccion(self):
        if self.rect.x >= self.limite_mayor:
            self.posicion = "izquierda"
        elif self.rect.x <= self.limite_menor:
            self.posicion = "derecha"
    
    def mover(self):
        self.direccion()
        if self.posicion == "derecha":
            super().mover_derecha()
        else:
            super().mover_izquierda()

