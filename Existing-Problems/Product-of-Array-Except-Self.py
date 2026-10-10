1class Solution(object):
2    def productExceptSelf(self, nums):
3        """
4        :type nums: List[int]        # Input list of integers
5        :rtype: List[int]            # Output list where each element is
6                                     # the product of all elements except itself
7        """
8
9        # ---------------- LEFT MULTIPLICATION ARRAY ----------------
10        # This array stores the cumulative product of elements
11        # from the left side (index 0 up to current index)
12
13        left_multiply = []           # List to store left cumulative products
14        temp = 1                     # Temporary variable to store running product
15
16        for num in nums:             # Traverse the array from left to right
17            temp *= num              # Multiply current number with running product
18            left_multiply.append(temp)
19                                     # Append current product to left_multiply
20
21        # Example:
22        # nums = [1, 2, 3, 4]
23        # left_multiply = [1, 2, 6, 24]
24
25        # ---------------- RIGHT MULTIPLICATION ARRAY ----------------
26        # This array stores the cumulative product of elements
27        # from the right side (index n-1 down to current index)
28
29        right_multiply = []          # List to store right cumulative products
30        temp = 1                     # Reset running product
31
32        for num in nums[::-1]:       # Traverse the array from right to left
33            temp *= num              # Multiply current number with running product
34            right_multiply.append(temp)
35                                     # Append product (in reverse order)
36
37        right_multiply = right_multiply[::-1]
38                                     # Reverse to match original index order
39
40        # Example:
41        # right_multiply = [24, 24, 12, 4]
42
43        # ---------------- FINAL ANSWER CALCULATION ----------------
44
45        ans = []                     # List to store final result
46
47        for i in range(len(nums)):   # Loop through each index
48            left = left_multiply[i-1] if i > 0 else 1
49                                     # Product of all elements to the left of index i
50                                     # If i == 0, there are no left elements → use 1
51
52            right = right_multiply[i+1] if i < len(nums)-1 else 1
53                                     # Product of all elements to the right of index i
54                                     # If i is last index → use 1
55
56            ans.append(left * right) # Multiply left and right products and append
57
58        return ans                   # Return the final result list
59