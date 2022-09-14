""" Vamos a ver el uso de la funcion super() """

class Persona():

    def __init__(self, nombre, edad, lugar_residencia) -> None:
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print("Nombre: ", self.nombre, "Edad: ", self.edad, "Lugar de residencia: ", self.lugar_residencia)

class empleado(Persona):

    def __init__(self,salario, antiguedad, nombre_empleado, edad_empleado, lugar_residencia_empleado) -> None:
        super().__init__( nombre_empleado, edad_empleado, lugar_residencia_empleado)  
        self.salario = salario
        self.antiguedad = antiguedad
        
    def descripcion(self):
        print("Salario: ", self.salario, "Antiguedad: ", self.antiguedad)
        return super().descripcion()


hugo = empleado(500, 20, "Hugo", 35, "Medellin")

hugo.descripcion()