import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    print(max(len(length) for length in bin(n)[2:].split('0')))
