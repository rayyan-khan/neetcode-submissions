# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # traverse all the way through the linked list to get the length
        # at the end, start going backwards and reversing it, but retain a 
        # pointer to the new head (the end of the list)
        # when you get to the halfway point, stop reversing
        # from there, insert one element from the reversed linked list
        # after each node in the forward linked list
        length = 1
        forward_pointer = head
        while head.next:
            length += 1
            head = head.next

        # when head does not have next, we are at the end
        # so now we divide the length by 2 and reverse after that point
        backwards_pointer = head
        halfway_point = (length+1) // 2 

        # now time to reverse
        prev = None
        curr = forward_pointer
        next_node = forward_pointer.next
        idx = 0
        last_forward_node = None

        while curr:
            next_node = curr.next
            if idx >= halfway_point: 
                curr.next = prev
                prev = curr  
            else:
                if idx == halfway_point-1:
                    last_forward_node = curr  

            curr = next_node
            idx += 1

        if last_forward_node:
            last_forward_node.next = None

        # at this point, the latter half of the list should be reversed, and also disjoint, so backwards_pointer is our reference to it
        # now we want to zip them together essentially

        head = forward_pointer
        reversed_head = backwards_pointer

        def to_list(n):
            out = []
            while n:
                out.append(n.val)
                n = n.next
            return out

        print(to_list(forward_pointer), to_list(backwards_pointer))
        
        while reversed_head:
            skip = head.next
            next_node = reversed_head.next
            head.next = reversed_head
            reversed_head.next = skip
            head = skip
            reversed_head = next_node

