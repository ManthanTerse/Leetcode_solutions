# 1st Method :
# Integer Truncation(Casting) Method
# (Memory: 12.26 MB, Beats: 98.27%)
class Solution(object):
    def isPerfectSquare(self, num):
        root = int(num ** 0.5)
        return root * root == num
      
# 2nd Method :
# Float Comparison Method
class Solution(object):
    def isPerfectSquare(self, num):
        root = num ** 0.5
        return root == int(root)
      
# 3rd Method :
# Modulo Check Method
# (Memory : 12.59 MB , Beats : 51.08%)
class Solution(object):
    def isPerfectSquare(self, num):
        root = num ** 0.5
        if((root % 2 == 0 ) or (root % 2 == 1)):
            return True
        return False
