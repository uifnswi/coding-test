n,m=map(int,input().split())
h=set()
s=set()
for i in range(n):
    h.add(input())
for i in range(m):
    s.add(input())

p=sorted(h&s)

print(len(p))
for i in p:
    print(i)