"""
006 - Circular Linked List Implementation
========================================

This module implements circular linked lists (both singly and doubly):
- Circular Singly Linked List
- Circular Doubly Linked List
- All basic operations adapted for circular structure
- Special traversal methods for circular lists

Time Complexity:
- Access: O(n)
- Search: O(n)
- Insertion: O(1) at known position, O(n) at specific position
- Deletion: O(1) at known position, O(n) at specific position

Advantages:
- No null pointers (except empty list)
- Can start traversal from any node
- Useful for round-robin scheduling
- Memory efficient for cyclic operations
"""

class CircularSinglyListNode:
    """Node class for circular singly linked list"""
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)


class CircularSinglyLinkedList:
    """Circular Singly Linked List implementation"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """Check if the list is empty"""
        return self.head is None
    
    def get_size(self):
        """Return the size of the list"""
        return self.size
    
    def append(self, data):
        """Insert element at the end of the list"""
        new_node = CircularSinglyListNode(data)
        
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head  # Point to itself
        else:
            # Find the last node
            current = self.head
            while current.next != self.head:
                current = current.next
            
            current.next = new_node
            new_node.next = self.head
        
        self.size += 1
    
    def prepend(self, data):
        """Insert element at the beginning of the list"""
        new_node = CircularSinglyListNode(data)
        
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            # Find the last node
            current = self.head
            while current.next != self.head:
                current = current.next
            
            new_node.next = self.head
            current.next = new_node
            self.head = new_node
        
        self.size += 1
    
    def insert_at_position(self, data, position):
        """Insert element at specific position"""
        if position < 0 or position > self.size:
            raise IndexError("Position out of bounds")
        
        if position == 0:
            self.prepend(data)
            return
        
        if position == self.size:
            self.append(data)
            return
        
        new_node = CircularSinglyListNode(data)
        current = self.head
        
        for _ in range(position - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete_first(self):
        """Delete the first element"""
        if self.is_empty():
            raise IndexError("List is empty")
        
        deleted_data = self.head.data
        
        if self.size == 1:
            self.head = None
        else:
            # Find the last node
            current = self.head
            while current.next != self.head:
                current = current.next
            
            current.next = self.head.next
            self.head = self.head.next
        
        self.size -= 1
        return deleted_data
    
    def delete_last(self):
        """Delete the last element"""
        if self.is_empty():
            raise IndexError("List is empty")
        
        if self.size == 1:
            deleted_data = self.head.data
            self.head = None
            self.size -= 1
            return deleted_data
        
        # Find the second last node
        current = self.head
        while current.next.next != self.head:
            current = current.next
        
        deleted_data = current.next.data
        current.next = self.head
        self.size -= 1
        return deleted_data
    
    def delete_at_position(self, position):
        """Delete element at specific position"""
        if position < 0 or position >= self.size:
            raise IndexError("Position out of bounds")
        
        if position == 0:
            return self.delete_first()
        
        current = self.head
        for _ in range(position - 1):
            current = current.next
        
        deleted_data = current.next.data
        current.next = current.next.next
        self.size -= 1
        return deleted_data
    
    def search(self, value):
        """Search for a value and return its position"""
        if self.is_empty():
            return -1
        
        current = self.head
        position = 0
        
        while True:
            if current.data == value:
                return position
            current = current.next
            position += 1
            
            if current == self.head:  # Completed one full circle
                break
        
        return -1
    
    def display(self):
        """Display the circular linked list"""
        if self.is_empty():
            print("List is empty")
            return
        
        elements = []
        current = self.head
        
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        
        print(" -> ".join(elements) + " -> (back to " + str(self.head.data) + ")")
    
    def josephus_problem(self, k):
        """Solve Josephus problem with step size k"""
        if self.is_empty() or k <= 0:
            return []
        
        eliminated_order = []
        current = self.head
        
        while self.size > 0:
            # Move k-1 steps
            for _ in range(k - 1):
                current = current.next
            
            # Store the eliminated person
            eliminated_order.append(current.data)
            
            # Remove current node
            if self.size == 1:
                self.head = None
                self.size = 0
            else:
                # Find previous node
                prev = current
                while prev.next != current:
                    prev = prev.next
                
                if current == self.head:
                    self.head = current.next
                
                prev.next = current.next
                current = current.next
                self.size -= 1
        
        return eliminated_order


class CircularDoublyListNode:
    """Node class for circular doubly linked list"""
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.data)


class CircularDoublyLinkedList:
    """Circular Doubly Linked List implementation"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """Check if the list is empty"""
        return self.head is None
    
    def get_size(self):
        """Return the size of the list"""
        return self.size
    
    def append(self, data):
        """Insert element at the end of the list"""
        new_node = CircularDoublyListNode(data)
        
        if self.is_empty():
            self.head = new_node
            new_node.next = new_node.prev = new_node
        else:
            last = self.head.prev
            
            new_node.next = self.head
            new_node.prev = last
            last.next = new_node
            self.head.prev = new_node
        
        self.size += 1
    
    def prepend(self, data):
        """Insert element at the beginning of the list"""
        new_node = CircularDoublyListNode(data)
        
        if self.is_empty():
            self.head = new_node
            new_node.next = new_node.prev = new_node
        else:
            last = self.head.prev
            
            new_node.next = self.head
            new_node.prev = last
            last.next = new_node
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1
    
    def delete_first(self):
        """Delete the first element"""
        if self.is_empty():
            raise IndexError("List is empty")
        
        deleted_data = self.head.data
        
        if self.size == 1:
            self.head = None
        else:
            last = self.head.prev
            second = self.head.next
            
            last.next = second
            second.prev = last
            self.head = second
        
        self.size -= 1
        return deleted_data
    
    def delete_last(self):
        """Delete the last element"""
        if self.is_empty():
            raise IndexError("List is empty")
        
        if self.size == 1:
            deleted_data = self.head.data
            self.head = None
            self.size -= 1
            return deleted_data
        
        last = self.head.prev
        deleted_data = last.data
        second_last = last.prev
        
        second_last.next = self.head
        self.head.prev = second_last
        
        self.size -= 1
        return deleted_data
    
    def display_forward(self):
        """Display the list in forward direction"""
        if self.is_empty():
            print("List is empty")
            return
        
        elements = []
        current = self.head
        
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        
        print("Forward: " + " <-> ".join(elements) + " <-> (circular)")
    
    def display_backward(self):
        """Display the list in backward direction"""
        if self.is_empty():
            print("List is empty")
            return
        
        elements = []
        current = self.head.prev
        
        while True:
            elements.append(str(current.data))
            current = current.prev
            if current == self.head.prev:
                break
        
        print("Backward: " + " <-> ".join(elements) + " <-> (circular)")


def test_circular_linked_lists():
    """Test circular linked list implementations"""
    print("=== Testing Circular Singly Linked List ===\n")
    
    # Test Circular Singly Linked List
    csll = CircularSinglyLinkedList()
    
    print("Testing insertion operations:")
    csll.append(10)
    csll.append(20)
    csll.append(30)
    csll.prepend(5)
    csll.display()
    print(f"Size: {csll.get_size()}")
    print()
    
    print("Testing search operation:")
    position = csll.search(20)
    print(f"Position of 20: {position}")
    print()
    
    print("Testing insertion at position 2:")
    csll.insert_at_position(15, 2)
    csll.display()
    print()
    
    print("Testing deletion operations:")
    deleted = csll.delete_first()
    print(f"Deleted first: {deleted}")
    csll.display()
    
    deleted = csll.delete_last()
    print(f"Deleted last: {deleted}")
    csll.display()
    
    deleted = csll.delete_at_position(1)
    print(f"Deleted at position 1: {deleted}")
    csll.display()
    print()
    
    # Test Josephus Problem
    print("=== Testing Josephus Problem ===")
    josephus_list = CircularSinglyLinkedList()
    for i in range(1, 8):  # People numbered 1 to 7
        josephus_list.append(i)
    
    print("Initial circle:")
    josephus_list.display()
    
    k = 3  # Every 3rd person is eliminated
    eliminated_order = josephus_list.josephus_problem(k)
    print(f"Elimination order with k={k}: {eliminated_order}")
    print()
    
    # Test Circular Doubly Linked List
    print("=== Testing Circular Doubly Linked List ===\n")
    
    cdll = CircularDoublyLinkedList()
    
    print("Testing insertion operations:")
    cdll.append(100)
    cdll.append(200)
    cdll.append(300)
    cdll.prepend(50)
    cdll.display_forward()
    cdll.display_backward()
    print(f"Size: {cdll.get_size()}")
    print()
    
    print("Testing deletion operations:")
    deleted = cdll.delete_first()
    print(f"Deleted first: {deleted}")
    cdll.display_forward()
    
    deleted = cdll.delete_last()
    print(f"Deleted last: {deleted}")
    cdll.display_forward()
    print()
    
    # Performance comparison
    print("=== Performance Notes ===")
    print("Circular lists advantages:")
    print("1. No null pointer checks needed during traversal")
    print("2. Can start traversal from any node")
    print("3. Useful for implementing round-robin algorithms")
    print("4. Memory efficient for cyclic operations")
    print("5. Both ends are accessible in O(1) for doubly circular list")


if __name__ == "__main__":
    test_circular_linked_lists()
