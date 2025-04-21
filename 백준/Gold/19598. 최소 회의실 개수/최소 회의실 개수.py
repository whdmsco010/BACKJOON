n = int(input())
a = []
for _ in range(n):
    s, f = input().split()
    a.append((int(s), int(f)))
a.sort()

cnt = 0 # 회의실 수
end_times = [] # 진행중인 회의의 종료 시간을 저장함

for start, end in a:
    for i in range(len(end_times)):
        if start >= end_times[i]:
            end_times[i] = end
            break
    else: # for문이 끝났을 때 실행되는 else문(위의 if문과는 상관 없음)
        end_times.append(end)
        cnt += 1
print(cnt)