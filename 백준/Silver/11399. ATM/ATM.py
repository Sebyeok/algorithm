n = int(input())

S = 0

A = list(map(int, input().split()))

A.sort()

for i in range(0, n):

  S += A[i]  

  if(i<n-1):

      A[i+1] += A[i]

        

print(S)