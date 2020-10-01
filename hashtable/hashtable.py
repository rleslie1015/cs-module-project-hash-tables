from notes.LinkedList import LinkedList

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'( {self.key} - {self.value} )'
# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY):
        # Your code here
        self.capacity = capacity 
        self.storage = [None] * capacity
        self.number_of_elements = 0

    def __repr__(self):
        str1 = ''
        for i in range(len(self.storage)):
            str1 += f'( {i} : {str(self.storage[i])} ) \n'
        return str1

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        lf = self.number_of_elements / self.get_num_slots()
        return lf


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        byte_arr = key.encode('utf-8')
        # print('byte', byte_arr)
        for byte in byte_arr:
        # the modulus keeps it 32-bit, python ints don't overflow
            hash = ((hash * 33) ^ byte) % 0x100000000
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
## automatic rehashing

        print('load factor ', self.get_load_factor())
        if self.get_load_factor() >= 0.7:
            print('warning load factor is: ', self.get_load_factor())
            self.resize(self.capacity*2)
            print('resizing to: ', self.get_load_factor())

##   get the index for the key
        index = self.hash_index(key)
        # create a new entry
        new_entry = HashTableEntry(key, value)
##     search the linked list at the index for the key
        # reference the item or linked list at the index
        slot = self.storage[index]
        # if there is nothing at the index create a LL and insert the entry at head
##           insert the key and value at the head of the list at that index
        if slot is None:
            ll = LinkedList()
            ll.insert_at_head(new_entry)
            # assign the LL at the right index
            self.storage[index] = ll
            self.number_of_elements += 1
        # else if there is already something at the hash_index
        else: 
##     if the key is found, overwrite the value stored there
            if slot.find_by_key(key) is not None:
                slot.find_by_key(key).value = value
            else:
                # if not then add entry to head
                slot.insert_at_head(new_entry)
                self.number_of_elements += 1



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # get the index
        index = self.hash_index(key)
        # find the entry by key
        entry = self.storage[index].find_by_key(key)
        
        value = None # value to return 
        # if key exists in the LL 
        if entry:

            # update number of elements 
            self.number_of_elements -= 1
            # delete the value using LL delete method
            self.storage[index].delete(entry.value)
            value = entry.value
        return value

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        # find by key
        entry = (self.storage[index].find_by_key(key))
        # if exists return value
        if entry: 
            return entry.value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # # Your code here
        # store the current values
        # ll = LinkedList()
        old_storage = self.storage
        # make new array with new_capacity
        new_array = [None] * new_capacity
        # replace self.storage
        self.storage = new_array
        # loop through all LL in old_storage 
        for entry in old_storage:
            if entry is None:
                continue
            current = entry.head
            while current is not None:
                # insert each item into new_array
                self.put(current.key, current.value)
                current = current.next
        


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")

    # print("")

    # # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")
