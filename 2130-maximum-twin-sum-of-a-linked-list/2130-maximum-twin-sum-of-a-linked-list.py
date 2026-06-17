# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        def reverseList(head1):
            if head1 is None or head1.next is None:
                return head1
            temp=reverseList(head1.next)
            head1.next.next=head1
            head1.next=None
            return temp
        head1=ListNode(0)
        dummy=head1
        temp=head
        while temp:
            dummy.next=ListNode(temp.val)
            temp=temp.next
            dummy=dummy.next
        temp=reverseList(head1.next)
        res=0
        while(head):
            res=max(res,head.val+temp.val)
            head=head.next
            temp=temp.next
        return res