def conversor(tipo_pesos, valor_dolar):
    pesos = input('¿Cuantos pesos ' + tipo_pesos + ' tiene?: ')
    pesos = float(pesos)
    valor_dolar = valor_dolar
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    if(dolares == '1.0'):
        print('Tienes $' + dolares + ' dolar')
    else:
        print('Tienes $' + dolares + ' dolares')

menu = '''
Bienvenido al conversor de monedas 💱

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion: '''

opcion  = int(input(menu))

if opcion == 1:
    conversor('colombianos', 3875)
elif opcion == 2:
    conversor('argentinos', 65)
elif opcion == 3:
    conversor('mexicanos', 21)

else:
    print('Ingresa una opcion correcta por favor')


