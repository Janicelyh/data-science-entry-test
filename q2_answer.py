def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    return


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

Attempted answer : 

def find_and_replace(lst, find_val, replace_val):
    
       if not isinstance(lst, list):
        raise TypeError("lst must be a list")
    
    return [replace_val if item == find_val else item for item in lst]


# Invoke the function with the given scenarios
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")

print(result1)
print(result2)
Output:
[1, 5, 3, 4, 5, 5]
['orange', 'banana', 'orange']
