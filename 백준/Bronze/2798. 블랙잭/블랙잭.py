n,m=map(int,input().split())
c=list(map(int,input().split()))
max=0
cc=0
for i in range(n-2):
    for ii in range(i+1,n-1):
        for iii in range(ii+1,n):
            cc=c[i]+c[ii]+c[iii]
            if cc<=m and cc>max:
                max=cc
print(max)