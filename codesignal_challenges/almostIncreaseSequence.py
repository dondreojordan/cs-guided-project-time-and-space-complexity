"""
Given a sequence of integers as an array, 
determine whether it is possible to obtain a strictly increasing sequence by 
removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. 
Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. 
Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
"""

def almostIncreasingSequence(sequence):
    # input: an array of integers
    # Loop through sequence and for num in seq if num[0 + 2] != idx[0] + 1 return False

    for i in sequence:
        if sequence[i+1].pop and sequence[i]+1 == sequence[i+2]:
            continue
    # # return: boolean, True meaning a number can be removed to make a sequential increase, False meaning no. 
    # return True
# To comabt subscriptable error:
# https://careerkarma.com/blog/python-typeerror-int-object-is-not-subscriptable/

if __name__ == '__main__':
    sequence = [10, 1, 2, 3, 4, 5]
    print(almostIncreasingSequence(sequence))