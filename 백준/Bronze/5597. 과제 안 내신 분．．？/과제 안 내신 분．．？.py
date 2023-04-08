N = [x for x in range(1,31)]
n_list = []
for i in range(28):
    n = int(input())
    n_list.append(n)
B = [x for x in N if x not in n_list]
for b in B:
    print(b)