#BRUTE FORCE 
# class Solution(object):
#     def hammingWeight(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         count = 0
#         while n!=0:
#             if (n&1) == 1:
#                 count += 1
#             n >>= 1
        # return count

#BRIAN KERNIGHAN'S ALGORITHM
class Solution(object):
    def hammingWeight(self,n):
        count = 0
        while n!=0:
            n = n&(n-1)
            count += 1
        return count
#https://leetcode.com/problems/number-of-1-bits/solutions/6942378/beats-10000-2-approach-brute-force-optim-1v2v