import sys

input = sys.stdin.readline

str = input()
check = str[0]
newstr = []
for i in range(0,len(str)):
  if(str[i] == check):
    continue
  else:
    newstr.append(check)
    check = str[i]
    
print(min(newstr.count("0"),newstr.count("1")))