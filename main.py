

#linear search
unsorted_list = [42, 15, 7, 30, 22, 10, 18]
target_1 = 30

def linear_search_unsorted(arr, target):
    
    step = 0
    for idx, i in enumerate(arr):
        step += 1
        if i == target:
            return f"""Scenario 1 (Linear Search): Target {target} found at index {idx} in {step} steps."""

    return -1


print(linear_search_unsorted(unsorted_list, target_1))

######################################

##binary search

def binary_search_unsorted(arr, target):
    steps = 0
    sorted_list = sorted(arr)
    low, high = 0, len(sorted_list) -1
    
    while low <= high:
        steps += 1
        mid = (high + low) // 2
        if sorted_list[mid] == target:
            return f"Scenario 1 (Binary Search): Target {target} found at index {sorted_list.index(target)} in {steps} steps."

        elif sorted_list[mid] < target:
            low = mid + 1
            
        else:
            high = mid -1
    return -1


print(binary_search_unsorted(unsorted_list, target_1))
        
        