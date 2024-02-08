def find_closest(arr, target):
  low = 0
  high = len(arr) - 1
  closest = None

  while low <= high:
      mid = (low + high) // 2
      if arr[mid] == target:
          return arr[mid]
      elif arr[mid] < target:
          low = mid + 1
      else:
          high = mid - 1

      if closest is None or abs(arr[mid] - target) < abs(closest - target):
          closest = arr[mid]

  return closest

sorted_arr = [1, 3, 5, 7, 9]
target = 6
print(find_closest(sorted_arr, target)) 
