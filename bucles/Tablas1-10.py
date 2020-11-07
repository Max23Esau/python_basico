def operacion(base):
    for i in range(11):
        print(str(base) + ' x ' + str(i) + ' = ' + str(base*i))

menu = '''
Tablas de multiplicar
1. Tabla del 1
2. Tabla del 2
3. Tabla del 3
4. Tabla del 4
5. Tabla del 5
6. Tabla del 6
7. Tabla del 7
8. Tabla del 8
9. Tabla del 9
10. Tabla del 10

Elige una opcion: '''

opcion = int(input(menu))

if __name__ == '__main__':
    operacion(opcion)




