import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # c = number of lists in arr
    # loop through each list and grad the index + 1
    # sum = list[i] + list[i - c -1 ]
    c = len(arr)
    sum1,sum2 = 0,0
    for i in range(len(arr)):
        sum1 = sum1 + arr[i][i]
        sum2 = sum2 + arr[i][c-1]
        c -= 1
    return (abs(sum1-sum2))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
