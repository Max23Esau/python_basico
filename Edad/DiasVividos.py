from datetime import date

def menu():
    print('\nHola! Calculemos el tiempo que has vivido')
    age = int(input('¿En que año naciste?: '))
    print('''
    Meses del año
    1. Enero
    2. Febrero
    3. Marzo
    4. Abril
    5. Mayo
    6. Junio
    7. Julio
    8. Agosto
    9. Septiembre
    10. Octubre
    11. Noviembre
    12. Diciembre
    ''')
    month = int(input('¿En que mes naciste?: '))
    all(age, month)

def all(age, month):
    year_of_birth = age
    month_of_birth = month
    
    actual_year = date.today().year
    actual_month = date.today().month
    actual_day = date.today().day

    if year_of_birth > actual_year:
        print('Ingresa una fecha valida')
    else:
        actual_age = actual_year - year_of_birth
        month_of_birth = actual_month - month_of_birth
        actual_months = actual_age * 12 + month_of_birth
        
        if actual_age == 1:
            print('Tienes ' + str(actual_age) + ' año.\nOh podemos decir que tienes ' + str(actual_months) + ' meses de vida')
        else:
            print('Tienes ' + str(actual_age) + ' años.\nOh podemos decir que tienes ' + str(actual_months) + ' meses de vida')


def days():
    day_of_birth = int(input('¿Que dia nacieste?: '))
    actual_day = date.today().day
    print('El dia que nacieste fue un ' + str(day_of_birth))
    print('El dia de hoy es ' + str(actual_day))


if __name__ == '__main__':
    menu()
