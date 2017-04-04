from odenarium import isint

def inInt(text='Введите: ',feedback='Введено не целое цисло!'):
    while True:
        Z=isint(input(text))
        if Z=='':
            print(feedback)
        else:
            return Z
