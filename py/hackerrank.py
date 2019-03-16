"""
Given a square matrix of size , calculate the absolute difference between the sums of its diagonals.
Input Format
The first line contains a single integer, . The next  lines denote the matrix's rows, with each line containing space-separated integers describing the columns.
Print the absolute difference between the two sums of the matrix's diagonals as a single integer.

#!/bin/python3

import sys

def diagonalDifference(a):
    # Complete this function
    p = 0
    s = 0
    for i in range(len(a)):
        p += a[i][i]
        s += a[i][(len(a)-1-i)]
    return(abs(p-s))

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
"""
"""
Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a new line.

#!/bin/python3

import sys

def plusMinus(arr):
    # Complete this function
    a = [0,0,0]
    if len(arr)>0:
        for i in arr:
            a[0] += 1 if i>0 else 0
            a[1] += 1 if i<0 else 0
            a[2] += 1 if i==0 else 0
        print("{0:.6f}".format(a[0]/len(arr)))
        print("{0:.6f}".format(a[1]/len(arr)))
        print("{0:.6f}".format(a[2]/len(arr)))
    else:
        print(0)
        print(0)
        print(0)

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
"""

"""
Consider a staircase of size :

   #
  ##
 ###
####
Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size .

#!/bin/python3

import sys

def staircase(n):
    # Complete this function
    for i in range(n):
        print(' '*(n-i-1)+'#'*(i+1))
if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
"""
"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

#!/bin/python3

import sys

def miniMaxSum(arr):
    # Complete this function
    arrs = sorted(arr)
    print(sum(arrs[0:4]),sum(arrs[1:5]))
if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
"""

"""
You are in-charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age. When she blows out the candles, she’ll only be able to blow out the tallest ones.

For example, if your niece is turning  years old, and the cake will have  candles of height , , , , she will be able to blow out  candles successfully, since the tallest candle is of height  and there are  such candles.

Complete the function birthdayCakeCandles that takes your niece's age and an integer array containing height of each candle as input, and return the number of candles she can successfully blow out.

#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    ars = sorted(ar)
    c = 0
    for x in ars:
        c += 1 if x == ars[(n-1)] else 0
    return(c)
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
"""

"""
Given a time in -hour AM/PM format, convert it to military (-hour) time.
Note: Midnight is  on a -hour clock, and  on a -hour clock. Noon is  on a -hour clock, and  on a -hour clock.
Input Format
A single string containing a time in -hour clock format (i.e.:  or ), where  and .

#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function
    if s[8]=='A':
        if s[0:2]=='12':
            s='00'+s[2:8]
        else:
            s='{num:02d}'.format(num=int(s[0:2]))+s[2:8]
    else:
        if s[0:2]=='12':
            s='12'+s[2:8]
        else:
            s='{num:02d}'.format(num=(12+int(s[0:2])))+s[2:8]
    return(s)

s = input().strip()
result = timeConversion(s)
print(result)
"""

"""
Find the number of ways that a given integer, , can be expressed as the sum of the  powers of unique, natural numbers.

Input Format

The first line contains an integer . 
The second line contains an integer .

Constraints

Output Format
Output a single integer, the answer to the problem explained above.


#!/bin/python3

import sys

def powerSum(X, N):
    # Complete this function
    arr = []
    max = int(1+X**(1/float(N)))
    for i in range(1,max):
        if (i**N) <= X:
            arr.append((i**N))
    #print(arr)
    def recur(dig, ar):
        c = 0
        for i, j in enumerate(ar):
            if sum(dig) + j == X:
                c += 1
            else:
                c += recur(dig+[j], ar[i+1:])
        return c
    return recur([],arr)

if __name__ == "__main__":
    X = int(input().strip())
    N = int(input().strip())
    result = powerSum(X, N)
    print(result)
"""

"""

"""
