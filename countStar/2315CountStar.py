""""
    2315.统计星号
    给你一个字符串s，每两个连续竖线'|'为 一对。换言之，第一个和第二个'|'为一对，第三个和第四个'|'为一对，以此类推。
请你返回 不在 竖线对之间，s中'*'的数目。
    注意，每个竖线'|'都会 恰好属于一个对。

"""

# 实现
class Solution:
    def countAsterisks(self, s: str) -> int:
        length = len(s)
        ans = cnt = 0
        # 使用两个变量统计 ’|‘ 和’*‘，并输出相关内容/或是统计"|"的那个使用异或来实现统计，或是清零。
        for i in range(length):

            if s[i] == "|":
                cnt += 1

            if s[i] == "*" and cnt % 2 == 0:
                ans += 1

        return ans


