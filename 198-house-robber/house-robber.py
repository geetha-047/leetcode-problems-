class Solution:
    def rob(self, nums):
        a = 0
        b = 0

        for money in nums:
            c = max(a + money, b)
            a = b
            b = c

        return b