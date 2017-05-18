import odenarium


def YorN(vopr='(Yes/No)'):
    N = ('n', '-', '0')
    Y = ('y', '+', '1')
    while True:
        r = input(vopr)
        if r != '':
            r[0].lower()
        if r in Y:
            return True
        elif r in N:
            return False
        else:
            odenarium.erprint("Неверное значение")
