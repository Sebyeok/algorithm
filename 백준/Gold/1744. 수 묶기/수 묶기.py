import sys

input = sys.stdin.readline

n = int(input())

a = [int(input()) for _ in range(n)]

a.sort(reverse=True)

try:
  point = a.index(0)
except:
  point = n
  for i in range(0,n):
    if(a[i]<=0):
      point = i
      break
    

plus = a[:point]
minus = sorted(a[point:])
sum=0

i=0
while(i<len(plus)):
  if(i==len(plus)-1):
    sum += plus[i]
    break
  elif(plus[i]>1 and plus[i+1]>1):
    sum += plus[i] * plus[i+1]
    i+=2
  else:
    sum += plus[i]
    i+=1
    
i=0
while(i<len(minus)):
  if(i==len(minus)-1):
    sum += minus[i]
    break
  elif(minus[i+1] == 0):
    break
  elif(minus[i]<0 and minus[i+1]<0):
    sum += minus[i] * minus[i+1]
    i+=2
  else:
    sum += minus[i]
    i+=1
    
print(sum)
