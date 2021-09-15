import math

def is_prime(n):
    for i in range(2,int(n**1/2)+1):
        if n%i==0:
            return 0
    return 1        

def generate_all_primes(n):
    prime_list=[]
    for i in range(2,n+1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list   

def lucas_lehmer_test (p):
    if(p==2): return 1
    r_1=4 # k>=2
    M_p=(2**p)-1
    
    for i in range(2,p):
        r_1=(r_1**2-2)%M_p
        if r_1==0:
            return 1
    return 0

def find_mersenne_primes(max):
    mersenneList=[]
    for i in generate_all_primes(max):
        if lucas_lehmer_test(i):
            mersenneList.append(i)
    return mersenneList        

number=[3,17,31,521,9689,9697]
for i in number:
    print("lucas_lehmer_test(",i,") = ",lucas_lehmer_test(i))
    
print("find_mersenne_primes(5000)=",find_mersenne_primes(5000))