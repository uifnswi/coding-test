def fac(a):
    r=1
    for i in range(2,a+1):
        r*=i
    return r
n,k=map(int,input().split())
print(fac(n)//(fac(k)*(fac(n-k))))