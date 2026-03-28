arr=[]
for i in range(5):
    arr.append(int(input()))

t=0
for i in arr:
    if i<40:
        t+=40
    else:t+=i
print(t//5)