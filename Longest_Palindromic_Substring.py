#!/usr/local/bin/python2.7
# encoding=utf8

'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.

------------------

Input: "cbbd"

Output: "bb"

'''

from itertools import combinations
def sed(st):
 for y in range(len(st)-1,1,-1): ## starting from descending order
  for x in combinations(st,y):
   ###print x   
   if ''.join(x)==''.join(x)[::-1]:
    print ''.join(x)

sed("babad")
