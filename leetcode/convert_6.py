class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 把每一层的数字放入对应层数的list维护
        a = [[] for _ in range(numRows)]
        # 共L个数字
        L = len(s)

        # 分组放入每一层list
        # 每组数字的个数n = 2 * numRows - 2
        n = 2 * numRows - 2
        # 如果每组只有0个，则只有1个数字
        if n == 0:
            return s
        # 共N组
        N = L / n
        # 向上取整
        if N > int(N):
            N = int(N) + 1
        else:
            N = int(N)
        # 第i组
        for i in range(N):
            # 每组有n个
            # 最后一组可能不满,修改最后一组的个数
            for num in range(n if i!= N - 1 else L - i * n):
                if num < numRows:
                    a[num % numRows].append(s[n * i + num])
                else:
                    a[numRows - 2 - num % numRows].append(s[n * i + num])
        ans = ''
        for i in a:
            for j in i:
                ans = ans + j
        return ans


if __name__ == '__main__':
    s = "AB"
    numRows = 2
    a = Solution()
    print(a.convert(s, numRows))
