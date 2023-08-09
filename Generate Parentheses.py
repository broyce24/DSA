class Solution:
    def generateParenthesis(self, n: int):
        combos = [['(', n - 1, 1]]
        for _ in range(2 * n - 1):
            for i in range(len(combos)):
                combo = combos[i]
                if combo[1] and combo[2]:
                    combos.append([combo[0] + ')', combo[1], combo[2] - 1])
                    combo[0] += '('
                    combo[1] -= 1
                    combo[2] += 1
                elif combo[2]:
                    combo[0] += ')'
                    combo[2] -= 1
                elif combo[1]:
                    combo[0] += '('
                    combo[1] -= 1
                    combo[2] += 1
        return [p[0] for p in combos]


# Complexity: O(n^2)
# Space: O(2^n)
S = Solution()
#print(S.generateParenthesis(3))

S.generateParenthesis(8)

'''
'''