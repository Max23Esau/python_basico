from datetime import date

#Año, mes y dia (el presente)
actual_Year = date.today().year
actual_Month = date.today().month
actual_Day = date.today().day

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
    day = int(input('En que dia naciste?: '))
    leap_Days = leap_Years(age)
    all(age, month, day, leap_Days)

def leap_Years(user_Age):
    extra_Day = 0
    while user_Age <= actual_Year:
        if user_Age % 4 == 0 and user_Age % 100 != 0 or user_Age % 4 == 0 and user_Age % 400 == 0:
            extra_Day +=1
        else:
            pass
        user_Age += 1
    return extra_Day


def all(age, month, day, leap_Days):
    #Datos del usuario
    year_of_Birth = age
    month_of_Birth = month
    day_of_Birth = day

    if year_of_Birth > actual_Year:
        print('Ingresa una fecha valida')
    else:
        # Edad actual
        user_Actual_Age = actual_Year - year_of_Birth
        
        #Meses vividos
        month_of_Birth = actual_Month - month_of_Birth
        user_Actual_Months = user_Actual_Age * 12 + month_of_Birth

        #Dias vividos
        user_Actual_Days = 365 * user_Actual_Age + leap_Days
        
        if user_Actual_Age == 1:
            print(  'Tienes ' + str(user_Actual_Age) + ' año.\n'
                    'Oh podemos decir que tienes ' + str(user_Actual_Months) + ' meses de vida'
                    'Oh podemos decir que tienes ' + str(user_Actual_Days) + ' dias de vida')
        else:
            print(  'Tienes ' + str(user_Actual_Age) + ' años.\n'
                    'Oh podemos decir que tienes ' + str(user_Actual_Months) + ' meses de vida \n'
                    'Oh podemos decir que tienes ' + str(user_Actual_Days) + ' dias de vida')


def run():
    print('\nAdivinemos cuanto tiempo has vivido')
    
    age = years()
    month = months(age)
    leap_Days = leap_Years(age)
    day = days(age, leap_Days)

    print('Tienes ' + str(age) + ' años. Los cuales son ' + str(month) + ' meses. Y en total son ' + str(day) + ' dias')

def leap_Years(user_Age):
    extra_Day = 0
    while user_Age <= actual_Year:
        if user_Age % 4 == 0 and user_Age % 100 != 0 or user_Age % 4 == 0 and user_Age % 400 == 0:
            extra_Day +=1
        else:
            pass
        user_Age += 1
    return extra_Day

def years():
    year_of_Birth = int(input('¿En que año naciste?: '))

    if year_of_Birth > actual_Year:
        print('Ingresa una fecha valida')
    else:
        user_Actual_Age = actual_Year - year_of_Birth
    return user_Actual_Age

def months(user_Actual_Age):
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
    month_of_Birth = int(input('¿En que mes naciste?: '))
    month_of_Birth = actual_Month - month_of_Birth
    actual_Months = user_Actual_Age * 12 + month_of_Birth
    return actual_Months

def days(user_Actual_Age, leap_Days):
    int(input('En que dia naciste?: '))
    user_Actual_Days = 365 * user_Actual_Age + leap_Days
    return user_Actual_Days

if __name__ == '__main__':
    # menu()
    run()
