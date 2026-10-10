#BEST-XOR
class Solution:
    def singleNumber(self,nums):
        r = 0
        for c in nums:
            r ^= c
        return r




# #SORTING:  
# class Solution:
#     def singleNumber(self, nums):
#         n = len(nums)
#         nums.sort()
#         for i in range(0, n-1, 2):
#             if nums[i] != nums[i+1]:
#                 return nums[i]
#         return nums[n-1]

# #HASHSET:
# class Solution:
#     def singleNumber(self, nums):
#         seen=set()
#         for c in nums:
#             if c in seen:
#                 seen.remove(c)
#                 continue 
#             seen.add(c)
#         return next(iter(seen))

#https://leetcode.com/problems/single-number/solutions/8541333/on-time-o1-space-using-xor-beginner-frie-nqs9

