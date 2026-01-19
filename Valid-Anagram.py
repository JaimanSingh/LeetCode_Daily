1class Solution(object):
2    def isAnagram(self, s, t):
3        """
4        :type s: str
5        :type t: str
6        :rtype: bool
7        """
8        #Hash Map Approach
9        count = defaultdict(int)
10        for x in s:
11            count[x] += 1
12        for x in t:
13            count[x] -= 1
14        for val in count.values():
15            if val!=0:
16                return False 
17        return True
18        