class Coche():
##Se crean las propiedades de la clase
    largoChasis = 250
    anchoChasis = 120
    ruedas =4
    enmarcha=False

    ##Se establecen comportamientos (Metodos)
    ##self: hace referencia al propio objeto perteneciente a la clase.

    def arrancar(self, arrancamos):

        self.enmarcha=arrancamos

        if (self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene ", self.ruedas, " ruedas. Un ancho de ", self.anchoChasis,
                " y un laro de ", self.largoChasis)


##Construccion de objetos
##Instaciar el objeto es cuando se asigna la clase al objeto que se esta creando.
miCoche = Coche()

print(miCoche.largoChasis)

print("El coche tiene", miCoche.ruedas, "ruedas")

miCoche.arrancar(True)
print(miCoche.arrancar(True))
miCoche.estado()


print("-----------------A continucion creamos el segundo objeto -----------------------------")

miCochecito=Coche()
miCochecito.arrancar(False)
print(miCochecito.arrancar(False))
miCochecito.estado()