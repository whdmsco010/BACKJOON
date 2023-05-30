S = input().upper()
s = list(set(S))
cnt = []
for i in s:
    cnt.append(S.count(i))
if cnt.count(max(cnt)) > 1:
    print("?")
else: 
    print(s[(cnt.index(max(cnt)))])