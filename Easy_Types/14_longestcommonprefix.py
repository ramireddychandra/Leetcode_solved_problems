# 14. Longest Common Prefix
# Easy

# 10736

# 3442

# Add to List

# Share
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


def longestCommonPrefix(strs):
    strs.sort(key = lambda x : len(x))
    prefix = strs[0]
    for i in range(len(strs[0]),0,-1):
        if all([prefix[:i] == strs[j][:i] for j in range(1,len(strs))]):
            return prefix[:i]
    return ""



print(longestCommonPrefix(["flower","flow","flight"]))