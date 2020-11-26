def run():
	usuario1 = input('Ingresa tu nombre: ').capitalize()
	edad1 = int(input('Ingresa tu edad: '))

	usuario2 = input('\nIngresa el nombre de tu amigo: ').capitalize()
	edad2 = int(input('Ingresa la edad de tu amigo: '))

	if edad1 > edad2:
		print(f'{usuario1} es mayor que {usuario2}')

	elif edad1 < edad2:
		print(f'{usuario1} es menor que {usuario2}')
	
	else:
		print(f'{usuario1} y {usuario2} tienen la misma edad')


if __name__ == "__main__":
	run()