import sys
input = sys.stdin.readline
from collections import deque

f, s, g, u, d = map(int, input().split())

isVisit = set()

queue = deque([s])
count = {}
count[s]=0
isVisit.add(s)
while(queue):
    v = queue.popleft()
    if(v == g):
        break
    if(1<=v and v<=f and not v+u in isVisit):
        queue.append(v+u)
        isVisit.add(v+u)
        count[v+u] = count[v]+1
    if(1<=v and v<=f and not v-d in isVisit):
        queue.append(v-d)
        isVisit.add(v-d)
        count[v-d] = count[v]+1

if(g in count):
  print(count[g])
else:
  print("use the stairs")


