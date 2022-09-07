class Coche():
##Se crean las propiedades de la clase
    largoChasis = 250
    anchoChasis = 120
    ruedas =4
    enmarcha=False

    ##Se establecen comportamientos (Metodos)
    ##self: hace referencia al propio objeto perteneciente a la clase.

    def arrancar(self):
        self.enmarcha = True

    def estado(self):
        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"    

##Construccion de objetos
##Instaciar el objeto es cuando se asigna la clase al objeto que se esta creando.
miCoche = Coche()

print(miCoche.largoChasis)

print("El coche tiene", miCoche.ruedas, "ruedas")

#miCoche.arrancar()
print(miCoche.estado())