Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    return


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

Attempted Answer: 

def swap(x, y):
    # Check if both are numeric
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1  
    
    # Swap using only x and y
    x = x + y
    y = x - y
    x = x - y
    
    # Print swapped values
    print("x =", x)
    print("y =", y)


# Invoke the function

# Scenario 1: "Apple", 10
result1 = swap("Apple", 10)
print("Return value:", result1)

# Scenario 2: 9, 17
result2 = swap(9, 17)
print("Return value:", result2)

Expected Output:
       
Return value: -1
x = 17
y = 9
Return value: None
     
Explainations: 
The above swap functions allows us to sort numberic numbers within a dataset and its a temporary value exchange without losing the original data. 
This coding ( (isinstance(x, (int, float)) and isinstance(y, (int, float))): return -1 ) helps to ensure that only numbers will be pick up within the dataset. 
For the invoke function, it is used to call out the values that we needed for sorting. Apple is not numeric hence fucntions returns to -1. 
9 and 17 are numeric and when combine with the ealier swap function and the numbers were swapped and printed as x=17 and y=9 .
