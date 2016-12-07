#!/usr/local/bin/python2.7
# encoding=utf8

'''
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
first should = return [0, 1]
second should = return 2 7 
'''
nums = [2, 7, 11, 15]
target = 9

dic = {}
for i, num in enumerate(nums):
    if num in dic:
        print [dic[num], i]   ## printing the index
	print nums[dic[num]], nums[i] ## printing the actual element
    else:
        dic[target - num] = i

