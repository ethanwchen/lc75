#!/usr/bin/env python
# coding: utf-8

# ### Greatest Common Divisor of Strings - EASY (41%)
# 
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
# 
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
# 
# The Euclidean algorithm finds the greatest commmon divisor of two integers. The GCD of two integers is the largest integer that can divide both without leaving a remainder. We start by initializing our two numbers a, b. We replace a with b and b with a mod b. When b becomes zero, we have a as the GCD.
# 
# We first check if the strings even share a pattern by adding the strings and checking if they equal themselves with different strings in front.
# 
# We then run the Euclidean algorithm to find the greatest divisor and output the biggest pattern possible.

# In[2]:


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
       
       # Euclidean Algorithm
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        return str1[:gcd(len(str1), len(str2))]


# In[3]:


solution = Solution()
print(solution.gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
print(solution.gcdOfStrings("ABABAB", "ABAB"))  # Output: "AB"
print(solution.gcdOfStrings("LEET", "CODE"))    # Output: ""

