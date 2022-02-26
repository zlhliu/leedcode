import numpy as nu


# 快慢针优化

class Solution:
    def Calculate(self, n: int) ->int:
        Sum = 0
        while n != 0:
            Sum = Sum + (n % 10) * (n % 10)
            n = int(n / 10)
        return Sum

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        while True:
            if(fast == 1):
                return True
            slow = self.Calculate(slow)
            fast = self.Calculate(fast)
            fast = self.Calculate(fast)
            if (fast == slow):
                return False


if __name__ == '__main__':
    a = 19
    b = Solution()
    print(b.isHappy(a))

