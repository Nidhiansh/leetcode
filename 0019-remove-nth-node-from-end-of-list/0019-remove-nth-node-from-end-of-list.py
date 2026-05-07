# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev=None
        current=head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        head=prev
        return head
    def removeNthFromEnd(self, head, n):
        head=self.reverseList(head)
        if n==1:
            head=head.next
        else:
            temp=head
            for i in range(n-2):
                temp=temp.next
            temp.next=temp.next.next
        head=self.reverseList(head)
        return head
    