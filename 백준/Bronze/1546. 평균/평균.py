N = int(input())
n_list = list(map(int, input().split()))
sum = 0
for i in range (0,len(n_list)):
    M = max(n_list)
    sum += int(n_list[i])/M*100
print(sum/N)