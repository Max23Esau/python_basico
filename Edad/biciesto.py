def biciesto():
    year = int(input('\nAverigua si un año es biciesto o no.\nIngresa el año que desees: '))
    if year % 4 == 0 and year % 100 != 0 or year % 4 == 0 and year % 400 == 0:
        print('El ' + str(year) + ' es biciesto')
    else:
        print('El ' + str(year) + ' no es biciesto')

if __name__ == '__main__':
    biciesto()

#Divisible          No_Divisible
# 2020 % 4 == 0 and 2020 % 100 != 0

#                 or 

# #Divisible          Divisible
# 2020 % 4 == 0 and 2020 % 400 == 0
