n, price = map(int, input().split())
coins = []
count = 0
for i in range(0,n) :
  coins.append(int(input()))

coins.reverse()

for coin in coins:
  if(price // coin > 0):
    count += price // coin
    price %= coin

print(count)