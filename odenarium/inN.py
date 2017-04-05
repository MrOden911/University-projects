from odenarium import isint

def inN(text='Введите: ',feedback='Введено не натуральное значение!'):
    while True:
        Z=isint(input(text))
        if Z=='' or Z<=0:
            print(feedback)
        else:
            return Z
