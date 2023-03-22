n = int(input())

S = 0

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(0,n):
  S+=A[i]*B[i]

print(S)