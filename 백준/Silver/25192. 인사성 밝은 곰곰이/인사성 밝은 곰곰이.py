n=int(input())
arr=set()
cnt=0
for i in range(n):
    a=input()
    if a=='ENTER':
        arr.clear()
    elif a not in arr:
        arr.add(a)
        cnt+=1
print(cnt)