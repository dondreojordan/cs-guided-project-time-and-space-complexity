"""
Given a list of integers, your function should return `True` if any value
appears at least two times in the array. Your function should return `False` if
every element is unique.

Example:

Input: [1,3,3,2,1]
Output: True

Example:

Input: [0,1,2,3]
Output: False

*Note: In your first solution, it is okay to use a simple linear search. What
is the time complexity of this approach? Other possible solutions will have
time complexities of `O(n log n)` or `O(n)`. Possible space complexities are
`O(1)` or `O(n)`. Try to come up with solutions with different time and space
complexities and think about the tradeoffs between the solutions.*
"""

# https://www.kite.com/python/answers/how-to-check-for-duplicates-in-a-list-in-python
# def contains_duplicates(nums):
#     if any(nums.count(element) > 1 for element in nums):
#         return True
#     return False

# Which is the same as...  BUT!
# def contains_duplicates(nums):
#     for element in nums:
#         if any(nums.count(element)) > 1:   # BUT... TypeError: 'int' object is not iterable
#             return True
#     return False

# Another way
# def contains_duplicates(nums):
#     s = set()
#     #0(n)
#     for n in sums:
#         s.add(n)  # 0(1)
    
#     # what is the runtime of 'len'
#     # 'len' is an 0(1) function
#     return len(nums) != len(s)

# Another Way...
# def contains_duplicates(nums):
#     # if we sort our nums
#     nums.sort()  # what is the runtime of sorting...  O(n^2) > O(n log n) > O(n)
#     for i in range(1, len(nums)):
#         if nums[i-1] == nums[i]:
#             return True
    # return False

# Another Way

def contains_duplicates(nums):
    # Your code here
    dup1 = set()  # create empty set
    dup2 = set()  # create empty set for true false
    # Check to see if there are any duplicates loop elements in list
    for i in nums:
        if nums.count(i) > 1:
            dup1.add(i)
    # checking if anything is added to the empty list
    if dup1 == dup2:
        return False
    # If there are duplicates the condition is not met and return True
    else:
        return True

    
nums = [0,1,2,3,5]
print(contains_duplicates(nums))
