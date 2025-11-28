#Concatenate Non-Zero Digits & Multiply by Sum 1 Using Python
class Solution(object):
    def sumAndMultiply(self, n):
        s_n = str(n)
        newstr = "".join(digit for digit in s_n if digit != '0')  # list comprehension
        x = int(newstr) if newstr else 0
        digit_sum = sum(int(digit) for digit in newstr)
        return x * digit_sum     
