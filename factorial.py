def factorial (n):
    if n==0 or n==1: 
        return 1
    else: 
        return factorial(n-1)*n

def binomia(n,k):
    if n==k or k==0:
        return 1
    else:
        if b_arr[n][k]:
            return b_arr[n][k]
        b_arr[n][k]= binomia(n-1,k-1)+binomia(n-1,k)
        return b_arr[n][k]

N=int(input("factorial Number of entries: "))
print("factorial(%d)= %d"%( N, factorial(N)))

b_arr=[[0]*10000 for _ in range(10000)]
N,K=map(int,input("Enter binomial coefficient n,k: ").split())
print("binomia(%d,%d)= %d"%(N,K,binomia(N,K)))
