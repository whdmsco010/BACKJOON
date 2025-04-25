def dfs(graph, node, visited):
    if node not in visited:
        visited.add(node) # set이기 때문에 add 사용
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited) # 재귀 

n = int(input())
m = int(input())

graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i) # 양방향 그래프
    graph[i].sort() # 노드를 오름차순으로 정렬

visited = set() # 중복을 방지하기 위함
dfs(graph, 1, visited)
print(len(visited) - 1) 