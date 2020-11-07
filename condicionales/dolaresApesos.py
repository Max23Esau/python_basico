dolares = input('¿Cuantos dolares tienes?: ')
dolares = float(dolares)
valor_pesoMx = 21
pesosMx = dolares * valor_pesoMx
pesosMx = round(pesosMx, 2)
pesosMx = str(pesosMx)
if(pesosMx == '1.0'):
    print('Tienes $' + pesosMx + ' peso mexicano')
else:
    print('Tienes $' + pesosMx + ' pesos mexicanos')