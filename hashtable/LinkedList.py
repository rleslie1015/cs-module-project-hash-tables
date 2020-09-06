class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        currStr = ""
        curr = self.head
        while curr is not None:
            currStr += f'{str(curr.value)} -> '
            curr = curr.next
        return currStr

    # Runtime: O(1)
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    # Runtime O(number of nodes)
    def insert_at_head_or_overwrite(self, node):
        # node = Node(value)
        existingNode = self.find(node.value)
        if existingNode is not None:
            existingNode.value = node.value
        else:
            self.insert_at_head(node)

    # Runtime: O(number of nodes)
    # Space: O(1)
    def delete(self, value):
        curr = self.head

        if curr.value == value:
            self.head = curr.next
            return curr

        prev = curr
        curr = curr.next

        while curr is not None:
            if curr.value == value:
                prev.next = curr.next
                curr.next = None
                return curr
            else:
                prev = curr
                curr = curr.next

        return None

    # Runtime: O(number of nodes)
    def find(self, value):
        curr = self.head
        while curr is not None:
            if curr.value == value:
                return curr
            curr = curr.next
        return None
    
    def find_by_key(self, key):
        curr = self.head
        while curr is not None:
            if curr.key == key:
                return curr
            curr = curr.next
        return None 
