"""
Given a sorted array `nums`, remove the duplicates from the array.

Example 1:

Given nums = [0, 1, 2, 3, 3, 3, 4]

Your function should return [0, 1, 2, 3, 4]

Example 2:

Given nums = [0, 1, 1, 2, 2, 2, 3, 4, 4, 5]

Your function should return [0, 1, 2, 3, 4, 5].

*Note: For your first-pass, an out-of-place solution is okay. However, after
solving out-of-place, try an in-place solution with a space complexity of O(1).
For that solution, you will need to return the length of the modified `nums`.
The length will tell the user where the end of the array is after removing all
of the duplicates.*
"""

# out-of-place: using extra memory
# in-place:
#

def remove_duplicates(nums):
    # We'll need to remove duplicates from the input list
    # check elements two-at-a-time, remove one of them
    # when we see that the two elements are the same
    # loop through the nums list
    for idx in reversed(range(0, len(nums)-1)):
        if nums[idx] == nums[idx+1]:
            nums.pop(idx+1)


nums = [0, 1, 1, 2, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(nums))