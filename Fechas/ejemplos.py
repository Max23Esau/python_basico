def run():
    from datetime import date    
    
    # hoy = datetime.date.today()
    # print(hoy)
    #>>> 2020-11-07
    
    hoy = date.today().year
    print(hoy)
    
    #>>> 2020-11-07
    
    # otro = datetime.datetime.today()
    # print(otro)
    #>>> 2020-11-07 11:00:07.835613

    # otro = datetime.time()
    # print(otro)
    #>>> 00:00:00

if __name__ == '__main__':
    run()