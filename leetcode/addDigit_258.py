class Solution:
    def addDigits(self, num: int) -> int:
        # 可以很容易看到9的循环
        # 初始的0可以直接返回
        if num == 0:
            ans = num
        else:
            ans = num % 9 if num % 9 != 0 else 9
        return ans


if __name__ == '__main__':
    num = 0
    a = Solution()
    print(a.addDigits(num))
