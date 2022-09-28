# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        prev = None
        for i in range (n):
            fast = fast.next
            
        while fast != None:
            prev = slow
            fast = fast.next
            slow = slow.next
            
        if prev == None:
            head = head.next
            return head
        else :
            prev.next = slow.next
            return head
        