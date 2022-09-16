class Coche():

    def desplazamiento(self):
        print("Me desplazon en 4 ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo en 2 ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo en 6 ruedas")


""" Esta funcion se encarga de llamar a cada metodo desplazamiento de las clases """
def desplazamiento(vehiculo):
    vehiculo.desplazamiento()


miVehiculo = Camion()
desplazamiento(miVehiculo)
        
