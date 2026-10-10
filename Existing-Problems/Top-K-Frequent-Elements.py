1from collections import Counter            # Import Counter to count frequencies using a hash map
2
3class Solution(object):                    # Define the Solution class
4    def topKFrequent(self, nums, k):        # Method to find the top k most frequent elements
5        """
6        :type nums: List[int]               # nums is a list of integers
7        :type k: int                        # k is the number of top frequent elements to return
8        :rtype: List[int]                   # returns a list of integers
9        """
10        
11        count = Counter(nums)               # Count how many times each number appears in nums
12                                            # Creates a dictionary-like object:
13                                            # key   -> number
14                                            # value -> frequency of that number
15        
16        sorted_elements = sorted(
17            count.items(),                  # Convert the dictionary into (number, frequency) pairs
18            
19            key=lambda x: x[1],             # lambda x: x[1] means:
20                                            # - x represents one (number, frequency) pair
21                                            # - x[0] is the number
22                                            # - x[1] is the frequency
23                                            # - sorting is done based on frequency
24            
25            reverse=True                    # Sort in descending order so highest frequency comes first
26        )
27        
28        return [item[0] for item in sorted_elements[:k]]
29                                            # Take the first k elements (top k frequent)
30                                            # Extract only the number (item[0])
31                                            # Ignore the frequency and return the result
32