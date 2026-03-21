n=int(input())
for i in range(n):
    for ii in range(n-1-i,0,-1):
        print(" ",end='')
    for iii in range(2*i+1):
        print("*",end='')
    print()