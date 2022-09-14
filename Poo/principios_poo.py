
class Coche():
## Se crea constructor, el cual me da el estado inicial de la clase
    def __init__(self) -> None:
        
##Se crean las propiedades de la clase
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas =4
        self.__enmarcha=False

    ##Se establecen comportamientos (Metodos)
    ##self: hace referencia al propio objeto perteneciente a la clase.

    def arrancar(self, arrancamos):

        self.__enmarcha=arrancamos
        if (self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if (self.__enmarcha and chequeo):
            return "El coche esta en marcha"

        elif(self.__enmarcha and chequeo == False):
            return "Algo a ido mal en el chequeo, no podemos arrancar"

        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis,
                " y un laro de ", self.__largoChasis)

    def __chequeo_interno(self):
        print("Realizando cheque interno")

        self.gasolina= "ok"
        self.aceite="ok"
        self.puertas="Cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="Cerradas"):
            return True
        else:
            return False

##Construccion de objetos
##Instaciar el objeto es cuando se asigna la clase al objeto que se esta creando.
miCoche = Coche()
miCoche.arrancar(True)
print(miCoche.arrancar(True))
miCoche.estado()


print("-----------------A continucion creamos el segundo objeto -----------------------------")

miCochecito=Coche()
miCochecito.arrancar(False)
print(miCochecito.arrancar(False))
miCochecito.estado()