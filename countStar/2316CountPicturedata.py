"""
    2316. 统计无向图中无法互相到达点对数
    给你一个整数n，表示一张无向图中有n个节点，编号为0到n - 1。同时给你一个二维整数数组edges，其中edges[i] = [ai, bi]表示节点ai 和bi之间有一条无向边。
请你返回 无法互相到达的不同 点对数目。

"""

# 实现
import collections
from itertools import accumulate
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # 查：寻找x的祖先节点
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # 并：将x的祖先节点挂到y的祖先节点上
        def union(x, y):
            parent[find(x)] = find(y)

        parent = list(range(n))  # 初始化每个节点的祖先节点为其自身
        for u, v in edges:
            union(u, v)  # 并

        for i in range(n):  # 统一祖先节点：一个连通块压缩为一个点
            parent[i] = find(i)

        vals = list(collections.Counter(parent).values())  # 每个连通块的大小
        presum = list(accumulate(vals))  # 连通块大小的前缀和
        ans = 0
        for i in range(len(vals)):
            ans += vals[i] * (n - presum[i])  # 数学关系

        return ans
        # pass
