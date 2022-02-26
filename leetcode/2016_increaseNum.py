class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        L = len(nums)
        # 慢针
        i = 0
        maxVal = -1
        # 快针
        for j in range(1, L):
            if nums[i] >= nums[j]:
                i = j
            else:
                maxVal = max(maxVal, nums[j] - nums[i])
        return maxVal


if __name__ == '__main__':
    nums = [1, 5, 2, 10]
    a = Solution()
    print(a.maximumDifference(nums))

