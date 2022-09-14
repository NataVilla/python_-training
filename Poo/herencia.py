from cgi import print_arguments


class Vehicles():

    def __init__(self, trademark, model):
        self.trademark = trademark
        self.model = model
        self.run = False
        self.speed_up = False
        self.curb = False

    def start(self):
        self.run = True

    def speed(self):
        self.speed_up = True

    def stop(self):
        self.curb = True

    def status(self):
        print("Trademark: ", self.trademark, "\nModel: ", self.model, "\nRun: ", self.run, "\nSpeed up: ", self.speed_up, "\nCurb: ", self.curb)
        
    
class Furgoneta(Vehicles):
    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            "La furgoneta no esta cargada"    

class Motorcycle(Vehicles):
    h_horse = ""

    def horse(self):
        self.h_horse = "I'm making the horse"

    def status(self):
        print("Trademark: ", self.trademark, "\nModel: ", self.model, "\nRun: ", self.run, "\nSpeed up: ", self.speed_up, "\nCurb: ", self.curb, "\n", self.h_horse)    


class electric_vehicles():
    def __init__(self) -> None:
        self.autonomy = 100

    def charge(self):
        self.charging = True


myMotorcycle = Motorcycle("Honda", "CBR")
myMotorcycle.horse()
myMotorcycle.status()
myFurgoneta = Furgoneta("Renault", "Kangaroo")
myFurgoneta.speed()
myFurgoneta.status()
print(myFurgoneta.carga(True))

class Electric_bicycle(electric_vehicles, Vehicles):
    pass

myBicycle = Electric_bicycle()