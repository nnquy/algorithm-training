# Problem from UVA
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=508
# import sys
# sys.stdout = open("file.txt", "w+")

INF = float(1e9)
MAXN = 26


def floyd_warshall(young_graph, old_graph, start_young, start_old):
    for k in range(MAXN):
        for i in range(MAXN):
            for j in range(MAXN):
                young_graph[i][j] = min(young_graph[i][j], young_graph[i][k] + young_graph[k][j])
                old_graph[i][j] = min(old_graph[i][j], old_graph[i][k] + old_graph[k][j])

    min_dist, min_i = INF, -1
    for i in range(MAXN):
        d = young_graph[start_young][i] + old_graph[start_old][i]
        if d < min_dist:
            min_dist, min_i = d, i
    if min_dist >= INF:
        print('You will never meet.')
    else:
        flag = False
        for i in range(MAXN):
            d = young_graph[start_young][i] + old_graph[start_old][i]
            if d == min_dist:
                if flag:
                    print(' {:s}'.format(chr(ord('A') + i)), end='')
                else:
                    flag = True
                    print('{:d} {:s}'.format(min_dist, chr(ord('A') + i)), end='')
        print()


def solution():
    counte = 1
    while True:
        # if counte == 42:
        #     print()
        # counte += 1
        N = int(input().strip())
        if N == 0:
            break

        young_graph = [[INF] * MAXN for i in range(MAXN)]
        old_graph = [[INF] * MAXN for i in range(MAXN)]

        for i in range(MAXN):
            young_graph[i][i] = old_graph[i][i] = 0

        for i in range(N):
            line = list(map(str, input().strip().split()))

            if line[0] == 'Y':
                x = ord(line[2]) - 65
                y = ord(line[3]) - 65
                if x != y:
                    young_graph[x][y] = int(line[-1])
                    if line[1] == 'B':
                        young_graph[y][x] = int(line[-1])
            else:
                x = ord(line[2]) - 65
                y = ord(line[3]) - 65
                if x != y:
                    old_graph[x][y] = int(line[-1])
                    if line[1] == 'B':
                        old_graph[y][x] = int(line[-1])

        start_young, start_old = map(lambda x: ord(x) - 65, input().strip().split())

        # if start_old == start_young:
        #     print('{:d} {:s}'.format(0, chr(ord('A') + start_young)))
        # else:
        floyd_warshall(young_graph, old_graph, start_young, start_old)


solution()


