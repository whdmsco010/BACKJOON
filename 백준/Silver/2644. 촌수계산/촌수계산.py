import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

cnt = 0

def dfs(graph, node, visited, finish):
    global cnt
    if node == finish:
        return True
    visited.add(node) # set이기 때문에 add 사용
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(graph, neighbor, visited, finish): # 재귀
                cnt += 1
                return True
    return False
n = int(input())
u, v = map(int, input().split())
m = int(input())

graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i) # 양방향 그래프

visited = set() # 중복을 방지하기 위함
found = dfs(graph, u, visited, v)

if found:
    print(cnt)
else:
    print(-1)