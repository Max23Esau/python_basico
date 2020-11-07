#Programa que muestra una serie de mensajes
#de acuersdo a la opcion que eligio el usuario------------------------------------------------------------------------------------
def conversacion(mensaje):
    print('Hola')
    print('Como estas?')
    print(mensaje)
    print('Adios')

opcion = int(input('Elige una opcion(1, 2, 3): '))
if opcion == 1:
    conversacion('Elegiste la opcion 1')
elif opcion == 2:
    conversacion('Elegiste la opcion 2')
elif opcion == 3:
    conversacion('Elegiste la opcion 1')
else:
    print('Escribe la opcion correcta')


#Funcion que suma dos numeros----------------------------------------------------------------------------------------------
def suma(a, b):
    print('Se suman dos numeros')
    resultado = a + b
    return resultado

sumatoria = suma(1, 4)
print(sumatoria)