# class Solution(object):
#     def countBits(self, n):
#         """
#         :type n: int
#         :rtype: List[int]
#         """
        
class Solution(object):
    def countBits(self, n):
        ans = []
        for i in range(n + 1):
            x = i              # work on a copy so i stays intact
            count = 0
            while x:
                x &= x - 1     # remove the lowest 1-bit
                count += 1
            ans.append(count)
        return ans