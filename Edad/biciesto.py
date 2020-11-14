# def biciesto():
#     year = int(input('\nAverigua si un año es biciesto o no.\nIngresa el año que desees: '))
#     if year % 4 == 0 and year % 100 != 0 or year % 4 == 0 and year % 400 == 0:
#         print('El ' + str(year) + ' es biciesto')
#     else:
#         print('El ' + str(year) + ' no es biciesto')

def bucle():
    year = int(input('Año de nacimiento: '))
    fin = 2020
    dias_extra = 0

    while year <=fin:
        if year % 4 == 0 and year % 100 != 0 or year % 4 == 0 and year % 400 == 0:
            dias_extra +=1
        else:
            pass
        year += 1
    
    print('Estos son los dias extra:' + str(dias_extra))
        

if __name__ == '__main__':
    # biciesto()
    bucle()


#Divisible          No_Divisible
# 2020 % 4 == 0 and 2020 % 100 != 0

#                 or 

# #Divisible          Divisible
# 2020 % 4 == 0 and 2020 % 400 == 0


# 1900 2020