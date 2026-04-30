# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k==0:
            return head
        curr,l=head,1
        while curr.next:
            curr=curr.next
            l+=1
        curr.next=head
        k%=l
        for _ in range(l-k):
            curr=curr.next
        new_head=curr.next
        curr.next=None
        return new_head