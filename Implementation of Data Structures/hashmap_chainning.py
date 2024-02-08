class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def _hash_function(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next is not None:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            current.next = Node(key, value)
    
    def get(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(f"Key '{key}' not found in the hash map.")
    
    def remove(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
        raise KeyError(f"Key '{key}' not found in the hash map.")

# Example usage:
hash_map = HashMap(10)
hash_map.put("apple", 5)
hash_map.put("banana", 7)
hash_map.put("orange", 3)

print(hash_map.get("apple"))  # Output: 5
print(hash_map.get("banana"))  # Output: 7
print(hash_map.get("orange"))  # Output: 3

hash_map.remove("banana")
print(hash_map.get("banana"))  # Raises KeyError: Key 'banana' not found in the hash map.


#  another method

arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 9]
hashh = [[] for _ in range(len(arr))] 

for i in range(len(arr)):
    hash_value = arr[i] % len(arr) 
    hashh[hash_value].append(arr[i])  

print(hashh)
