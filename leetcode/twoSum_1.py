class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numsN = nums.copy()
        numsIt = nums.copy()
        numsN.sort()
        L = len(nums)
        i = int(0)
        j = int(L - 1)
        while i < j:
            if target < numsN[i] + numsN[j]:
                j = j - 1
            elif target > numsN[i] + numsN[j]:
                i = i + 1
            elif target == numsN[i] + numsN[j]:
                if numsIt.index(numsN[i]) != numsIt.index(numsN[j]):
                    return [numsIt.index(numsN[i]), numsIt.index(numsN[j])]
                else:
                    a = numsIt.index(numsN[i])
                    numsIt[a] = None
                    return [a, numsIt.index(numsN[j])]
            else:
                return None


if __name__ == '__main__':
    a = [1,3,3,2]
    b = Solution()
    print(b.twoSum(a, 6))
