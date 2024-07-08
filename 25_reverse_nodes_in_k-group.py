class Solution(object):
    def reverseKGroup(self, head, k):
        def reverseLinkedList(head, k):
            prev = None
            curr = head
            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev, head
        
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head:
            tail = prev
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next 
            
            next_head = tail.next
            reversed_head, reversed_tail = reverseLinkedList(head, k)
            
            prev.next = reversed_head
            reversed_tail.next = next_head
            
            prev = reversed_tail
            head = next_head
        
        return dummy.next
