"""
In-place Reversal of LinkedList Pattern
=======================================

Reverse linked list or parts of it in-place.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class ListNode:
    """Simple linked list node"""
    def __init__(self, val=0):
        self.val = val
        self.next = None


def reverse_linkedlist(head):
    """
    Reverse entire linked list in-place.
    
    Args:
        head: Head of the linked list
        
    Returns:
        New head of reversed list
    """
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev


def reverse_sublist(head, p, q):
    """
    Reverse sublist from position p to q.
    
    Args:
        head: Head of linked list
        p: Start position (1-indexed)
        q: End position (1-indexed)
        
    Returns:
        Head of modified list
    """
    if p == q:
        return head
    
    # Skip p-1 nodes
    current = head
    prev = None
    for _ in range(p - 1):
        prev = current
        current = current.next
    
    # Store connections
    last_node_first_part = prev
    last_node_sublist = current
    
    # Reverse sublist
    for _ in range(q - p + 1):
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    # Connect with first part
    if last_node_first_part:
        last_node_first_part.next = prev
    else:
        head = prev
    
    # Connect with last part
    last_node_sublist.next = current
    
    return head


def reverse_every_k_elements(head, k):
    """
    Reverse every k elements in the linked list.
    
    Args:
        head: Head of linked list
        k: Group size to reverse
        
    Returns:
        Head of modified list
    """
    if k <= 1 or not head:
        return head
    
    current = head
    prev = None
    
    while True:
        last_node_prev_part = prev
        last_node_sub_list = current
        
        # Reverse k nodes
        for _ in range(k):
            if not current:
                break
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        # Connect with previous part
        if last_node_prev_part:
            last_node_prev_part.next = prev
        else:
            head = prev
        
        # Connect with next part
        last_node_sub_list.next = current
        
        if not current:
            break
        
        prev = last_node_sub_list
    
    return head


def print_list(head):
    """Helper function to print linked list"""
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    return " -> ".join(result)


def create_list(values):
    """Helper function to create linked list from values"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head


def example_usage():
    """Demonstrate linked list reversal operations"""
    # Reverse entire list
    head = create_list([1, 2, 3, 4, 5])
    print("Original:", print_list(head))
    
    reversed_head = reverse_linkedlist(head)
    print("Reversed:", print_list(reversed_head))
    
    # Reverse sublist
    head = create_list([1, 2, 3, 4, 5])
    reversed_sub = reverse_sublist(head, 2, 4)
    print("Reverse sublist (2-4):", print_list(reversed_sub))
    
    # Reverse every k elements
    head = create_list([1, 2, 3, 4, 5, 6, 7, 8])
    reversed_k = reverse_every_k_elements(head, 3)
    print("Reverse every 3 elements:", print_list(reversed_k))


if __name__ == "__main__":
    example_usage()
