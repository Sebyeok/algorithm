import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
v1, v2 = map(int, input().split())
m = int(input())

graph = list([] for _ in range(n+1))

# graph
for i in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

isVisit = [False] * (n+1) # isVisit 초기화

queue = deque([v1])
counts = [0] * (n+1)
counts[v1]=1
while(queue):
  v = queue.popleft()
  isVisit[v] = True
  for i in graph[v]:
    if(not isVisit[i]): # 방문하지 않은 노드면
      queue.append(i)
      isVisit[i] = True
      counts[i]=counts[v]+1
print(counts[v2]-1)