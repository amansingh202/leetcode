# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Base cases
        if not l1:
            return l2
        if not l2:
            return l1
        
        # Compare values of the current nodes of l1 and l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# Example usage
solution = Solution()

# Create example linked lists
# Create list1: ListNode(1 -> 2 -> 4)
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# Create list2: ListNode(1 -> 3 -> 4)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# Merge the lists
result = solution.mergeTwoLists(list1, list2)

# Function to convert ListNode to list (for printing purposes)
def list_from_linked_list(head: Optional[ListNode]) -> list:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Print the merged list (converted from ListNode to list)
print(list_from_linked_list(result))
