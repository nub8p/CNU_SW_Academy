import heapq

prision = int(input())
prisions = list(map(int, input().split()))

lighter = int(input())
lighters = list(map(int, input().split()))

max_heap = []
for p in prisions:
    min_heap = []
    for l in lighters:
        heapq.heappush(min_heap, abs(p - l))
    heapq.heappush(max_heap, -heapq.heappop(min_heap))

print(-heapq.heappop(max_heap))
