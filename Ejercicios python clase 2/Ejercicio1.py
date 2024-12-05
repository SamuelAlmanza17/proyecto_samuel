edad = int (input("Ingrese su edad: "))
Nombre = (input("Ingrese su nombre: "))

primera_letra = Nombre[0].upper()

if edad < 18 and primera_letra in 'AEIOU':
    print("Perteneces al grupo 1.")
elif edad >= 18 and primera_letra not in 'AEIOU':
    print("Perteneces al grupo 2.")
else:
    print("Perteneces al grupo 3.")