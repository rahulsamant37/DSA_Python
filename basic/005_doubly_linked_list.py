"""
005 - Doubly Linked List Implementation
======================================

This module implements a doubly linked list with all basic operations:
- Node creation with previous and next pointers
- Insertion (at beginning, end, and specific position)
- Deletion (from beginning, end, and specific position)
- Forward and backward traversal
- Search operations
- Utility functions

Time Complexity:
- Access: O(n)
- Search: O(n)
- Insertion: O(1) at beginning/end, O(n) at position
- Deletion: O(1) at beginning/end, O(n) at position

Advantages over Singly Linked List:
- Bidirectional traversal
- Easier deletion of a given node
- Easier to implement certain algorithms
"""

class DoublyListNode:
    """Node class for doubly linked list"""
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    """Doubly Linked List implementation"""
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        """Check if the linked list is empty"""
        return self.head is None
    
    def get_size(self):
        """Return the size of the linked list"""
        return self.size
    
    def prepend(self, data):
        """Insert element at the beginning of the list"""
        new_node = DoublyListNode(data)
        
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1
    
    def append(self, data):
        """Insert element at the end of the list"""
        new_node = DoublyListNode(data)
        
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
    
    def insert_at_position(self, data, position):
        """Insert element at specific position (0-indexed)"""
        if position < 0 or position > self.size:
            raise IndexError("Position out of bounds")
        
        if position == 0:
            self.prepend(data)
            return
        
        if position == self.size:
            self.append(data)
            return
        
        new_node = DoublyListNode(data)
        
        # Decide whether to traverse from head or tail
        if position <= self.size // 2:
            # Traverse from head
            current = self.head
            for _ in range(position):
                current = current.next
        else:
            # Traverse from tail
            current = self.tail
            for _ in range(self.size - position - 1):
                current = current.prev
        
        # Insert the new node
        new_node.next = current
        new_node.prev = current.prev
        current.prev.next = new_node
        current.prev = new_node
        
        self.size += 1
    
    def delete_first(self):
        """Delete the first element"""
        if self.is_empty():
            raise IndexError("List is empty")
        
        deleted_data = self.head.data
        
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        self.size -= 1
        return deleted_data
    
    def delete_last(self):
        """Delete the last element"""
        if self.is_empty():
            raise IndexError("List is empty")
        
        deleted_data = self.tail.data
        
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        self.size -= 1
        return deleted_data
    
    def delete_at_position(self, position):
        """Delete element at specific position"""
        if position < 0 or position >= self.size:
            raise IndexError("Position out of bounds")
        
        if position == 0:
            return self.delete_first()
        
        if position == self.size - 1:
            return self.delete_last()
        
        # Decide whether to traverse from head or tail
        if position <= self.size // 2:
            # Traverse from head
            current = self.head
            for _ in range(position):
                current = current.next
        else:
            # Traverse from tail
            current = self.tail
            for _ in range(self.size - position - 1):
                current = current.prev
        
        deleted_data = current.data
        current.prev.next = current.next
        current.next.prev = current.prev
        
        self.size -= 1
        return deleted_data
    
    def delete_node(self, node):
        """Delete a specific node (given node reference)"""
        if node is None:
            return False
        
        if node == self.head:
            self.delete_first()
        elif node == self.tail:
            self.delete_last()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
        
        return True
    
    def delete_by_value(self, value):
        """Delete first occurrence of value"""
        current = self.head
        
        while current:
            if current.data == value:
                self.delete_node(current)
                return True
            current = current.next
        
        return False
    
    def search(self, value):
        """Search for a value and return its position"""
        current = self.head
        position = 0
        
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        
        return -1
    
    def search_from_tail(self, value):
        """Search for a value from tail and return its position from head"""
        current = self.tail
        position = self.size - 1
        
        while current:
            if current.data == value:
                return position
            current = current.prev
            position -= 1
        
        return -1
    
    def get_at_position(self, position):
        """Get element at specific position"""
        if position < 0 or position >= self.size:
            raise IndexError("Position out of bounds")
        
        # Optimize by choosing direction
        if position <= self.size // 2:
            # Traverse from head
            current = self.head
            for _ in range(position):
                current = current.next
        else:
            # Traverse from tail
            current = self.tail
            for _ in range(self.size - position - 1):
                current = current.prev
        
        return current.data
    
    def update_at_position(self, position, new_value):
        """Update element at specific position"""
        if position < 0 or position >= self.size:
            raise IndexError("Position out of bounds")
        
        # Optimize by choosing direction
        if position <= self.size // 2:
            # Traverse from head
            current = self.head
            for _ in range(position):
                current = current.next
        else:
            # Traverse from tail
            current = self.tail
            for _ in range(self.size - position - 1):
                current = current.prev
        
        old_value = current.data
        current.data = new_value
        return old_value
    
    def reverse(self):
        """Reverse the doubly linked list"""
        if self.is_empty() or self.size == 1:
            return
        
        current = self.head
        
        while current:
            # Swap next and prev pointers
            current.next, current.prev = current.prev, current.next
            current = current.prev  # Move to next node (which is now prev)
        
        # Swap head and tail
        self.head, self.tail = self.tail, self.head
    
    def find_middle(self):
        """Find the middle element using two pointers"""
        if self.is_empty():
            return None
        
        slow = fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
    
    def display_forward(self):
        """Display the linked list from head to tail"""
        if self.is_empty():
            print("List is empty")
            return
        
        elements = []
        current = self.head
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print("Forward: " + " <-> ".join(elements))
    
    def display_backward(self):
        """Display the linked list from tail to head"""
        if self.is_empty():
            print("List is empty")
            return
        
        elements = []
        current = self.tail
        
        while current:
            elements.append(str(current.data))
            current = current.prev
        
        print("Backward: " + " <-> ".join(elements))
    
    def display(self):
        """Display the linked list in both directions"""
        self.display_forward()
        self.display_backward()
    
    def to_list(self):
        """Convert linked list to Python list"""
        result = []
        current = self.head
        
        while current:
            result.append(current.data)
            current = current.next
        
        return result
    
    def from_list(self, python_list):
        """Create linked list from Python list"""
        self.head = self.tail = None
        self.size = 0
        
        for item in python_list:
            self.append(item)
    
    def merge_sorted(self, other_list):
        """Merge two sorted doubly linked lists"""
        dummy = DoublyListNode(0)
        current = dummy
        
        ptr1, ptr2 = self.head, other_list.head
        
        while ptr1 and ptr2:
            if ptr1.data <= ptr2.data:
                current.next = ptr1
                ptr1.prev = current
                ptr1 = ptr1.next
            else:
                current.next = ptr2
                ptr2.prev = current
                ptr2 = ptr2.next
            current = current.next
        
        # Attach remaining elements
        if ptr1:
            current.next = ptr1
            ptr1.prev = current
        elif ptr2:
            current.next = ptr2
            ptr2.prev = current
        
        # Create new merged list
        merged_list = DoublyLinkedList()
        merged_list.head = dummy.next
        if merged_list.head:
            merged_list.head.prev = None
        
        # Find tail
        current = merged_list.head
        while current and current.next:
            current = current.next
        merged_list.tail = current
        
        merged_list.size = self.size + other_list.size
        
        return merged_list


