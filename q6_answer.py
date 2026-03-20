def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    return


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

Attempted answers:

def find_first_negative(lst):
    i = 0
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]
        i += 1
    return "No negatives"

# Invoke the function with the given scenarios
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
result2 = find_first_negative([2, 10, 7, 0])

print(result1)  # Output: -1
print(result2)  # Output: No negatives

Output:
-1
No negatives

Explainations: 
The task 1 function allow us to do data validation to quickly detect the first negative numbers in a list without scanning the entire list. 
This is useful in data cleaning where one can filter out outliers or values that doesnt make sense within the datasetss. In the above coding funtions, 
it calls out negative values as the "error" data and users will be prompted to clean up the data. 
The invoke functions calls out the scenarios to check on negatives within the datasets where result1 calls out the negative value with -1 while 
there is no negatives in result2.
