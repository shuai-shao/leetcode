class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        sum = 0
        div = n
        while div > 0:
            div = div // 5
            sum = sum + div
        return sum
