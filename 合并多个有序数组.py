'''
多个有序数组 合并成一个有序数组

'''
import heapq
from collections import deque
def  slove(lists):

    #转换的目的是为了方便从左边pop  list只有pop
    deques = [d for d in map(deque,lists)]

    heap =[]

    for index,de in enumerate(deques):
        heap.append((de.popleft(),index))

#转成最小堆
    heapq.heapify(heap)

    result = []

    while heap:
        re,ind = heapq.heappop(heap)
        result.append(re)
        if deques[ind]:
            heapq.heappush(heap,(deques[ind].popleft(),ind))
    return result

print(slove([[4,8,10],[100,200,300,370],[5,8,100,2000]]))
