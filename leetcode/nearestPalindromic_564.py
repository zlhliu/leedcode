# 给定一个表示整数的字符串n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。
#
# “最近的”定义为两个整数差的绝对值最小。
#
#
#
# 示例 1:
#
# 输入: n = "123"
# 输出: "121"
# 示例 2:
#
# 输入: n = "1"
# 输出: "0"
# 解释: 0 和 2是最近的回文，但我们返回最小的，也就是 0。
#
#
# 提示:
#
# 1 <= n.length <= 18
# n只由数字组成
# n不含前导 0
# n代表在[1, 1018- 1] 范围内的整数

class Solution:
    def nearestPalindromic(self, n: str) -> str:

        # 情况1，正常对称过去
        # 情况2：如果长度为奇数，则有可能中间的数字改变后更接近，如89200->89298,但是89198更接近89200,或者12098->12021，但是12121更接近12098
        # number：原本的数字 numberNew:直接低位换的数字 numberSecond:中位数字-1 numberThird:中位数字+1
        # 如果中间数字==0
        # 情况3：100->99而非101，1283->1331而非1221, 999->1001
        # 可以遍历在一定范围内所有的情况
        L = len(n)
        conditions = [10 ** (L - 1) - 1, 10 ** L + 1]
        frontNumber = int(n[:(L + 1) // 2])
        for x in range(frontNumber - 1, frontNumber + 1 + 1):
            # L奇数时只取前一半
            y = x if L % 2 == 0 else x // 10
            # 将y放入x
            while y:
                x = x * 10 + y % 10
                y //= 10
            # 放入conditions
            conditions.append(x)


        # 遍历所有conditions，选择和原数差距最小的
        ans = -1
        number = int(n)
        for condition in conditions:
            if condition == number:
                continue
            if abs(condition - number) < abs(ans - number)\
                    or (abs(condition - number) == abs(ans - number) and condition < ans):# 相等的情况选择小的
                ans = condition

        return str(ans)


if __name__ == '__main__':
    n = "1"
    a = Solution()
    print(a.nearestPalindromic(n))




