n = int(input())
vol = 0
length = 1
while vol < n:
    vol = length ** 3
    if vol <= n:
        print(vol, end=' ')
    length += 1
