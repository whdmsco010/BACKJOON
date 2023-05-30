N = int(input())
for i in range(N):
    n = list(map(int, input().split()))
    m = sum(n[1:])/n[0]
    count = 0
    for i in n[1:]:
        if m < i:
            count += 1
    print('%.3f'%(count/n[0]*100)+"%")