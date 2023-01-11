import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    n = len(a)
    swap_count = 0
    for i in range(0,n-1):
        for j in range(0,n-1):
            temp = a[j]
            if a[j] > a[j+1]:
                a[j] = a[j + 1]
                a[j +1] = temp
                swap_count+=1
    print("Array is sorted in " + str(swap_count) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[n-1]))
           

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
