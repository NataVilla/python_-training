#Crear programa que devuelva ciudades
#yield from, nos permite prescindir del for anidado
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield from elemento

ciudades_devueltas= devuelve_ciudades("Madrid", "Medellin", "itagui", "Envigado")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))