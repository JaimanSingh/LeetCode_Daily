1class Solution(object):
2    def longestConsecutive(self, nums):
3        """
4        :type nums: List[int]     # Input list of integers
5        :rtype: int               # Returns length of longest consecutive sequence
6        """
7
8        if not nums:
9            # If the list is empty, there are no sequences
10            return 0
11
12        s = set(nums)
13        # Convert list to set for O(1) lookup
14        # Also removes duplicates automatically
15        # This is the key to making the solution O(n)
16
17        longest = 1
18        # Variable to store the maximum length found so far
19        # Minimum possible length is 1 (if at least one number exists)
20
21        for x in s:
22            # Iterate through each unique number in the set
23
24            if x - 1 not in s:
25                # Only start counting if x is the BEGINNING of a sequence
26                # Meaning: there is no number before x
27                # Example:
28                # If x = 5 and 4 exists → skip (not start)
29                # If x = 1 and 0 does not exist → start sequence here
30
31                curr = x
32                # Current number we are expanding from
33
34                length = 1
35                # Start sequence length at 1 (counting x itself)
36
37                while curr + 1 in s:
38                    # Keep checking if next consecutive number exists
39                    # This builds the sequence forward
40
41                    curr += 1
42                    # Move to next number
43
44                    length += 1
45                    # Increase sequence length
46
47                longest = max(longest, length)
48                # Update longest sequence found so far
49
50        return longest
51        # Return the maximum consecutive sequence length
52