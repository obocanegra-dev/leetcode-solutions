class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode()
        current = dummy_head
        carry = 0
        
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            sum = x + y + carry
            carry = sum // 10  
            current.next = ListNode(sum % 10)
            current = current.next 
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry > 0:
            current.next = ListNode(carry)
        
        return dummy_head.next
