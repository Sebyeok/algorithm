from collections import deque 
def solution(n, computers):
    answer = 0
    connect = []
    isVisit = set()
    for i in range(n+1):
        connect.append(set())
    
    queue = deque([])
    for i in range(n):
        for j in range(n):
            if(i != j and computers[i][j] == 1):
                connect[i+1].add(j+1)
    
    for i in range(1, n+1):
        for node in connect[i]:
            if(not node in isVisit):
                queue.append(node)
                isVisit.add(node)
        if(not i in isVisit) :
            isVisit.add(i)
            answer+=1
        while(queue):
            v = queue.popleft()
            for node in connect[v]:
                if(not node in isVisit):
                    queue.append(node)
                    isVisit.add(node)
    return answer