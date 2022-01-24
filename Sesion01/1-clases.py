class Vehiculo:
    ruedas = 4
    color = 'azul'

# para usar la plantilla hay que sacarle copias también. Para esto se hacen instancias
# hacemos copia y lo guardamos en v1


vehiculo1 = Vehiculo()
vehiculo1.ruedas = 5
vehiculo1.procedencia = 'Japon'

vehiculo2 = Vehiculo()

print(vehiculo1.ruedas)
print(vehiculo2.ruedas)
print(vehiculo1.procedencia)
print(vehiculo2.procedencia)


class VehiculoConConstructor():
    # en todo metodo de la clase SIEMPRE debemos colocar como primer parametro self
    # self sirve para referenciar la instancia actual de la clase. Se podría comparar con el this de JS. ES UNA BUENA PRÁCTICA.
    def __init__(self, ruedas, color):
        self.ruedas = ruedas
        self.color = color

    def __str__(self):
        return 'Esta es una instancia de la clase VehiculoConConstructor'


vehiculo3 = VehiculoConConstructor(4, 'morado')
print(vehiculo3)
