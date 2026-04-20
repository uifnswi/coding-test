import sys
input = sys.stdin.readline

n=int(input())
arr1=list(map(int,input().split()))
m=int(input())

arr2=[0]*(n+1)

for i in range(n):
    arr2[i+1]=arr2[i]+arr1[i]

for i in range(m):
    a,b=map(int,input().split())
    print(arr2[b]-arr2[a-1])
