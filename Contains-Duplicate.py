1#Hash Set method:
2class Solution:
3    def containsDuplicate(self, nums: List[int]) -> bool:
4        seen = set()
5        for num in nums:
6            if num in seen:
7                return True 
8            seen.add(num)
9        return False
10
11# #Hash Map Method:
12# class Solution:
13#     def containDuplicate(self, nums: List[int]) -> bool:
14#         seen = {} #empty dictionary (key value pairs)
15#         for num in nums:
16#             if num in seen and seen[num] >= 1: #seen[num] refers to the value stored in the dictionary under the key num.
17#                 return True 
18#             seen[num] = seen.get(num,0) + 1 #seen.get(num, 0): Returns the current count if num exists, Otherwise returns 0
19#         return False