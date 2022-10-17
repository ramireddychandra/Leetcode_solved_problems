# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].


def roman_to_int(r):
    symbols = ['I','V','X','L','C','D','M']
    values = [1,5,10,50,100,500,1000]
    I = {'V','X'}
    X = {'L','C'}
    C = {'D','M'}
    key_val = dict(zip(symbols,values))
    num = 0
    for i in range(0,len(r)):
        st = r[i:i+2]     
        if (st[0] == 'I' and st[-1] in I) or (st[0] == 'X' and st[-1] in X) or (st[0] == 'C' and st[-1] in C):
            num -= key_val[r[i]]
        else:
            num += key_val[r[i]]
     
    return num
    

print(f"the number written in roman evaluates to: {roman_to_int('MCMXCIV')}")