from odenarium import isvar
def invar(text='Введите переменную: ',feedback='Ошибка при вводе, повторите попытку.'):
    while True:
        x=input(text)
        if isvar(x):
            return x
        else:
            print(feedback)
