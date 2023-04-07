s = input()
s_list = list(map(str, str(s)))
sum=0
for s in s_list:
    if s == 'A' or s == 'B' or s == 'C':
        sum += 3
    elif s == 'D' or s == 'E' or s == 'F':
        sum +=4
    elif s == 'G' or s == 'H' or s == 'I':
        sum += 5
    elif s == 'J' or s == 'K' or s == 'L':
        sum += 6
    elif s == 'M' or s == 'N' or s == 'O':
        sum += 7
    elif s == 'P' or s == 'Q' or s == 'R' or s == 'S':
        sum += 8
    elif s == 'T' or s  == 'U' or s == 'V':
        sum += 9
    elif s == 'W' or s == 'X' or s == 'Y' or s == 'Z':
        sum += 10
print(sum)