class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` number buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity if capacity >= 8 else MIN_CAPACITY
        self.storage = [None] * capacity



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
        full_nodes = 0
        for node in self.storage:
            if isinstance(node, HashTableEntry):
                full_nodes += 1
            else:
                pass
        return (self.capacity - full_nodes)/self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # Your code here
        # FNV_offset_basis = 14695981039346656037
        # FNV_prime = 1099511628211
        # algorithm 
        pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        # make a variable equal to 5381
        djb2_hash = 5381
        for char in key:
            # (hash * 33) + unicode value of char
            djb2_hash = (djb2_hash * 33) + ord(char)

        return djb2_hash


    # def djb2_alt(self, key):
    #     """
    #     DJB2 hash, 32-bit

    #     Implement this, and/or FNV-1.
    #     """

    #     # Your code here
    #     # make a variable equal to 5381
    #     djb2_hash = 5381
    #     # print(str(djb2_hash))
    #     # print(djb2_hash.encode())
    #     # print(djb2_hash << 5)

    #     # binary shift
    #     # 0b 01 << 1  --> 010
    #     # 0b 111 << 1  --> 1110
    #     # 0b 01110 << 5  --> 01110 00000

    #     for char in key:
    #         # set hash as hash bit value shifted by 5 plus it's value plus the 
    #         djb2_hash = ((djb2_hash << 5) + djb2_hash) + ord(char)

    #     return djb2_hash

    
    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # print('hash_index', self.djb2(key) % self.capacity)
        # print('key', key)
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        # Store the value with the given key.
        # Hash collisions should be handled with Linked List Chaining.
        # hash key, mod by len array to get idx
            # if idx == None, put Node there
            # else iterate through
                # if same key found, overwrite
                # else append tail
        """
        # Your code here
        # print(self.hash_index(self.key))
        new_node = HashTableEntry(key, value)
        # print('new_node', new_node.value)
        self.storage[self.hash_index(key)] = new_node
        # for (idx, item) in enumerate(self.storage):
        #     if item is None:
        #         print(f"{idx}, None")
        #     else:
        #         print(f"{idx}, {item.value}")


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        to_delete = self.storage[self.hash_index(key)]
        hashed_key = self.hash_index(key)
        del self.storage[hashed_key]
        # Your code here
        # hashed_key = self.hash_index(key)
        # try:
        #     to_delete = self.storage[hashed_key]
        #     print('key', key)
        #     print('to_delete', to_delete.value)
        #     print('hashed_key', hashed_key)
        #     for (idx, item) in enumerate(self.storage):
        #         if item is None:
        #             print(f"{idx}, None")
        #         else:
        #             print(f"{idx}, {item.value}")
        #     del(self.storage[hashed_key])
        #     return to_delete
        # except ValueError:
        #     print('value error')
        #     return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        """
        hash key, mod by len array to get idx
        if idx == None, return None
        else iterate through, find matching key and return value
        """
        # Your code here
        try:
            return self.storage[self.hash_index(key)].value
        except:
            return None



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    # ht = HashTable(8)

    # print('get_load_factor->', ht.get_load_factor())
    # print("")
    # ht.put("line_1", "'Twas brillig, and the slithy toves")
    # ht.put("line_2", "Did gyre and gimble in the wabe:")
    # ht.put("line_3", "All mimsy were the borogoves,")
    # ht.put("line_4", "And the mome raths outgrabe.")
    # ht.put("line_5", '"Beware the Jabberwock, my son!')
    # ht.put("line_6", "The jaws that bite, the claws that catch!")
    # print('get_load_factor->', ht.get_load_factor())
    # print("")
    # ht.put("line_7", "Beware the Jubjub bird, and shun")
    # ht.put("line_8", 'The frumious Bandersnatch!"')
    # ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")
    # ht.put("line_13", "BLAH, BLAH, BLAH")

    # print("")

    # print('get_num_slots->', ht.get_num_slots())
    # print("")

    # print('get_load_factor->', ht.get_load_factor())
    # print("")

    # print('delete->', ht.delete("line_13"))
    # print("")
    
    # # Test storing beyond capacity
    # print("beyond capacity")
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

    ht = HashTable(8)

    ht.put("key-0", "val-0")
    ht.put("key-1", "val-1")
    ht.put("key-2", "val-2")
    print('puts completed?')
    return_value = ht.get("key-0")
    print(return_value == "val-0")
    return_value = ht.get("key-1")
    print(return_value == "val-1")
    return_value = ht.get("key-2")
    print(return_value == "val-2")
    print("")

    ht.delete("key-2")
    ht.delete("key-1")
    ht.delete("key-0")
    print("")
    
    return_value = ht.get("key-0")
    print(return_value is None)
    return_value = ht.get("key-1")
    print(return_value is None)
    return_value = ht.get("key-2")
    print(return_value is None)