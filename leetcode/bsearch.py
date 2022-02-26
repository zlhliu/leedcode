import bisect as bi


class Solution:

    def FourAddedNumEqualFind(self, m: int, arr: list) -> bool:
        # 排序
        arr.sort()

        # 列表长度
        L = len(arr)

        #
        arrNew = list()
        for i in range(L):
            for j in range(L):
                arrNew.append(arr[i] + arr[j])
        arrNew.sort()

        for i in range(L):
            for j in range(L):
                a = m - arr[i] - arr[j]
                if self.TwoAddedNumEqualFind(a, arrNew):
                    return True
        return False

    def TwoAddedNumEqualFind(self, m: int, arr: list):

        L = len(arr)
        # 首先相乘
        # 二分
        if bi.bisect(arr, m) == L*L and m != arr[L*L-1] or bi.bisect(arr, m) == 0:
            return False
        else:
            return bi.bisect(arr, m)



if __name__ == '__main__':
    a = [1, 6, 2, 9]
    b = Solution()
    print(b.FourAddedNumEqualFind(7, a))
