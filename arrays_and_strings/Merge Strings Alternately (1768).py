#!/usr/bin/env python
# coding: utf-8

# ### 1768. Merge Strings Alternately - EASY (81%)
# 
# We need to merge two strings being word1 and word2 by alternating their characters. If the strings are different lengths, the remainder of the longer string should be appended to the end of the result.
# 
# We start by initializing an empty string 'merged' to stroe the result. Two pointers 'i' and 'j' are initialized to '0'. 
# 
# The while loop runs as long as 'i' is less than the length of 'word1' or 'j' is less than the length of 'word2', ensuring that we keep merging until both are fully processed.
# 
# Inside the loop, we check if there are remaining characters in 'word1' and 'word2'. If this is the case, the letter is appended to 'merged' and 'i' or 'j' is incremented by 1.
# 
# The loop stops when 'i' and 'j' reach the end of their strings.

# In[1]:


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        i, j = 0, 0  
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                merged += word1[i]
                i += 1
            if j < len(word2):
                merged += word2[j]
                j += 1
        return merged


# In[2]:


solution = Solution()
print(solution.mergeAlternately("abc", "pqr"))  # Output: "apbqcr"
print(solution.mergeAlternately("ab", "pqrs"))  # Output: "apbqrs"
print(solution.mergeAlternately("abcd", "pq"))  # Output: "apbqcd"

