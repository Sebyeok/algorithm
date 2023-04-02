import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = []
graph = list([] for _ in range(n+1))

for i in range(m):
  x, y = map(int, input().split())
  graph[y].append(x)
  graph[x].append(y)
isVisit = [False] * (n+1) # isVisit 초기화

queue = deque()
queue.append(1)
isVisit[1] = True
count = 0

while(queue):
  v = queue.popleft()
  for i in graph[v]:
    if(not isVisit[i]): # 방문하지 않은 노드면
      queue.append(i)
      isVisit[i] = True
      count+=1

print(count)