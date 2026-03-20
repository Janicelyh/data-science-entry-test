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

Explainations: 
Task 1 allow us to do data cleaning by finding and replacing the values that was needed and help to fix incorrect entries. 
This coding 
( if not isinstance(lst, list):
        raise TypeError("lst must be a list") is an input validation to ensure that this is the correct dataset that we want before running the function.
The invoke functions provide the values to replace 2 with 5 within the dataset and replacing apple with orange wihin the list. This function works for 
different types of data such as numbers and text and not just 1.
This data cleaning process will allow dataset to be more meaniningful when doing analysis.    
