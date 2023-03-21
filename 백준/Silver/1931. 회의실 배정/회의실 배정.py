n = int(input())

meets = []

count = 0

for i in range(0,n) :
  meets.append(list(map(int, input().split())))

meets.sort(key = lambda x : (x[1], x[0]))
# print(meets)
i=0
j=1
while(i<n and j<n):
  # print("반복문1-",i,j)
  count+=1
  # print("count+1")
  while(j<n-1 and not meets[i][1] <= meets[j][0]):
    # print ("반복문2-",j+1)
    j+=1
  if(j==n-1 and meets[i][1] <= meets[n-1][0]):
    # print("마지막카운트")
    count+=1
    break
  i=j
  j=i+1
    
print(count)