# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head: return None
        oddh=oddt=ListNode(0)
        evenh=event=ListNode(0)
        i=1
        curr=head
        while curr:
            if i%2==0:
                event.next=curr
                event=event.next
            else:
                oddt.next=curr
                oddt=oddt.next
            curr=curr.next
            i+=1
        event.next=None
        oddt.next=evenh.next
        return oddh.next