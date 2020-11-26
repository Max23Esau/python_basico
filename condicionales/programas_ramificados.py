numero1 = int(input('Escribe un numero: '))
numero2 = int(input('Escribe otro numero: '))

if numero1 > numero2:
  print('El ' + str(numero1) + ' es mayor que el ' + str(numero2))
elif numero1 < numero2:
  print('El ' + str(numero1) + ' es menor que el ' + str(numero2))
else: 
  print('Los dos numeros son iguales')
