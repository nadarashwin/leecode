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
ref :- https://discuss.leetcode.com/topic/20844/python-easy-to-understand-solution-with-comments-from-middle-to-two-ends
'''
def sed(s):
    res = ""
    for i in xrange(len(s)):
        for k in xrange(2):
            tmp = helper(s, i, i+k)
            print tmp
            if len(tmp) > len(res):
                res = tmp
    return res



# get the longest palindrome, l, r are the middle indexes   
# from inner to outer
def helper(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]


sed("babad")
