from collections import deque

def solution(numbers, target):
    answer = 0
    queue1 = deque([numbers[0], -numbers[0]])
    queue2 = deque()
    for number in numbers[1:]:
        while(queue1):
            v = queue1.popleft()
            queue2.append(v+number)
            queue2.append(v-number)
        queue1 = queue2.copy()
        queue2.clear()
    
    for num in queue1:
        if(num==target):
            answer+=1
    return answer

def solution2(numbers, target):
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
