# Write a Python function to remove common elements from two sets without using built-in set operations.

def remove_common_elements(set1, set2):
    # Create a new set to store unique elements
    result = []
    
    # Add elements from the first set that are not in the second set
    for element in set1:
        if element not in set2:
            result.append(element)

    # Add elements from the second set that are not in the first set
    for element in set2:
        if element not in set1:
            result.append(element)

    return result

# Example usage
set1 = [1, 2, 3, 4]
set2 = [3, 4, 5, 6]
unique_elements = remove_common_elements(set1, set2)
print(unique_elements) 