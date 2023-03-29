import sys
from heapq import heappush, heappop 
input = sys.stdin.readline

n = int(input())

tables = [list(map(int, input().split())) for _ in range(n)]

if(n==1):
    print(1)
    exit(0)

tables.sort(key = lambda x: x[0])

heap = []
heappush(heap,tables[0][1])
minimum = tables[0][1]

for table in tables[1:]:
  if(table[0] >= heap[0]):
    heappop(heap)
  heappush(heap, table[1])

print(len(heap))