t=int(input())
for i in range(t):
    cnt=1
    n=int(input())
    p=sum(list(map(int,input().split())))
    while n>=p:
        p*=4
        cnt+=1
    print(cnt)
