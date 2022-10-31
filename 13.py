i=1
while i <= 100:
    if(i % 2 == 0):
        print(i)
    i = i + 1
i=1
while i <= 100:
    if(i % 2 != 0):
        print(i)
    i = i + 1
for Number in range (1, 101):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(Number)

