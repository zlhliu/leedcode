class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        # 返回值answear
        ans = 0
        # 遍历2^m次,即枚举所有的请求的可能性，使用一个二进制数维护
        for mask in range(1 << len(requests)):
            # cnt为mask对应的请求的数量，1的数量
            cnt = 0
            for i in range(mask.bit_length()):
                if mask & (1 << i):
                    cnt += 1
            # 如果已经有cnt数量的请求通过，则不需要判断
            if cnt <= ans:
                continue
            # 一个列表维护此次请求的n栋楼的人数平衡
            pBalance = [0 for _ in range(n)]
            # 开始判断mask是否通过,m为第m个请求，(i, j)为具体的request
            for m, (i, j) in enumerate(requests):
                # 如果位置存在1，则是请求
                if mask & (1 << m):
                    pBalance[i] += 1
                    pBalance[j] -= 1
            z = 1
            # 判断是否所有的楼人数都是平衡的
            if all(x == 0 for x in pBalance):
                ans = cnt
        return ans


if __name__ == '__main__':
    n=3
    requests = [[1,2],[1,2],[2,2],[0,2],[2,1],[1,1],[1,2]]
    a = Solution()
    print(a.maximumRequests(n, requests))
