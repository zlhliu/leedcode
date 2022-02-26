class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:

        R1, I1 = map(int, num1[:-1].split("+"))
        R2, I2 = map(int, num2[:-1].split("+"))

        return str(R1*R2 - I1*I2) + '+' + str(R1*I2 + R2*I1) + 'i'
    #     a = []
    #     b = []
    #
    #     a = self.sliceStr(num1)
    #     b = self.sliceStr(num2)
    #
    #     r = a[0]*b[0] - a[1]*b[1]
    #     i = a[0]*b[1] + a[1]*b[0]
    #
    #     s = str(r) + '+' + str(i) + 'i'
    #
    #     return s
    #
    #
    # def sliceStr(self, num: str) -> int:
    #     rPart = True
    #     R1 = 0
    #     I1 = 0
    #     sign1 = 1
    #     sign2 = 1
    #     for i in num:
    #         if rPart and i != '+':
    #             if i == 'i':
    #                 I1 = R1
    #                 R1 = 0
    #             else:
    #                 if i == '-':
    #                     sign1 = -1
    #                     continue
    #                 R1 = R1 * 10 + int(i)*sign1
    #                 continue
    #         rPart = False
    #         if i != 'i' and i != '+':
    #             if i == '-':
    #                 sign2 = -1
    #                 continue
    #             I1 = I1 * 10 + int(i)*sign2
    #     return [R1, I1]


if __name__ == '__main__':
    s = "78+-76i"
    s1 = "-86+72i"
    a=Solution()
    print(a.complexNumberMultiply(s,s1))
