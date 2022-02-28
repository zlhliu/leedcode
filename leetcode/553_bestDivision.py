# math
class Node:
    def __init__(self):
        self.maxVal = 0
        self.minVal = 1e6
        self.maxStr = '0'
        self.minStr = ''
class Solution:
    def optimalDivision(self, nums: list[int]) -> str:
        L = len(nums)
        dp = [[Node() for _ in  range(L)] for _ in range(L)]

        # 只有一个的情况
        for i, val in enumerate(nums):
            dp[i][i].maxVal = val
            dp[i][i].minVal = val
            dp[i][i].maxStr = str(val)
            dp[i][i].minStr = str(val)

        # 动态规划遍历
        # i为长度
        for i in range(1, L):
            # j遍历下标
            for j in range(L - i):
                for k in range(j, j + i):
                    # 遍历ij中每一个的最大情况
                    if dp[j][j+i].maxVal < dp[j][k].maxVal/dp[k+1][j+i].minVal:
                        dp[j][j+i].maxVal = dp[j][k].maxVal/dp[k+1][j+i].minVal
                        # 修改字符
                        # 去除单独数字加括号的情况
                        if k+1 == j+i:
                            dp[j][j + i].maxStr = dp[j][k].maxStr + '/' + dp[k + 1][j + i].minStr
                        else:
                            dp[j][j+i].maxStr = dp[j][k].maxStr + '/(' + dp[k+1][j+i].minStr + ')'
                    # 遍历ij中每一个的最小情况
                    if dp[j][j+i].minVal > dp[j][k].minVal/dp[k+1][j+i].maxVal:
                        dp[j][j+i].minVal = dp[j][k].minVal/dp[k+1][j+i].maxVal

                        if k + 1 == j + i:
                            dp[j][j + i].minStr = dp[j][k].minStr + '/' + dp[k + 1][j + i].maxStr
                        else:
                            dp[j][j + i].minStr = dp[j][k].minStr + '/(' + dp[k + 1][j + i].maxStr + ')'

        return dp[0][L-1].maxStr
        # if len(nums) == 1:
        #     return ''.join(str(nums[0]))
        # elif len(nums) == 2:
        #     return ''.join(str(nums[0])) + '/' +''.join(str(nums[1]))
        # numsN = list()
        # numsN.append(str(nums[0]))
        # numsN.append('/')
        # numsN.append('(')
        # for i in range(len(nums)-1):
        #     numsN.append(str(nums[i+1]))
        #     numsN.append('/')
        # numsN.pop()
        # numsN.append(')')
        # return ''.join(numsN)



if __name__ == '__main__':
    s = [2,6,5,9,8,2,3]
    a = Solution()
    print(a.optimalDivision(s))
