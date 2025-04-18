import re

n = input()
# 숫자 앞에 붙은 0 제거
n = re.sub(r'\b0+(\d)', r'\1', n)
sum = 0

if '-' not in n:
    sum = eval(n)
else:
    minus = n.find('-')
    count = n.count('-')
    sum += eval(n[:minus]) # -이전의 값을 sum에 다 더해줌
    for i in range(count):
        n_minus = n.find('-', minus+1)
        if n_minus == -1: # 더이상 -가 나오지 않으면면
            sum -= eval(n[minus+1:])
            break
        else:
            sum -= eval(n[minus+1:n_minus])
            minus = n_minus
print(sum)