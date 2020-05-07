class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.head = None
      
class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
   
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.size = 0
      
    
    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        hash_ = 14695981039346656037
        for k in key:
            hash_ = hash_ ^ ord(k)
            hash_ = hash_ * 1099511628211
            hash_ &= 0xffffffffffffffff 
        return hash_    
    
    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash_ = 5381
        for k in key:
            hash_ = (hash_*33) + ord(k)
            hash_ &= 0xffffffff
        return hash_    
    
    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        Modify this to handle chaining for collision Resolution
        STEPS:
            Put()
            Find the hash index
            Search the list for the key

            If it's there, replace the value
            If it's not, append a new record to the list
        """
        index = self.hash_index(key)
        current = self.storage[index]
        
        if current is None:
            self.storage[index] = HashTableEntry(key, value)
            self.size += 1
            self.adjust_load_factor()
            return
        if current.key == key:
            current.value = value
            return    
        while current.key != key:
            if current.next is None:
                current.next = HashTableEntry(key, value)
                self.size += 1
                self.adjust_load_factor()
                return
            current = current.next
            if current.key == key:
                current.value = value  
                return


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        Modify this to handle chaining for collision Resolution
        STEPS:
            Delete()
            Find the hash index
            Search the list for the key
            If found, delete the node from the list, (return the node or value?)
            Else return None
        """
        index = self.hash_index(key)
        current = self.storage[index]

        if current is None or self.size == 0:
            return None

        if current.next is None:
            if current.key == key:
                deleted_val = current.value
                self.storage[index] = None
                self.size -= 1
                self.adjust_load_factor()
                return deleted_val
            else:
                return None    

        prev = None

        while current:
              
            if current.key == key:
                deleted_val = current.value
                self.size -= 1
                current.key = None
                prev.next = current.next
                self.adjust_load_factor()
                return deleted_val
            prev = current    
            current = current.next
        return None    



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        Modify this to handle chaining for collision Resolution
        STEPS:
            Get()
            Find the hash index
            Search the list for the key
            If found, return the value
            Else return None
        """
        index = self.hash_index(key)
        current = self.storage[index]
        if current is None:
            return None
        while current.key !=key:
            if current.next is None:
                return None
            current = current.next
        return current.value


    def adjust_load_factor(self):
        load_factor = self.size/self.capacity
        if load_factor > 0.7:
            self.resize(self.capacity*2)

        elif load_factor < 0.2 and self.capacity > 8:
            half = load_factor//2
            self.resize(load_factor//2)
                    



    def resize(self,new_capacity):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity
        self.capacity = max((self.capacity),8)
        new_storage = [None]*self.capacity
        for node in self.storage:
            if node != None:
                hashed_key=self.hash_index(node.key)
                new_storage[hashed_key] = node
            self.storage = new_storage    
         

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    new_capacity = len(ht.storage)*2
    ht.resize(new_capacity)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
