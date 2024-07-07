import heapq

class Solution(object):
    def mergeKLists(self, lists):
        min_heap = []
        
        for head in lists:
            if head:
                heapq.heappush(min_heap, (head.val, head))
        
        dummy = ListNode()
        current = dummy
        
        while min_heap:
            val, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, node.next))
        
        return dummy.next
