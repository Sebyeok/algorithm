import sys
input = sys.stdin.readline
from collections import deque

def endCheck(h, m, n): # 모두 익었는가?
  for i in range(h):
    for j in range(m):
      for k in range(n):
        if(box[i][j][k] == 0):
          return False
  return True

n, m, h = map(int, input().split())

box = []
for i in range(h):
    box.append([])
    for _ in range(m):
      box[i].append(list(map(int, input().split())))

isVisit = []
for i in range(h):
    isVisit.append([])
    for _ in range(m):
      isVisit[i].append([False] * (n)) # isVisit 초기화

queue = deque()

for i in range(h):
  for j in range(m):
      for k in range(n):
        if(box[i][j][k] == 1 and isVisit[i][j][k] == False): # 1을 찾아서 모두 queue에 집어넣는다.
          queue.append([i,j,k])
          isVisit[i][j][k] = True
# queue에서 pop하면서 상하좌우위아래 요소들이 0인 녀석들을 1로 바꾼다. -1이면 냅둠.
while(queue):
  x, y, z = queue.popleft()
  if(x<h-1 and box[x+1][y][z] == 0 and isVisit[x+1][y][z] == False):
      box[x+1][y][z] = box[x][y][z] + 1
      isVisit[x+1][y][z] = True
      queue.append([x+1,y,z])
  if(y<m-1 and box[x][y+1][z] == 0 and isVisit[x][y+1][z] == False):
      box[x][y+1][z] = box[x][y][z] + 1
      isVisit[x][y+1][z] = True
      queue.append([x,y+1,z])
  if(x>0 and box[x-1][y][z] == 0 and isVisit[x-1][y][z] == False):
      box[x-1][y][z] = box[x][y][z] + 1
      isVisit[x-1][y][z] = True
      queue.append([x-1,y,z])
  if(y>0 and box[x][y-1][z] == 0 and isVisit[x][y-1][z] == False):
      box[x][y-1][z] = box[x][y][z] + 1
      isVisit[x][y-1][z] = True
      queue.append([x,y-1,z])
  if(z<n-1 and box[x][y][z+1] == 0 and isVisit[x][y][z+1] == False):
      box[x][y][z+1] = box[x][y][z] + 1
      isVisit[x][y][z+1] = True
      queue.append([x,y,z+1])
  if(z>0 and box[x][y][z-1] == 0 and isVisit[x][y][z-1] == False):
      box[x][y][z-1] = box[x][y][z] + 1
      isVisit[x][y][z-1] = True
      queue.append([x,y,z-1])

#토마토 확인

maximum = 1
for i in range(h):
  for j in range(m):
      for k in range(n):
         if(box[i][j][k]==0):
            print(-1)
            exit(0)
      maximum = max(maximum, max(box[i][j]))

print(maximum-1)
