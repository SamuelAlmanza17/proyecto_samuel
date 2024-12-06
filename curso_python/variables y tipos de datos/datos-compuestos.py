#AGRUPAR DATOS arrays (del 0 al 9)
lista = ["Samuel Almanza", "Samuelito17", True, 1.85] #la list puede modificar los datos
tipla = ("Samuel Almanza", "Samuelito17", True, 1.85) #la tupla no puede modificar los datos
print(lista[0]) #se pide que muestre el primer elemento, el 1 el segundo elemmento y asi sucesivamente

lista[3] = "Maquinota" #cambiar lo que hay en la posición 3 de la tabla

print(lista)


#crear un conjunto (set)

#un conjunto no los datos no tienen un orden fijo, asi que las posiciones de los datos pueden cambiar
#no se pueden cambiar los datos, igua que las tuplas
#no piermite repetir datos, asi que se usa para eliminar datos duplicados
#no se puede acceder por un indice

conjunto = {"Samuel Almanza", "Samuelito17", True, 1.85}

conjunto


#CREAR UN DICCIONARIO DE DATOS (dict)

diccionario = {
    'nombre' : 'samuelito',
    'edad' : '23',
    'estatura' : 1.81,
    'dni' : 1007863835,
    'genero masculino' : True
}

print(diccionario['estatura'] + 2)

