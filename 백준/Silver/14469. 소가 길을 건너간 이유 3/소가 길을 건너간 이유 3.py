n = int(input())
a = []
ct = 0
for _ in range(n):
    s, d = input().split()
    a.append((int (s), int(d))) # 값을 두 개 넘기려면 튜플 형태로 넘겨야 한다.
a.sort()

for i, j in a:
    if ct < i:
        ct = i
    ct += j
    
print(ct)