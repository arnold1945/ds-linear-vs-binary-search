# Scenario 3 Test
occurrence_list = [5, 10, 15, 20, 10, 25, 30, 35, 10, 40]
target_3 = 10




# Linear Search
# def linear_search_last_occurrence(arr, target):
   

#     steps = 0
#     index = -1
    
#     for i in range(len(arr)):
#         steps += 1
#         if arr[i] == target:
#             index = i
            
#     if index != -1:
#         return f"Scenario 3 (Linear Search): Last occurrence of {target} found at index {index} in {steps} steps."

# print(linear_search_last_occurrence(occurrence_list, target_3))
        
        
        
        
######################################################

# Binary Search
def binary_search_last_occurrence(arr, target):

    steps = 0
    arr_sorted = sorted(arr)
    
    print(arr_sorted)
    
    low, high = 0, len(arr_sorted) -1
    
    while low <= high:
        steps += 1
        mid = (high + low) // 2
        if arr_sorted[mid] == target:
            result = mid
            low = mid + 1
        elif arr_sorted[mid] < target:
            low = mid + 1
        else:
            high = mid -1 
            
    if arr_sorted[mid] != -1:
        return f"Scenario 3 (Binary Search): Last occurrence of {target} found at index {result} in {steps} steps."    
    




print(binary_search_last_occurrence(sorted(occurrence_list), target_3))



# print(f"Scenario 3 (Binary Search): Last occurrence of {target_3} found at index {result_binary_search_3[0]} in {result_binary_search_3[1]} steps.")