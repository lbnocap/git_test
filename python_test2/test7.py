numbers=list()
num=1
for i in range(2,100):
    for x in range(2,i):
        if i%x==0:
            break
    else:
        numbers.append(i)

print(numbers)
