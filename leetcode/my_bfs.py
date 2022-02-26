import collections as co


def pushDominoes(dominoes: str) -> str:
    # q放置每一层的节点
    q = co.deque()
    # n记录总数
    n = len(dominoes)
    # force放置
    force = [[] for _ in range(n)]
    # 记录时刻
    time = [-1]*n

    for i, j in enumerate(dominoes):
        # 查询节点是否符合
        if j != '.':
            q.append(i)
        # 0时刻的初始多米诺
            time[i] = 0
            force[i].append(j)

    res = ['.']*n
    while q:
        i = q.popleft()
        if len(force[i]) == 1:
            f = force[i][0]
            res[i] = f
            ni = i-1 if f == 'L' else i+1
            if 0 <= ni < n:
                # 根据时间执行操作，
                t = time[i]
                # 如果是没有触发的多米诺
                if time[ni] == -1:
                    # 加入节点队列
                    q.append(ni)
                    # 时间更新
                    time[ni] = t+1
                    # 力
                    force[ni].append(f)
                # 同时触碰的情况
                elif time[ni] == t+1:
                    # 此时会出现[]中有两个的情况
                    force[ni].append(f)
    return ''.join(res)


if __name__ == '__main__':
    dom = "R.R.LL"
    dom = pushDominoes(dom)
    print(dom)