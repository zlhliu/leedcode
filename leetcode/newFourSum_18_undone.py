import twoSum_1 as ts


class Solution:
    def FourAddedNumEqualFind(self, m: int, arr: list) -> list[list[int]]:
        # 排序

        # 列表长度
        L = len(arr)

        # 返回值
        arrNew = list()

        # 调用两数的方法
        twoS = ts.Solution()

        for i in range(L):
            for j in range(i, L):
                a = m - arr[i] - arr[j]
                result = twoS.twoSum(arr, a)
                if not result:
                    continue
                res = [arr[result[0]], arr[result[1]], arr[i], arr[j]]
                arrNew.append(res)
        return arrNew


if __name__ == '__main__':
    a = [1, 6, 1, 9]
    b = Solution()
    print(b.FourAddedNumEqualFind(4, a))
