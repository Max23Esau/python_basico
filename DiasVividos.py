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


# def menu():
#     print('\nHola! Calculemos el tiempo que has vivido')
#     age = int(input('¿En que año naciste?: '))
#     print('''
#     Meses del año
#     1. Enero
#     2. Febrero
#     3. Marzo
#     4. Abril
#     5. Mayo
#     6. Junio
#     7. Julio
#     8. Agosto
#     9. Septiembre
#     10. Octubre
#     11. Noviembre
#     12. Diciembre
#     ''')
#     month = int(input('¿En que mes naciste?: '))
#     option = ('''
#     Elige el numero de opcion de como quieres conocer tu edad!
#         Opcion 1: En años
#         Opcion 2: En meses

#     ¿Que opcion eliges?: ''')
#     chosen_option = int(input(option))
#     if chosen_option == 1:
#         in_years(age)
#     elif chosen_option == 2:
#         months(age, month)



# def in_years(year_of_birth):
#     actual_year = date.today().year

#     if year_of_birth > actual_year:
#         print('Ingresa una fecha valida')
#     else:
#         actual_age = actual_year - year_of_birth
#         print('Tienes ' + str(actual_age) + ' años.')
#     return actual_age


# def months(year_of_birth, month_of_birth):
#     actual_year = date.today().year
#     actual_month = date.today().month

#     actual_age = actual_year - year_of_birth

#     month_of_birth = actual_month - month_of_birth
#     actual_months = actual_age * 12 + month_of_birth
#     print('Tienes ' + str(actual_months) + ' meses de vida')


if __name__ == '__main__':
    menu()