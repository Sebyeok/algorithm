import sys

input = sys.stdin.readline
sum = 0
n = int(input())
a = [int(input()) for _ in range(n)]

max = a[n-1]

for i in range(n-2,-1,-1):
  if(a[i] >= max):
    sum += abs(a[i] - (max - 1))
    a[i] = max - 1
  max = a[i]

print(sum)