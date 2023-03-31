import sys
input = sys.stdin.readline

n = int(input())

# flowers = [[1,1,3,6],[3,4,5,8],....]
flowers = [list(map(int, input().split())) for _ in range(n)] 

# flowers = [[101, 306],[304, 508],....]
flowers = [[flower[0]*100 + flower[1], flower[2]*100 + flower[3]] for flower in flowers] 

# flowers = [[301, 306],[304, 508],....]
for i in range(n):
  if(flowers[i][0] < 301):
    flowers[i][0] = 301
  if(flowers[i][1] > 1131):
    flowers[i][1] = 1131

#시작 하는 날 기준으로 정렬
flowers.sort(key = lambda x: x[0])

# flowers에서 시작 값의 가장 작은 값이 301보다 크면 0을 출력하고 종료
if(flowers[0][0] > 301): 
  print(0)
  exit(0)

# 끝나는 날의 max 값을 구하기 위해 끝나는 날들의 리스트를 만듦
flowerend = [flower[1] for flower in flowers]
  
count = 0 # 꽃의 개수
endpoint = 301
i = 0 # start point
j = 1 # end point

while(endpoint < 1131):
  # i 인덱스의 피는 날이 endpoint보다 크면 이어나갈 수 없으므로 바로 종료
  if(flowers[i][0] > endpoint):
    break
  # j가 n일때까지 증가하면 i인덱스부터 끝까지 지는 날이 1131인 값이 있는지 체크하여 있으면 count+1 하고 endpoint 수정 후 종료.
  if(j == n):
    if(max(flowerend[i:]) < 1131):
      break
    else:
      count += 1
      endpoint = 1131
      break
  # j인덱스의 시작하는 날이 endpoint보다 작거나 같으면 j+1
  if(flowers[j][0] <= endpoint):
    j+=1
  # j인덱스의 시작하는 날이 endpoint보다 크면 i~j-1 인덱스까지 중에 지는 날이 가장 큰 값으로 endpoint 변경 후 i와 j 인덱싱, count+1
  else:
    endpoint = max(flowerend[i:j])
    count += 1
    i = j
    j = i+1

if(endpoint == 1131):
  print(count)
else:
  print(0)