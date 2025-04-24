n = input()
cnt = 0
if len(n) == 1:
    n = '0' + n
m = n
while True:
    a = int(n[0])
    b = int(n[1])
    s = a + b
    n = str(b) + str(s % 10)
    cnt += 1
    if m == n:
        break
print(cnt)