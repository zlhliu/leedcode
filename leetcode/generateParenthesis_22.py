import collections as co


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # 动态规划
        if n == 1:
            return ['()']
        # 存放不同个数的括号集
        # nParenthesis[0]中什么都没有
        nParenthesis = [[] for _ in range(n + 1)]
        nParenthesis[0].append('')
        nParenthesis[1].append('()')
        # n个括号,由括号拼接而成
        for i in range(2, n + 1):
            # '(' + j的括号 + ‘)’ + i - j - 1 的括号组成, j从长度0到长度i-1
            for j in range(i):
                for k in nParenthesis[j]:
                    for l in nParenthesis[i - j - 1]:
                        nParenthesis[i].append('(' + l + ')' + k)

        return nParenthesis[n]


if __name__ == '__main__':
    n = 4
    ans = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    a = Solution()
    print(a.generateParenthesis(4))
