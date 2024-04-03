tm0 = float(input())
tm1 = tm0
k = 0
while tm1 != 0:
    if tm1 < tm0:
        k += 1
    tm0 = tm1
    tm1 = float(input())
print(k)
