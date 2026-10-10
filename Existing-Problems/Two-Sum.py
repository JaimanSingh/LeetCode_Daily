1class Solution(object):
2    def twoSum(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        #One Pass Hash Table Approach 
9        numMap = {}
10        n = len(nums)
11        for i in range(n):
12            complement = target - nums[i]
13            if complement in numMap:
14                return [numMap[complement],i]
15            numMap[nums[i]] = i
16        return []
17        