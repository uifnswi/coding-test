n=int(input())
p=list(map(int,input().split()))
p.sort()

m=[p[0]]
for i in range(1,n):
    m.append(m[i-1]+p[i])
print(sum(m))