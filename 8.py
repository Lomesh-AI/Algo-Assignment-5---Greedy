import heapq

n = int(input())
arr = list(map(int, input().split(' ')))

min_heap = []

health = 0

for i in range(n):
    health += arr[i]
    heapq.heappush(min_heap, arr[i])
    if health < 0:
        last = heapq.heappop(min_heap)
        health -= last

print(len(min_heap))