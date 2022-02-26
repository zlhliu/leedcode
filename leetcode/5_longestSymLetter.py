class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        maxl = 0
        begin = 0

        if n == 1:
            return s

        if n == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        for L in range(2, n+1):

            for i in range(n):
                j = i + L - 1

                # j越界则无意义
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False

                elif j - i <= 2:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]

                if dp[i][j] and j - i + 1 > maxl:
                    maxl = j - i + 1
                    begin = i
        if maxl == 0:
            maxl = 1
        return s[begin:begin+maxl]


if __name__ == '__main__':
    s='axcb'
    a = Solution()

    print(a.longestPalindrome(s))

