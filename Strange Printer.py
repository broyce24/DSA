class Solution:
    def strangePrinter(self, s: str) -> int:
        # goal: turn 'abcbb' into ['a', 'b', 'c', 'b']
        chars = []
        for c in s:
            if not chars or c != chars[-1]:
                chars.append(c)
        count = 0
        while chars:
            if chars[0] == chars[-1]:
                print(chars.pop(0))
                if chars:
                    print(chars.pop(-1))
            elif chars[:-1][0] == chars[:-1][-1]: # if we want to remove the last item
                print(chars.pop(-1))
            else:
                print(chars.pop(0))
            count += 1
        return count









S = Solution()
a = (2, 'aaabbb')
b = (2, 'aba')
c = (3, 'abcba')
d = (3, 'abcb')
e = (5, 'abcabc')
f = (5, 'abababac')
g = (1, 'aaaa')
h = (2, 'aaab')
i = (6, 'leetcode')
j = (3, 'abcbb')
k = (3, 'bcbba')
m = (8, "nwlrbbmqbh")
n = (8, "nwhlrbbmqbh")
o = (5, 'dabcbdf')
p = (7, "abacababacab")
q = (7, "bacababacaba")
case = c
#print(case, S.strangePrinter(case[1]))
#print("Correct answer is", case[0], "Result is", S.strangePrinter(case[1]))

def run_cases(lis):
    for case in lis:
        print("Correct answer is", case[0], "Result is", S.strangePrinter(case[1]))

run_cases([p, o, n, m, a, b, c, d, e, f, g, h, i, j, k])
'''
aaaaaa
abbbbb
abcccc
abcaac
abcabc
'''

''' storing char and min, max indices
class Solution:
    def strangePrinter(self, s: str) -> int:
        moves = 0
        # hashmap associating char with its [min, max] indices
        char_map = {}
        for i, char in enumerate(s):
            if char not in char_map:
                char_map[char] = [i, i]
                moves += 1
            else:
                char_map[char][1] = i
        print(char_map)
        return moves
'''

''' front and back typewriter
class Solution:
    def strangePrinter(self, s: str) -> int:
        moves = 0
        # pointer = [char, index]
        front_char, front_index = s[0], 0
        back_char, back_index = s[len(s) - 1], len(s) - 1
        moving_forward = True
        while True:
            run = ''  #
            while moving_forward:
                run += s[front_index]
                if s[front_index + 1] == front_char:
                    front_index += 1
                else:
                    moves += 1
                    print(run)  #
                    moving_forward = False
                    if back_index - front_index == 1:
                        return moves
            run = ''  #
            while not moving_forward:
                run += s[back_index]
                if s[back_index - 1] == back_char:
                    back_index -= 1
                else:
                    moves += 1
                    print(run)
                    moving_forward = True
                    if back_index - front_index == 1:
                        return moves
'''