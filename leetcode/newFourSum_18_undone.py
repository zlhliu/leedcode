# import twoSum_1_renew as ts

class twoSumSolution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numsN = nums.copy()
        numsIt = nums.copy()
        numsN.sort()
        L = len(nums)
        i = int(0)
        j = int(L - 1)
        ans = list()
        while i < j:
            if target < numsN[i] + numsN[j]:
                j = j - 1
            elif target > numsN[i] + numsN[j]:
                i = i + 1
            elif target == numsN[i] + numsN[j]:
                if numsIt.index(numsN[i]) != numsIt.index(numsN[j]):
                    ans.append([numsIt.index(numsN[i]), numsIt.index(numsN[j])])
                else:
                    a = numsIt.index(numsN[i])
                    numsIt[a] = None
                    return ans.append([a, numsIt.index(numsN[j])])
            else:
                return None
# 不需要下标，直接返回数字就行了
# 思路是正确的，气死了
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # 排序
        nums.sort()
        # 列表长度
        L = len(nums)

        # 返回值
        arrNew = list()

        # 暂存数组
        tempList = nums.copy()
        # 调用两数的方法
        twoS = twoSumSolution()
        if nums[L - 1] + nums[L - 2] + nums[L - 3] + nums[L - 4] == target:
            return [[nums[L - 1], nums[L - 2], nums[L - 3], nums[L - 4]]]
        for i in range(L):
            # if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            #     break
            # if nums[i] + nums[L - 1] + nums[L - 2] + nums[L - 3] < target:
            #     break
            for j in range(i + 1, L):
                tempList = nums.copy()
                a = target - tempList[i] - tempList[j]
                temp = tempList[j]
                tempList.remove(tempList[i])
                tempList.remove(temp)
                while True:
                    result = twoS.twoSum(tempList, a)
                    if not result:
                        break
                    res = [tempList[result[0]], tempList[result[1]], nums[i], nums[j]]
                    res.sort()
                    if res not in arrNew:
                        arrNew.append(res)
                        break
                    else:
                        temp = tempList[result[1]]
                        tempList.remove(tempList[result[0]])
                        tempList.remove(temp)
        return arrNew


if __name__ == '__main__':
    a = [2,2,2,2,2]
    b = Solution()
    print(b.fourSum(a, 8))
