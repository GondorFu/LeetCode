# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        rlt = p = ListNode(0)
        while l1 or l2 or carry:
            v1 =  v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            p.next = ListNode(val)
            p = p.next
        return rlt.next

    def reverse(self, l):
        '''
        reverse the linked list
        '''
        if l == None or l.next == None:
            return l
        rlt = self.reverse(l.next)
        l.next.next = l
        l.next = None
        return rlt