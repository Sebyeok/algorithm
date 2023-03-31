import sys
from heapq import heappush, heappop 
input = sys.stdin.readline

n, m = map(int,input().split())

inputs = list(map(int, input().split()))
cards = []

for input in inputs:
  heappush(cards, input)

for i in range(m):
  a = heappop(cards)
  b = heappop(cards)
  heappush(cards, a+b)
  heappush(cards, a+b)

print(sum(cards))