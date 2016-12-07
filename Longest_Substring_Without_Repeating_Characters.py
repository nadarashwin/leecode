#!/usr/local/bin/python2.7
# encoding=utf8

'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

def lengthOfLongestSubstring(s):
    maxln = 0
    start = 0
    last = {}
    for i in range(len(s)): ## we can consider i as an end point
        if s[i] in last and last[s[i]] >= start:
            ##print s[i], last[s[i]], start
            start = last[s[i]] + 1
            ##print start
        last[s[i]] = i
        ##print "last[s[i]]", last[s[i]], last
        maxln = max(maxln, i - start + 1)
        ##print maxln
    return maxln

print lengthOfLongestSubstring("abcabcbb")
print lengthOfLongestSubstring("bbbbb")
print lengthOfLongestSubstring("pwwkew")
