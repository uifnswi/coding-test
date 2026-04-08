n=int(input())
t=0
for i in range(n):
    a,b=map(int,input().split())
    t+=b%a
print(t)