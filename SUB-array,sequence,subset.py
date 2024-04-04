import itertools

nums = [1, 2, 3, 4]
k = 2

# Subarrays of size k
print("Subarrays of size k:")
for i in range(len(nums) - k + 1):
    print(nums[i:i + k])

# Subsequences of size k
print("\nSubsequences of size k:")
for subset in itertools.combinations(nums, k):
    print(list(subset))

# Subsets of size k
print("\nSubsets of size k:")
for subset in itertools.permutations(nums, k):
    print(list(subset))
