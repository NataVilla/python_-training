def generar_pares(limite):

    num=1
    mi_lista=[]

    while num<limite:
        mi_lista.append(num*2)
        num+=1
    return mi_lista


print(generar_pares(10))