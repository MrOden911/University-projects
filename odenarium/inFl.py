from odenarium import isfloat

def inFl(text='Введите: ',feedback='Значение задано неверно!'):
    while True:
        Z=isfloat(input(text))
        if Z=='':
            print(feedback)
        else:
            return Z
