import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = list([] for _ in range(n+1))

# graph에 각 노드별로 신뢰당하는 노드들을 집합에 넣는다.
for i in range(m):
  x, y = map(int, input().split())
  graph[y].append(x)

counts = [1] * (n+1) # counts는 각 노드를 해킹하면 해킹되는 노드들의 수(1이 기본 값)
isVisit = [False] * (n+1) # isVisit 초기화

queue = deque([])
for node in range(1, n+1): # 노드들 1~끝노드까지
  isVisit = [False] * (n+1) # isVisit 초기화
  queue.append(node)
  while(queue):
    v = queue.popleft()
    isVisit[v] = True
    for i in graph[v]:
      if(not isVisit[i]): # 방문하지 않은 노드면
        queue.append(i)
        isVisit[i] = True
        counts[node]+=1

maximum = max(counts) # 최대 값을 구한다.
for node in range(1, n+1):
  if(counts[node] == maximum): # 최대 값일 때 출력.(오름차순으로 출력 됨.)
    print(node, end=" ")