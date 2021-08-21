
import numpy as np

def linear_search(array, target):
    
    for i in range(0, len(array)):
        if array[i] == target:
            return f"Located target at index: {i} "

    return "Target not in list"

def binary_search(array, target):
    
    first = 0
    last = len(array) -1
    
    while first <=last:
        
        middle = (first + last) // 2
        
        if array[middle] == target:
            return f"Located target at index: {middle} "
        elif array[middle] < target:
            first = middle + 1
        else:
            last = middle
    
    return "Target not in list"


def recursion_binary_search(array, target):
    
    if len(array) == 0:
        return "Target not in list"
    else:
        middle = (len(array) - 1)//2
        
        if array[middle] == target:
            return f"Target found in the list"
        elif array[middle] < target:
            return recursion_binary_search(array[middle+1:], target)
        else:
            return recursion_binary_search(array[:middle], target)
        
print(recursion_binary_search(np.arange(20),1))