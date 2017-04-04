def isfloat(x):
        CHISL=['1','2','3','4','5','6','7','8','9','0']
        if x=='':
            return ''
        res=0
        reg=0
        rem=0
        if '-' in x and x[0]!='-':
            return ''
        for i in range(len(x)):
                
                if x[i]=='-':
                        res+=1
                elif x[i]=='.':
                        reg+=1
                elif x[i] in CHISL:
                        rem+=1
                elif x[i] not in CHISL:
                        return ''
                if reg>1 or res>1:
                        return ''
            
        if rem==0:
                return ''
        return float(x)
