1from collections import defaultdict        # Import defaultdict to automatically create empty lists for new keys
2
3class Solution:                             # Define a class named Solution
4    def groupAnagrams(self, strs):          # Define a method that takes a list of strings as input
5        
6        anagram_map = defaultdict(list)    # Create a dictionary where each key maps to an empty list by default
7        
8        for word in strs:                   # Loop through each word in the input list
9            
10            sorted_word = ''.join(sorted(word))
11            # Sort the characters of the word alphabetically and join them back into a string
12            # Example: "eat" -> ['a','e','t'] -> "aet"
13            
14            anagram_map[sorted_word].append(word)
15            # Use the sorted word as a key and add the original word to its list
16            # All anagrams share the same sorted key
17        
18        return list(anagram_map.values())
19        # Return all the grouped anagram lists as a single list
20