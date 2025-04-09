
#nombre = input("¿como te llamas?")
#print ("Hola" , nombre)

"""edad = int (input("Ingrese su edad : "))
if edad >=18:
    print ("Eres mayor de edad")
else:
    print("No eres mayor de edad")    """

edad = int (input("Ingrese su edad : "))

def verificar_edad(edad):

    if edad >=18:
        return "Eres mayor de edad"
    else:
        return "No eres mayor de edad"

print(verificar_edad(edad))



