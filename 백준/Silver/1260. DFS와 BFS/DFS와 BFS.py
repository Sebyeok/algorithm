import sys
from collections import deque
input = sys.stdin.readline

def dfs(node, isVisit, graph): # dfs탐색 함수(재귀 함수)
  isVisit[node] = True # 방문했다는 표시
  print(node, end=' ')
  for i in graph[node]: # 연결된 그래프
    if(not isVisit[i]):
      dfs(i, isVisit, graph)

def bfs(node, isVisit, graph): # 탐색 함수(재귀 함수)
  isVisit[node] = True # 방문했다는 표시
  queue = deque([node])
  while(queue):
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]: # 연결된 그래프
        if(not isVisit[i]):
            isVisit[i] = True # 방문했다는 표시
            queue.append(i)

n, m, start = map(int, input().split())

graph = []
for i in range(n+1):
   graph.append([])

# graph에 각 노드별로 연결된 노드들을 집합에 넣는다.
for i in range(m):
  x, y = map(int, input().split())
  graph[y].append(x)
  graph[x].append(y)

for i in range(1, n+1):
    graph[i].sort()

isVisit = [False] * (n+1) # isVisit 초기화
dfs(start, isVisit, graph)
print()

isVisit = [False] * (n+1) # isVisit 초기화
bfs(start, isVisit, graph)
