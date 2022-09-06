def evalua_edad (edad):

    if edad < 0:
        raise TypeError("No se permiten edades negativas")
        
    if edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres maduro"
    elif edad < 100:
        return "Cuidate"

print(evalua_edad(18))                    