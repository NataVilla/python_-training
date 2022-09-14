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
        
    

class Motorcycle(Vehicles):
    pass

myMotorcycle = Motorcycle("Honda", "CBR")
myMotorcycle.status()
