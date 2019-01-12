#  Problem from SPOJ
#  https://www.spoj.com/problems/TRVCOST/


import heapq
import sys


class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist < other.dist


def dijkstra(n, s, graph):

    dist = [-1 for x in range(n + 1)]
    pqueue = []
    heapq.heappush(pqueue, Node(s, 0))
    dist[s] = 0

    while len(pqueue) > 0:
        top = heapq.heappop(pqueue)
        u = top.id
        w = top.dist
        for neighbor in graph[u]:
            if w + neighbor.dist < dist[neighbor.id] or dist[neighbor.id] == -1:
                dist[neighbor.id] = w + neighbor.dist
                heapq.heappush(pqueue, Node(neighbor.id, dist[neighbor.id]))


    return 1


def solution():

    s = int(input())

    cities_index = {}

    for i in range(s):

        n = int(input())
        graph = [[] for xx in range(n + 1)]
        for xxx in range(n):

            cities_index[input()] = xxx + 1

            n_road = int(input())
            for r in range(n_road):
                ct, we = map(int, input().strip().split())
                graph[xxx + 1].append(Node(ct, we))


        results = dijkstra(U, graph, queries)



solution()
