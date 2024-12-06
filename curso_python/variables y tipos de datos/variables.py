a = 10
b = 20
c = a + b
print(c)


#Si quiero sumar un valor extra a una variable hago

nombredelavariable = 10
nombredelavariable += 1

#esto hace que no se reemplace el valor de la variable sino que se sume un

print(nombredelavariable)

#CONCATENACIÓN con + (Unir 2 strings)

nombre = "Samuel"
bienvenida = "Hola " + nombre + ", ¿como estás?"

print(bienvenida)

#otra forma de concatenar los '' (El F {} toma el dato y lo converte en texto) f-strings

nombre = 5
bienvenida = f"Hola {nombre} ¿Como estás?"
print(bienvenida)

#borrar una variable

del bienvenida