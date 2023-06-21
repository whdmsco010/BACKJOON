arr = [[0]*100 for _ in range(100)] # 100*100 배열을 만들어 준다
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1 # 색종이가 차지하는 곳을 1로 바꿔준다.
_count = 0
for i in arr:
    _count = _count + i.count(1) # 1인 것(색종이가 차지하는 곳)을 count한다.
print(_count)