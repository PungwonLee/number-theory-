import random
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

def generate_random_prime(a,b):
    while True:
        r_num=random.randrange(a, b+1)
        if is_prime(r_num):
            return  r_num

print("is_prime(11)=",is_prime(11))
print("is_prime(253)=",is_prime(253))
print("is_prime(65537)=",is_prime(65537))


print("generate_all_primes (50)=",generate_all_primes (50))
print("generate_all_primes (100)=",generate_all_primes (100))
print("generate_all_primes (1000)=",generate_all_primes (1000))

print("generate_random_prime(2,11)=",generate_random_prime (2, 11))
print("generate_random_prime(100,200)=",generate_random_prime (100, 200))
print("generate_random_prime(1000,2000)=",generate_random_prime (1000, 2000))
