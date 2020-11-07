pesosMx = input('¿Cuantos pesos mexicanos tienes?: ')
pesosMx = float(pesosMx)
valor_dolar = 21
dolares = pesosMx / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
if(dolares == '1.0'):
    print('Tienes $' + dolares + ' dolar')
else:
    print('Tienes $' + dolares + ' dolares')
