n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
arr=[]
for i in a:
    arr.append(i)
for i in b:
    arr.append(i)

arr.sort()
for i in arr:
    print(i,end=" ")