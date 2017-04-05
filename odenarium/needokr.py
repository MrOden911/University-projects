from odenarium import inN0, YorN

def needokr(x,op='Округлить результат? (Yes/No) '):
    l=YorN(op,n=[''])
    if l==False:
        return x
    else:
        ok=inN0('Сколько знаков после запятой? ','Введите натуральное число, или "0"')
        return round(x,ok)

  

