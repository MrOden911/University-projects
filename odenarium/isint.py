def isint(x):
        CHISL=['1','2','3','4','5','6','7','8','9','0']
                          
        if x=='' or x=='-':
            return ''
        res=0
        if '-' in x and x[0]!='-':
            return ''
        for i in range(len(x)):
            if x[i]=='-':
                res+=1
            elif x[i] not in CHISL:
                return ''
            if res>1:
                return ''
        return int(x)
    
