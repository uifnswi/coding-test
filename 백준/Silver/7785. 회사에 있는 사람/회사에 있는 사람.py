# n=int(input())
# arr=[]
# for i in range(n):
#     a,b=map(str,input().split())
#     arr.append([a,b])
# l=[]
# for i in range(n):
#     if arr[i][1]=='leave':
#         l.remove(arr[i][0])
#     else:l.append(arr[i][0])
# l.sort(reverse=True)
# for i in l:
#     print(i)

n=int(input())
arr={}

for i in range(n):
    a,b=input().split()
    if b=='enter':
        arr[a]=True
    else:del arr[a]

for a in sorted(arr.keys(), reverse=True):
    print(a)