from odenarium import isint

def inN0(text='Введите: ',feedback='Введено неверное значение!'):
    while True:
        Z=isint(input(text))
        if Z=='' or Z<0:
            print(feedback)
        else:
            return Z