def test_doubly_linked_list():
    """Test all doubly linked list operations"""
    print("=== Testing Doubly Linked List ===\n")
    
    # Create empty list
    dll = DoublyLinkedList()
    print(f"Created empty list. Size: {dll.get_size()}")
    print(f"Is empty: {dll.is_empty()}")
    dll.display()
    print()
    
    # Test insertion operations
    print("=== Insertion Operations ===")
    print("Appending elements: 10, 20, 30")
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.display()
    print(f"Size: {dll.get_size()}")
    print()
    
    print("Prepending element: 5")
    dll.prepend(5)
    dll.display()
    print()
    
    print("Inserting 15 at position 2:")
    dll.insert_at_position(15, 2)
    dll.display()
    print(f"Size: {dll.get_size()}")
    print()
    
    # Test search operations
    print("=== Search Operations ===")
    search_value = 20
    position = dll.search(search_value)
    print(f"Position of {search_value} (from head): {position}")
    
    position_tail = dll.search_from_tail(search_value)
    print(f"Position of {search_value} (from tail): {position_tail}")
    
    print(f"Element at position 3: {dll.get_at_position(3)}")
    print(f"Middle element: {dll.find_middle()}")
    print()
    
    # Test update operation
    print("=== Update Operation ===")
    old_value = dll.update_at_position(1, 25)
    print(f"Updated position 1 from {old_value} to 25")
    dll.display()
    print()
    
    # Test deletion operations
    print("=== Deletion Operations ===")
    deleted = dll.delete_first()
    print(f"Deleted first element: {deleted}")
    dll.display()
    print()
    
    deleted = dll.delete_last()
    print(f"Deleted last element: {deleted}")
    dll.display()
    print()
    
    deleted = dll.delete_at_position(1)
    print(f"Deleted element at position 1: {deleted}")
    dll.display()
    print()
    
    success = dll.delete_by_value(20)
    print(f"Deleted value 20: {success}")
    dll.display()
    print(f"Final size: {dll.get_size()}")
    print()
    
    # Test reverse operation
    print("=== Reverse Operations ===")
    dll.from_list([1, 2, 3, 4, 5])
    print("Original list:")
    dll.display()
    print()
    
    dll.reverse()
    print("After reversing:")
    dll.display()
    print()
    
    # Test merge operation
    print("=== Merge Operation ===")
    list1 = DoublyLinkedList()
    list1.from_list([1, 3, 5])
    print("List 1:")
    list1.display_forward()
    
    list2 = DoublyLinkedList()
    list2.from_list([2, 4, 6])
    print("List 2:")
    list2.display_forward()
    
    merged = list1.merge_sorted(list2)
    print("Merged list:")
    merged.display_forward()
    print()
    
    # Performance comparison with access
    print("=== Performance Test: Access from both ends ===")
    large_dll = DoublyLinkedList()
    large_dll.from_list(list(range(1000)))
    
    import time
    
    # Access from beginning
    start = time.time()
    val = large_dll.get_at_position(100)
    time_beginning = time.time() - start
    
    # Access from end
    start = time.time()
    val = large_dll.get_at_position(900)
    time_end = time.time() - start
    
    print(f"Access position 100 (near beginning): {time_beginning:.6f}s")
    print(f"Access position 900 (near end): {time_end:.6f}s")
    print("Note: Doubly linked list optimizes access by choosing direction")


if __name__ == "__main__":
    test_doubly_linked_list()
