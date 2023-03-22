n = int(input())

ropes = []
count = 0

for i in range(0,n) :
  ropes.append(int(input()))

ropes.sort()

max = 0

for i in range(0, n):
  if(max<ropes[i]*(n-i)):
    max=ropes[i]*(n-i)

print(max)