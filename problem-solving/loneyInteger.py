import os
import re
from collections import Counter


def lonelyinteger(a):
    c_dict = Counter(a)
    c_dict = [i for i, count in c_dict.items() if count == 1]
    for i in range(0, len(c_dict)):
        return c_dict[i]

    # a_string = ''.join(map(str, a))
    # unique_int = re.findall(r'\b(\d)\b(?!\d*\1', a_string)
# print(lonelyinteger[0,0,1,0,2,3,3])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
