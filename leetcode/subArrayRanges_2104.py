import collections as co


# class Solution:
#     def subArrayRanges(self, nums: list[int]) -> int:
#         # 先爆搜
#         L = len(nums)
#         # ans
#         ans = int(0)
#         # 维护单调最大、最小数
#         maxNumberStack = co.deque()
#         minNumberStack = co.deque()
#         for j in range(L):
#             # 从j开始搜索
#             # 将第一个数字放入
#             maxNumberStack.append(nums[j])
#             minNumberStack.append(nums[j])
#
#             for i in nums[j + 1:]:
#                 # 让max栈栈顶的值保持最大，并且单调排列
#                 if i >= maxNumberStack[-1]:
#                     maxNumberStack.append(i)
#                 if i <= minNumberStack[-1]:
#                     minNumberStack.append(i)
#                 ans += maxNumberStack[-1] - minNumberStack[-1]
#
#             if maxNumberStack[-1] == minNumberStack[-1]:
#                 break
#             # 否则将第j个数弹出，继续
#             maxNumberStack.popleft()
#             minNumberStack.popleft()
#             # 如果上一次最大值和最小值一致，则直接结束
#
#
#         return ans
class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        n = len(nums)
        minLeft, maxLeft = [0] * n, [0] * n
        minStack, maxStack = [], []
        # minLeft中放i最小的边界，同理maxLeft
        # minStack维护左边最小的数字的下标i
        for i, num in enumerate(nums):
            while minStack and nums[minStack[-1]] > num:
                minStack.pop()
            minLeft[i] = minStack[-1] if minStack else -1
            minStack.append(i)

            # 如果 nums[maxStack[-1]] == num, 那么根据定义，
            # nums[maxStack[-1]] 逻辑上小于 num，因为 maxStack[-1] < i
            while maxStack and nums[maxStack[-1]] <= num:
                maxStack.pop()
            maxLeft[i] = maxStack[-1] if maxStack else -1
            maxStack.append(i)

        minRight, maxRight = [0] * n, [0] * n
        minStack, maxStack = [], []
        for i in range(n - 1, -1, -1):
            num = nums[i]
            # 如果 nums[minStack[-1]] == num, 那么根据定义，
            # nums[minStack[-1]] 逻辑上大于 num，因为 minStack[-1] > i
            while minStack and nums[minStack[-1]] >= num:
                minStack.pop()
            minRight[i] = minStack[-1] if minStack else n
            minStack.append(i)

            while maxStack and nums[maxStack[-1]] < num:
                maxStack.pop()
            maxRight[i] = maxStack[-1] if maxStack else n
            maxStack.append(i)

        sumMax, sumMin = 0, 0
        for i, num in enumerate(nums):
            sumMax += (maxRight[i] - i) * (i - maxLeft[i]) * num
            sumMin += (minRight[i] - i) * (i - minLeft[i]) * num
        return sumMax - sumMin

if __name__ == '__main__':
    nums = [4,-2,-3,4,1]
    a = Solution()
    print(a.subArrayRanges(nums))
