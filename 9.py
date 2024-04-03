n, k, r = map(int, input().split())
kol = 1
while n < r:
    n = n * ((100 + k) / 100)
    kol += 1
print(kol)
