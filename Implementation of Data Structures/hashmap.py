# Simple implementaion
hash_map = {}

array = [1, 2, 3, 4, 5, 5, 61, 2, 3, 4, 5, 61, 2, 3]

for i in array:
    if i in hash_map:
        hash_map[i] += 1
    else:
        hash_map[i] = 1  # Initialize count for new element

print(hash_map)

# Actual implementation

class HashMap:
    def __init__(self):
        self.size = 10  # Initial size of the hash table
        self.table = [[] for _ in range(self.size)]  # Initialize the hash table with empty lists

    def _hash(self, key):
        return hash(key) % self.size  # Simple hash function to get the index in the hash table

    def put(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:  # If key already exists, update its value
                pair[1] = value
                return
        self.table[index].append([key, value])  # Add a new key-value pair

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:  # If key found, return its value
                return pair[1]
        raise KeyError("Key not found")  # Raise an exception if key not found

# Example usage:
hash_map = HashMap()
hash_map.put('a', 1)
hash_map.put('b', 2)
hash_map.put('c', 3)

print(hash_map.get('a'))  # Output: 1
print(hash_map.get('b'))  # Output: 2
print(hash_map.get('c'))  # Output: 3
