def is_sorted_recursive_idx(arr, i=1):
    if i >= len(arr):
        return True
    if arr[i-1] > arr[i]:
        return False
    return is_sorted_recursive_idx(arr, i+1)

# Примеры:
print(is_sorted_recursive_idx([1, 2, 2, 5]))   # True
print(is_sorted_recursive_idx([1, 3, 2]))      # False

Результат работы: 
True
False
