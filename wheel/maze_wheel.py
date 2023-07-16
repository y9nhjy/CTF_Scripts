# DFS
map = '\
.bcsb****\
****c****\
****s*bc*\
cbscbcssb\
sbc*sbc**\
**sbcbs**\
*cbssc***\
*s*cbs***\
*bcssbcs#'

n = m = 9
tx = int(map.index('#') / m)
ty = map.index('#') % m
book = []
for i in range(n):
    book.append([])
    for j in range(m):
        book[i].append(0)
ans = ''
# flag{ddddsssaaaasddsddwddsasssddd}


def dfs(ex, ey, step, state):
    if ex == tx and ey == ty:
        ans = step
        print(ans)
    for i in range(4):
        fx = ex + [0, 1, 0, -1][i]
        fy = ey + [1, 0, -1, 0][i]
        if fx < 0 or fy < 0 or fx >= 9 or fy >= 9:
            continue
        if state == 'b':
            if map[fx * 9 + fy] == 'c' and book[fx][fy] == 0 or map[fx * 9 + fy] == '#':
                book[fx][fy] = 1
                dfs(fx, fy, step + 'dsaw'[i], 'c')
                book[fx][fy] = 0
            else:
                continue
        elif state == 'c':
            if map[fx * 9 + fy] == 's' and book[fx][fy] == 0 or map[fx * 9 + fy] == '#':
                book[fx][fy] = 1
                dfs(fx, fy, step + 'dsaw'[i], 's')
                book[fx][fy] = 0
            else:
                continue
        elif state == 's':
            if map[fx * 9 + fy] == 'b' and book[fx][fy] == 0 or map[fx * 9 + fy] == '#':
                book[fx][fy] = 1
                dfs(fx, fy, step + 'dsaw'[i], 'b')
                book[fx][fy] = 0
            else:
                continue
    return


book[0][0] = 1
dfs(0, 0, '', 's')


# BFS
from collections import deque

map = '''\
***************\
*S000*0000000**\
*0**000*****0**\
*0*00*0*000*0**\
*000**0*0*0*0**\
*0***00*0*0*00*\
*0***0**0*0**0*\
*000*0*00*00*0*\
***0*0******0#*\
***0*00000000**\
*000********0**\
*0***00000*00**\
*0*0*****0**0**\
*0000000*00000*\
***************\
'''

n = m = 15
tx = map.index('#') // m
ty = map.index('#') % m
startx = 1
starty = 1
book = []
for i in range(n):
    book.append([])
    for j in range(m):
        book[i].append(0)


# 定义结构体Note
class Note:
    def __init__(self, x, y, f, s):
        self.x = x  # 横坐标
        self.y = y  # 纵坐标
        self.f = f  # 路径
        self.s = s  # 步数


next = [
    [0, 1],  # 右
    [1, 0],  # 下
    [0, -1], # 左
    [-1, 0]  # 上
]
direction = ['R', 'D', 'L', 'U']

# 队列初始化
que = deque()
que.append(Note(startx, starty, "", 0))
flag = 0

while que:
    head = que.popleft()

    for k in range(4):
        ex = head.x + next[k][0]
        ey = head.y + next[k][1]

        if 0 <= ex < n and 0 <= ey < m and map[ex * 15 + ey] == '0' and book[ex][ey] == 0:
            book[ex][ey] = 1
            que.append(Note(ex, ey, head.f + direction[k], head.s + 1))

        if ex == tx and ey == ty:
            flag = 1
            break

    if flag == 1:
        break

print(que[-1].s)
print(que[-1].f)
