n_list = []
for i in range(10):
    N  = int(input())
    n_list.append(N%42)
print(len(set(n_list)))