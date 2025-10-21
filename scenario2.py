#You have a sorted list of words. Write two functions, one for linear search and one for binary search, to find a specific word in the list. Provide a return value that includes the answer and the number of steps the program took to encounter the answer.

sorted_word_list = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry']
target_2 = 'orange'



# Linear Search
# def linear_search_sorted_words(word_list, target_word):
    
#     steps = 0
    
#     for index, word in enumerate(word_list):
#         steps += 1
        
#         if word == target_word:
#             return f"Scenario 2 (Linear Search): Target {target_word} found at index {index} in {steps} steps."
#     return -1, steps


# print(linear_search_sorted_words(sorted_word_list, target_2))
# print(f"Scenario 2 (Linear Search): Target {target_2} found at index {result_linear_search_2[0]} in {result_linear_search_2[1]} steps.")

###############################################################

# Binary Search
def binary_search_sorted_words(word_list, target_word):
    
    steps = 0
    low, high = 0, len(word_list) -1
   
    
    while low <= high:
        steps += 1
        mid = (high + low)   // 2
        if word_list[mid] == target_word:
            return f"Scenario 2 (Binary Search): Target {target_word} found at index {word_list.index('orange')} in {steps} steps"
        elif word_list[mid]< target_word:
            low = mid + 1
            
        else:
            high = mid -1
    return -1, steps




print(binary_search_sorted_words(sorted_word_list, target_2))
# print(f"Scenario 2 (Binary Search): Target {target_2} found at index {result_binary_search_2[0]} in {result_binary_search_2[1]} steps.")


