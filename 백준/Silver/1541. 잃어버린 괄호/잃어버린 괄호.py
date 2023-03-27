import sys

input = sys.stdin.readline

line = input().strip()

newstring = ''.join([i for i in line if not i.isdigit()])
operator=list(newstring)
line=line.replace('+','-')

nums = [int(i) for i in line.split('-')]

sum = nums[0]
plus = True
for i in range(0, len(operator)):
  if(operator[i] == '+' and plus == True):
    plus = True
  else:
    plus = False
  if(plus):
    sum+= nums[i+1]
  else:
    sum-= nums[i+1]

print(sum)