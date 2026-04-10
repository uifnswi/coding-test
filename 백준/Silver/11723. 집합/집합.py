import sys
input = sys.stdin.readline
m=int(input())
S=set()
for _ in range(m):
    a = input().split()
    if a[0] == 'add':
        S.add(int(a[1]))
    elif a[0] == 'check':
        if int(a[1]) in S:
            print(1)
        else:
            print(0)
    elif a[0] == 'remove':
        if int(a[1]) in S:
            S.remove(int(a[1]))
    elif a[0] == 'toggle':
        x = int(a[1])
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif a[0] == 'all':
        S = set(range(1, 21))
    elif a[0] == 'empty':
        S.clear()