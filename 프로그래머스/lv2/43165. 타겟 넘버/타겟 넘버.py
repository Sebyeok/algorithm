from collections import deque
import math

def solution(numbers, target):
    answer = 0
    queue = deque([numbers[0],-numbers[0]])
    for i in range(1, len(numbers)):
        for j in range(int(math.pow(2,i))):
            v = queue.popleft()
            queue.append(v+numbers[i])
            queue.append(v-numbers[i])
    for num in queue:
        if(num==target):
            answer+=1
    return answer