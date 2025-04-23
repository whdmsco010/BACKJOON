import heapq

n = int(input())
a = []
for _ in range(n):
    s, f = input().split()
    a.append((int(s), int(f)))
a.sort()

end_times = [] # 진행중인 회의의 종료 시간을 저장함

for start, end in a:
    if end_times and start >= end_times[0]:
        heapq.heappop(end_times)
    heapq.heappush(end_times, end)
print(len(end_times))