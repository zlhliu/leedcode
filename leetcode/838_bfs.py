import collections as co
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        q = co.deque()
        time = [-1] * n
        force = [[] for _ in range(n)]
        for i, f in enumerate(dominoes):
            if f != '.':
                q.append(i)
                time[i] = 0
                force[i].append(f)

        res = ['.'] * n
        while q:
            i = q.popleft()
            # 如果不止一个力，什么都不做
            if len(force[i]) == 1:
                res[i] = f = force[i][0]
                ni = i - 1 if f == 'L' else i + 1
                if 0 <= ni < n:
                    t = time[i]
                    if time[ni] == -1:
                        q.append(ni)
                        time[ni] = t + 1
                        force[ni].append(f)
                    elif time[ni] == t + 1:
                        force[ni].append(f)
        return ''.join(res)


if __name__ == '__main__':
    dom = "RR...L"
    a = Solution()
    dom = Solution.pushDominoes(a, dom)
    print(dom)
