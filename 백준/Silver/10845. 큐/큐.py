import sys
input = sys.stdin.readline
from collections import deque
dq=deque()
n=int(input())
for i in range(n):
    a=input().split()
    if a[0]=='push':
        dq.append(a[1])
    elif a[0]=='front':
        if len(dq)==0:
            print(-1)
        else:
            print(dq[0])
    elif a[0]=='back':
        if len(dq)==0:
            print(-1)
        else:
            print(dq[-1])
    elif a[0]=='size':
        print(len(dq))
    elif a[0]=='empty':
        if len(dq)==0:print(1)
        else:print(0)
    else:
        if len(dq)==0:
            print(-1)
        else:print(dq.popleft())