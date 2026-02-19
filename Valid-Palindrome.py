1class Solution(object):
2    def isPalindrome(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7        new = ""
8        for i in s:
9            if i.isalnum():
10                new += i.lower()
11        return new == new[::-1]