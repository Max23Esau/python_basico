def operacion(base, repeticiones):
    for i in range(1, repeticiones):
        print(str(base) + ' x ' + str(i) + ' = ' + str(base*i))

factor_1 = '''Tablas de multiplicar
Elige el numero que quieres multiplicar: '''
base = int(input(factor_1))

factor_2 = int(input('Elige el numero de veces que lo quieres multiplicar: '))
factor_2 += 1 
repeticiones = factor_2


if __name__ == '__main__':
    operacion(base, repeticiones)




