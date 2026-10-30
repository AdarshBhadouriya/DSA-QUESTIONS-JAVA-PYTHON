
class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # Skip spaces
        while i < n and s[i] == ' ':
            i += 1

        # Check sign
        sign = 1
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # Convert digits
        num = 0
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            num = num * 10 + digit
            i += 1

        num *= sign

        # Clamp integer range
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
