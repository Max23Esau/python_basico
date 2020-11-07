
# contador = 0
# while contador <= 1000:
#     print('2 elevado a '+ str(contador) + ' es igual a: ' + str(2**contador) + '\n')
#     contador = contador + 1


def run():
    LIMITE = 1000
    contador = 0
    potencia_2 = 2**contador

    while potencia_2 < LIMITE:
        print('2 elevado a '+ str(contador) + ' es igual a: ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador


if __name__ == '__main__':
    run()