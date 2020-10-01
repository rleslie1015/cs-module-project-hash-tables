class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'Node({repr(self.value)})'
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def __str__(self):
        r = ""
        # traverse the list
        cur = self.head
        while cur is not None:
            r += f'{cur.value} '

            if cur.next is not None:
                r += ' -> '
            cur = cur.next 

        return r
    
    def find(self, value):
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return cur
            
            cur = cur.next
        return None

    def delete(self, value):
        if self.head is None:
            return None

        if self.head.value == value:
           old_head = self.head
           self.head = self.head.next
           old_head.next = None
           return old_head

        # general
        prev = self.head
        cur = self.head.next

        while cur is not None:
            if cur.value == value:
                prev.next = cur.next
                cur.next = None
                return cur
            prev = prev.next
            cur = cur.next
        
        # if we get here,  we didn't find it
        return None




ll = LinkedList()

ll.insert_at_head(Node(10))
ll.insert_at_head(Node(20))
ll.insert_at_head(Node(30))
ll.insert_at_head(Node(40))
ll.insert_at_head(Node(50))
ll.insert_at_head(Node(60))
ll.insert_at_head(Node(70))

print(ll)
print(ll.delete(20))
ll.delete(70)
print(ll)
