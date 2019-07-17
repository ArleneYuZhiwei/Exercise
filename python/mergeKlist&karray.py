k-arrays:
import heapq

class Solution:
    # @param {int[][]} arrays k sorted integer arrays
    # @return {int[]} a sorted array
    def mergekSortedArrays(self, arrays):
        # Write your code here
        result = []
        heap = []
        for index, array in enumerate(arrays):
            if len(array) == 0:
                continue
            heapq.heappush(heap, (array[0], index, 0))
             
        while len(heap):
            val, arrayNum, index = heapq.heappop(heap)
            result.append(val)
            if index + 1 < len(arrays[arrayNum]):
                heapq.heappush(heap, (arrays[arrayNum][index + 1], arrayNum, index + 1))
            
        return result
        
merge k-lists:
import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        prev=ListNode(-1)
        now=prev
        heap=[]
        for i in lists:
            if i:
                heapq.heappush(heap,[i.val,i])

        while heap:
            item=heapq.heappop(heap)
            now.next=item[1]
            now = now.next
            item[1]=item[1].next
            if (item[1]):
                item[0]=item[1].val
                heapq.heappush(heap, item)
        return prev.next
