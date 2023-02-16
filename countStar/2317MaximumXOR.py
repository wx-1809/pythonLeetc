"""
    给你一个下标从 0开始的整数数组nums。一次操作中，选择 任意非负整数x和一个下标i，更新nums[i]为nums[i] AND (nums[i] XOR x)。

注意，AND是逐位与运算，XOR是逐位异或运算。

请你执行 任意次更新操作，并返回nums中所有元素最大逐位异或和。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/maximum-xor-after-operations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from functools import reduce
from typing import List

# reduce()函数会对参数序列中元素进行累积。 https://blog.csdn.net/qq_41554005/article/details/119933746
# 匿名函数lambda https://blog.csdn.net/sweet_tea_/article/details/126746212


class Solution:
    def maximumXOR(self, nums: List[int]) -> int:

        return reduce(lambda x,y: x|y, nums)
        # pass



