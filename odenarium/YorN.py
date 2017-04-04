from odenarium import erprint

def YorN(vopr='(Yes/No)'):
    N=('n','-','0')
    Y=('y','+','1')
    while True:
        r=input(vopr)[0].lower()
        if r in Y:
            return True
        elif r in N:
            return False
        else:
            print('Неверное значение')    
