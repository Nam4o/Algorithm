import heapq, sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    min_heap, max_heap, in_heap = [], [], set()

    for _ in range(k):
        op, num = input().split()
        num = int(num)

        if op == "I":
            heapq.heappush(min_heap, (num, _))
            heapq.heappush(max_heap, (-num, _))
            in_heap.add(_)
        else:
            if num == -1:
                while min_heap and min_heap[0][1] not in in_heap:
                    heapq.heappop(min_heap)
                if min_heap:
                    in_heap.remove(min_heap[0][1])
                    heapq.heappop(min_heap)
            else:
                while max_heap and max_heap[0][1] not in in_heap:
                    heapq.heappop(max_heap)
                if max_heap:
                    in_heap.remove(max_heap[0][1])
                    heapq.heappop(max_heap)

    while min_heap and min_heap[0][1] not in in_heap:
        heapq.heappop(min_heap)
    while max_heap and max_heap[0][1] not in in_heap:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
