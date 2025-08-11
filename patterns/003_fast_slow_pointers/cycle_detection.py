"""
Fast & Slow Pointers Pattern - Cycle Detection
===============================================

Detect cycle in a linked list using Floyd's algorithm.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class ListNode:
    """Simple linked list node for demonstration"""
    def __init__(self, val=0):
        self.val = val
        self.next = None


def has_cycle(head):
    """
    Detect if linked list has a cycle using fast & slow pointers.
    
    Args:
        head: Head of the linked list
        
    Returns:
        True if cycle exists, False otherwise
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next        # Move slow pointer by 1
        fast = fast.next.next   # Move fast pointer by 2
        
        if slow == fast:        # Cycle detected
            return True
    
    return False


def find_cycle_start(head):
    """
    Find the start of the cycle in a linked list.
    
    Args:
        head: Head of the linked list
        
    Returns:
        Node where cycle starts, or None if no cycle
    """
    if not has_cycle(head):
        return None
    
    # Find meeting point
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    # Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow


def cycle_length(head):
    """
    Find the length of the cycle in a linked list.
    
    Args:
        head: Head of the linked list
        
    Returns:
        Length of cycle, or 0 if no cycle
    """
    if not has_cycle(head):
        return 0
    
    # Find meeting point
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    # Count cycle length
    current = slow
    length = 0
    while True:
        current = current.next
        length += 1
        if current == slow:
            break
    
    return length


def example_usage():
    """Demonstrate cycle detection"""
    # Create a linked list with cycle: 1 -> 2 -> 3 -> 4 -> 2 (cycle)
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next  # Create cycle
    
    print(f"Has cycle: {has_cycle(head)}")
    
    cycle_start = find_cycle_start(head)
    print(f"Cycle starts at node with value: {cycle_start.val}")
    
    print(f"Cycle length: {cycle_length(head)}")


if __name__ == "__main__":
    example_usage()
