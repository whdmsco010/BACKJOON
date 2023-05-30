N = ["c=","c-","dz=","d-","lj","nj","s=","z="]
S = input()
for i in N: 
    S = S.replace(i,"*")
print(len(S))