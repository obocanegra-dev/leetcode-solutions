class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy_head = ListNode()
        current = dummy_head
        p1, p2 = list1, list2
        
        while p1 and p2:
            if p1.val <= p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
        
        if p1:
            current.next = p1
        elif p2:
            current.next = p2
        
        return dummy_head.next
