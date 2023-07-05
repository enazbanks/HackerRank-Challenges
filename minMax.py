import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    n = len(arr) - 1
    sorted_arr = sorted(arr)
    min_sum = sum(sorted_arr[0:n])
    max_sum = sum(sorted_arr[-n:])
    print(sorted_arr[-5])
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

miniMaxSum([1,2,3,4,5,6])
