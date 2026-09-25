# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        firstNode = secondNode = dummy 
        for i in range(n+1):
            firstNode = firstNode.next
        while firstNode:
            firstNode = firstNode.next
            secondNode = secondNode.next
        secondNode.next = secondNode.next.next
        return dummy.next
        