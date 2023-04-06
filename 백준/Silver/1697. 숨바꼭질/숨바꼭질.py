import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

isVisit = set()
queue = deque([n])
count = {}
count[n] = 0

isVisit.add(n)
while(queue):
    v = queue.popleft()
    if(k in count):
        break
    elif(v >= 0 and v <= 100000):
        if(not v+1 in isVisit):
          queue.append(v+1)
          count[v+1] = count[v]+1
          isVisit.add(v+1)
        if(not v-1 in isVisit):
          queue.append(v-1)
          count[v-1] = count[v]+1
          isVisit.add(v-1)
        if(not v*2 in isVisit):
          queue.append(v*2)
          count[v*2] = count[v]+1
          isVisit.add(v*2)
print(count[k])
