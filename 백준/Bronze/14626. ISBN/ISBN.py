isbn=input()
a=0
t=0
for i in range(13):
    if isbn[i]=="*":
        a=i
        continue
    elif i%2==0:
        t+=int(isbn[i])
    else:t+=int(isbn[i])*3

for m in range(10):
    if a%2==0:
        if (t+m)%10==0:
            print(m)
            break
    else:
        if (t+m*3)%10==0:
            print(m)
            break