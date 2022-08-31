#Funcion ordinaria

# def generar_pares(limite):

#     num=1
#     mi_lista=[]

#     while num<limite:
#         mi_lista.append(num*2)
#         num+=1
#     return mi_lista


# print(generar_pares(10))


#Funcion generador

def generar_pares(limite):

    num=1

    while num<limite:
        yield num*2
        num+=1

#Devuelve  el primer valor del generador.
devuelve_pares=generar_pares(10)

print(next(devuelve_pares))

print("Aqui hay mas codigo")

print(next(devuelve_pares))

print("Aqui hay mas codigo")

print(next(devuelve_pares))