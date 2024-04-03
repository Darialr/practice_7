k = 0
num = []
for i in range(100, 1000):
    if i % 17 == 0:
        num.append(i)
        k += 1
print(*num)
print(k)
