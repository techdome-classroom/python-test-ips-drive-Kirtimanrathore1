def smallest_missing_positive_integer(nums: list[int]) -> int:
    """
    Implement the function smallest_missing_positive_integer 
    using the provided smallest_missing_positive_integer function 
    to find the smallest missing positive integer in the given list.

    """
    
    
    
    if not nums:
        return 1

    # Move all positive integers to the left side of the list
    j = 0
    for i in range(len(nums)):
        if nums[i] > 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    
    # Check if all numbers are negative or zero
    if j == 0:
        return 1
    
    # Mark the presence of numbers using index as the indicator
    for i in range(j):
        if abs(nums[i]) - 1 < j and nums[abs(nums[i]) - 1] > 0:
            nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
    
    # Find the smallest missing positive integer
    for i in range(j):
        if nums[i] > 0:
            return i + 1
    
    return j + 1

# Example usage:
print(smallest_missing_positive_integer([3, 4, -1, 1]))  # Output: 2
print(smallest_missing_positive_integer([1, 2, 0]))     # Output: 3
print(smallest_missing_positive_integer([-1, -3, 4, 2]))# Output: 1


    



  

