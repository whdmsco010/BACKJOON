s = list(input())
cnt0 = 0
cnt1 = 0
prev = ''
for i in range(len(s)):
    if s[i]=='0' and prev != '0':
        cnt0+=1
    
    elif s[i]=='1' and prev != '1':
        cnt1+=1
    prev = s[i]
if cnt0>cnt1: # 0이 더 많은 경우 1을 0으로 바꿈
    for i in range(len(s)):
        if s[i] == '1':
            s[i] = '0'
    s = ''.join(s) 
    print(cnt1)
else:
    for i in range(len(s)):
        if s[i] == '0':
            s[i] = '1'
    s = ''.join(s)
    print(cnt0)