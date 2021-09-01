import math
import os
import random
import re
import sys

def chocolateFeast(n, c, m):
    # Write your code here
    #print(n)
    chocoInit = n//c
    tokens = chocoInit
    print(f'chocoInit={chocoInit}, tokens ={tokens}')
    while tokens >=m:
        currentChoco = tokens//m
        tokens -= currentChoco*m
        chocoInit+=currentChoco
        tokens+=currentChoco
    return chocoInit

if __name__ == '__main__':

    n = 10
    c = 2
    m = 5
    print(chocolateFeast(n,c,m))

    n = 12
    c = 4
    m = 4
    print(chocolateFeast(n,c,m))


    n = 6
    c = 2
    m = 2
    print(chocolateFeast(n,c,m))

