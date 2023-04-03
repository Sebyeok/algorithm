import sys
from collections import deque
input = sys.stdin.readline

def findij(n):
    for x in range(1, n+1):
        for y in range(1, n+1):
            if(x==n and y==n and isVisit[x][y]==False):
                return x, y
            if(miro[x][y]==1 and isVisit[x][y]==False):
                isVisit[x][y]=True
                return x, y
            isVisit[x][y]=True
    return n, n

n = int(input())

miro = []

miro.append([0 for _ in range(n+2)])
for i in range(1, n+1):
    miro.append([0])
    for j in input().rstrip():
        miro[i].append(int(j))
    miro[i].append(0)
miro.append([0 for _ in range(n+2)])
counts = []
isVisit = [[False for _ in range(n+2)] for _ in range(n+2)]
while(True):
    i, j = findij(n)
    if((i == n and j == n) and (not(miro[i][j]==1 and isVisit[i][j]==False))):
        break
    queue = deque([[i, j]])
    counts.append(0)
    if(i==n and j==n):
        counts[len(counts)-1]+=1
        break
    while(queue):
        i, j = queue.pop()
        counts[len(counts)-1]+=1
        if(miro[i+1][j] == 1 and not isVisit[i+1][j]):
            isVisit[i+1][j] = True
            queue.append([i+1, j])
        if(miro[i][j+1] == 1 and not isVisit[i][j+1]):
            isVisit[i][j+1] = True
            queue.append([i, j+1])
        if(miro[i-1][j] == 1 and not isVisit[i-1][j]):
            isVisit[i-1][j] = True
            queue.append([i-1, j])
        if(miro[i][j-1] == 1 and not isVisit[i][j-1]):
            isVisit[i][j-1] = True
            queue.append([i, j-1])

counts.sort()
print(len(counts))
for count in counts:
    print(count)