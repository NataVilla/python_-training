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

devuelve_pares=generar_pares(10)

for i in devuelve_pares:
    print(i)