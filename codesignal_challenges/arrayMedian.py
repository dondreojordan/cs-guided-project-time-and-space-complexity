"""
For sequence = [-1, 3, -2, 2], the output should be
arrayMedian(sequence) = 0.5;
For sequence = [1, 3, 2], the output should be
arrayMedian(sequence) = 2.
"""

def arrayMedian(sequence):
    # input: list of integers ragning from positive to negative, and single to multi-digit.
    # To know the median (middle), sum of sequence / length of sequence
    sequence.sort()
    mid = len(sequence) // 2
    # return: median of list 
    return (sequence[mid] + sequence[~mid]) / 2
    
if __name__ == '__main__':
    sequence = [-1, 3, -2, 2]
    # sequence = [0, -2, 15, -125, 85, 90, -63, -233, 186, 926, -330, 37]
    print(arrayMedian(sequence))