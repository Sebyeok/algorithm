import sys

input = sys.stdin.readline

n = int(input())

stocknums = []
stocks = []

maxprofit = []

for i in range(0, n):
  stocknums.append(int(input()))
  stocks.append(list(map(int, input().split())))

for i in range(0, n):
  maxprofit.append(0)
  stock = stocks[i]
  maxindex = stock.index(max(stock))
  if (maxindex == 0):
    continue
  for j in stock:
    maxprofit[i] += stock[maxindex] - j
    if (j == stock[maxindex] and maxindex < stocknums[i]-1):
      maxindex = stock.index(max(stock[maxindex + 1:]), maxindex + 1)

for result in maxprofit:
  print(result)