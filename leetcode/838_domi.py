def pushDominoes(dominoes):
    """
    :type dominoes: str
    :rtype: str
    """
    do_map = list('u')*len(dominoes)
    do = list(dominoes)
    cnt: int = int(0)
    for i in do:
        if i != '.':
            do_map[cnt] = 'd'
        cnt = cnt+1
    while(1):
        cnt: int = int(0)
        do = list(dominoes)
        for i in dominoes:
            if i != '.':
                if i == 'L':
                    if cnt - 1 >= 0:
                        if do[cnt - 1] == 'R' and do_map[cnt - 1] == 'u':
                            do[cnt - 1] = '.'
                            do_map[cnt] = 'd'
                        elif do_map[cnt - 1] == 'u':
                            do[cnt - 1] = 'L'
                            do_map[cnt] = 'd'
                elif i == 'R':
                    if cnt + 1 <= len(do) - 1:
                        if do[cnt + 1] == 'L' and do_map[cnt + 1] == 'u':
                            do[cnt + 1] = '.'
                            do_map[cnt] = 'd'
                        elif do_map[cnt + 1] == 'u':
                            do[cnt + 1] = 'R'
                            do_map[cnt] = 'd'
            cnt = cnt + 1
        temp = ''.join(do)
        if dominoes == temp:
            break
        else:
            dominoes = temp
    return dominoes


if __name__ == '__main__':
    dom = "RL"
    dom = pushDominoes(dom)
    print(dom)
