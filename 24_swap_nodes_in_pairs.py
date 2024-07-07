class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            curr = prev.next
            next_start = curr.next
            
            prev.next = next_start
            curr.next = next_start.next
            next_start.next = curr
            
            prev = curr
         
        return dummy.next
