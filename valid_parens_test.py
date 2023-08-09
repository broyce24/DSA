class Solution1:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) or len(s) == 1:
            return False
        diffs = 0
        s_set = set()
        for i in range(len(s)):
            s_set.add(s[i])
            if s[i] != goal[i]:
                if diffs == 0:
                    diff_s = s[i]
                    diff_g = goal[i]
                    diffs += 1
                elif diffs == 1:
                    if not s[i] == diff_g or not goal[i] == diff_s:
                        return False
                else:
                    return False
        if not diffs and len(s_set) == len(s):
            return False
        return True


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) != len(s)
        firstIndex = -1
        secondIndex = -1
        for i in range(len(s)):
            if s[i] != goal[i]:
                if firstIndex == -1:
                    firstIndex = i
                elif secondIndex == -1:
                    secondIndex = i
                else:
                    return False
        return s[firstIndex] == goal[secondIndex] and s[secondIndex] == goal[firstIndex]


s = 'ab'
g = 'ab'

S = Solution()
print(S.buddyStrings(s, g))


