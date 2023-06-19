n = int(input())
cnt = n # 그룹 단어의 최대 개수
for i in range(n):
    word = input() # 단어를 n번 입력 받는다
    for j in range(0,len(word)-1):
        if word[j] == word[j+1]: # 한 번 나왔던 단어가 연속해서 나오면 그룹단어
            pass
        elif word[j] in word[j+1:]: # 한 번 나왔던 단어가 연속해서 x 뒤에 또 나오면 
            cnt -= 1 
            break
print(cnt)