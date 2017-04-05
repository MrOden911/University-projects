def isvar(x):
    if '_' in x and x[0]!='_':
        x=x.replace('_','')
        return isvaar(x)
    else:
        return isvaar(x)

def isvaar(x):
    if x[0].isalpha():
        for i in x:
            if i.isnumeric():
                x=x.replace(i,'')
        if x.isalpha():
            return True
    return False
            
