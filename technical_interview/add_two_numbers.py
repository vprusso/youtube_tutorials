# YouTube Video: 
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        node = head
        carryOver = 0
        while True:
            value1 = l1.val if l1 is not None else 0
            value2 = l2.val if l2 is not None else 0
            node.val = (value1+value2+carryOver) % 10
            carryOver = (value1+value2+carryOver)/10
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            if l1 or l2:
                node.next = ListNode(0)
                node = node.next
            else:
                break
        if carryOver:
            node.next = ListNode(1)
        return head
