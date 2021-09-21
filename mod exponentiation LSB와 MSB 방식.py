def mod_exp(a,e,n):#MSB to LSB
    binary=format(e,'b')
    print(binary)
    res=1
    for i in binary:
        res=res**2
        if i=='1': res*=a
        res=res%n
    return res

def mod_exp1(a,e,n):    #LSB to MSB
    binary=format(e,'b')
    res=1
    power=a%n
    for i in range(len(binary)-1,-1,-1):
        if (binary[i])=='1':
            res=res*power%n
        power=power*power%n    
            
    return res    
print(mod_exp(2,1234,789))
print(mod_exp1(2,1234,789))                