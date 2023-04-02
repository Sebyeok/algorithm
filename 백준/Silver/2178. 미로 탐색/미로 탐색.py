import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

miro = []

miro.append([0 for _ in range(m+2)])
for i in range(1, n+1):
    miro.append([0])
    for j in input().rstrip():
        miro[i].append(int(j))
    miro[i].append(0)
miro.append([0 for _ in range(m+2)])

isVisit = [[False for _ in range(m+2)] for _ in range(n+2)]
queue = deque([[1,1]])

while(queue):
    i, j = queue.popleft()
    if(miro[i+1][j] > 0 and not isVisit[i+1][j]):
        miro[i+1][j] = miro[i][j] + 1
        isVisit[i+1][j] = True
        queue.append([i+1, j])
    if(miro[i][j+1] > 0 and not isVisit[i][j+1]):
        miro[i][j+1] = miro[i][j] + 1
        isVisit[i][j+1] = True
        queue.append([i, j+1])
    if(miro[i-1][j] > 0 and not isVisit[i-1][j]):
        miro[i-1][j] = miro[i][j] + 1
        isVisit[i-1][j] = True
        queue.append([i-1, j])
    if(miro[i][j-1] > 0 and not isVisit[i][j-1]):
        miro[i][j-1] = miro[i][j] + 1
        isVisit[i][j-1] = True
        queue.append([i, j-1])

print(miro[n][m])