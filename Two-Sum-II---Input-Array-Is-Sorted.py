1class Solution(object):
2    def twoSum(self, numbers, target):
3        """
4        :type numbers: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        n = len(numbers)
9        i = 0
10        j = n-1
11        while i < j:
12            current_sum = numbers[i] + numbers[j]
13            if current_sum == target:
14                return [i+1, j+1]
15            if current_sum > target:
16                j -= 1
17            else:
18                i += 1
19        return [-1, -1]
20
21"""
22Initialize: left = 0, right = n-1
23
24While left < right:
25    Calculate sum = numbers[left] + numbers[right]
26    
27    If sum == target:
28        └── Found! Return [left+1, right+1]
29    
30    If sum > target:
31        ├── Current sum too large
32        ├── Need smaller value
33        └── Move right pointer left: right--
34    
35    If sum < target:
36        ├── Current sum too small
37        ├── Need larger value
38        └── Move left pointer right: left++
39
40Return [-1, -1] (won't reach due to guaranteed solution)
41"""