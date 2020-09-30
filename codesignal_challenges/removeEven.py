"""
Write a function that removes the even numbers from the given array and returns the resulting array.
"""

def removeEvens(numbers):
    # input: a list of numbers, odd and even, single to multi-digit values
    # iterate over numbers list and if number has % 1 expect odd, otherwise even
    odd_num = []
    for num in numbers:
        if num % 2 == 1:
            odd_num.append(num)
    # return: remaining numbers in array
    return odd_num


if __name__ == '__main__':
    numbers = [3, 5, 7]
    # numbers = [1, 2, 3, 4, 5]
    print(removeEvens(numbers))