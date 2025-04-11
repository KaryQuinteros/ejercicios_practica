
#Hacer un programa que solicite una edad e imprima “Es mayor” si es mayor de edad ,sino que imprima “Es menor”.

edad = int (input("Ingrese su edad : "))

def verificar_edad(edad):

    if edad >=18:
        return "Eres mayor de edad"
    else:
        return "No eres mayor de edad"

print(verificar_edad(edad))



