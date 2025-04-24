from collections import deque

def dfs(graph, node, visited):
    if node not in visited:
        visited.add(node) # set이기 때문에 add 사용
        print(node, end=' ')
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited) # 재귀

def bfs(graph, start):
    visited = set()
    queue = deque([start]) # 시작 노드를 큐에 넣음

    while queue:
        node = queue.popleft() # 큐에서 노드 하나를 꺼냄

        if node not in visited: # 꺼낸 노드가 큐에 있는지 확인
            visited.add(node)
            print(node, end=' ')

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor) # 큐에 넣음

n, m, v = map(int, input().split())

graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i) # 양방향 그래프

for key in graph:
    graph[key].sort() # 노드를 오름차순으로 정렬

visited = set() # 중복을 방지하기 위함
dfs(graph, v, visited)
print()
bfs(graph, v)
