# DFS
maze = '\
.bcsb****\
****c****\
****s*bc*\
cbscbcssb\
sbc*sbc**\
**sbcbs**\
*cbssc***\
*s*cbs***\
*bcssbcs#'

start = '.'
target = '#'
road = 'bcs'
wall = '*'
m = 9         # 列的数量

direction = ['d', 's', 'a', 'w']
pace = [
    [0, 1],  # 右
    [1, 0],  # 下
    [0, -1], # 左
    [-1, 0]  # 上
]

n = len(maze) // m
tx = maze.index(target) // m
ty = maze.index(target) % m
startx = maze.index(start) // m
starty = maze.index(start) % m
book = []
for i in range(n):
    book.append([])
    for j in range(m):
        book[i].append(0)
ans = ''
# flag{ddddsssaaaasddsddwddsasssddd}


def dfs(ex, ey, step, state):
    if ex == tx and ey == ty:
        ans = f"flag{{{step}}}"
        print(ans)
    for i in range(4):
        fx = ex + pace[i][0]
        fy = ey + pace[i][1]
        if fx < 0 or fy < 0 or fx >= n or fy >= m:
            continue
        if state == 'b':
            if maze[fx * m + fy] == 'c' and book[fx][fy] == 0 or maze[fx * m + fy] == target:
                book[fx][fy] = 1
                dfs(fx, fy, step + direction[i], 'c')
                book[fx][fy] = 0
            else:
                continue
        elif state == 'c':
            if maze[fx * m + fy] == 's' and book[fx][fy] == 0 or maze[fx * m + fy] == target:
                book[fx][fy] = 1
                dfs(fx, fy, step + direction[i], 's')
                book[fx][fy] = 0
            else:
                continue
        elif state == 's':
            if maze[fx * m + fy] == 'b' and book[fx][fy] == 0 or maze[fx * m + fy] == target:
                book[fx][fy] = 1
                dfs(fx, fy, step + direction[i], 'b')
                book[fx][fy] = 0
            else:
                continue
    return


book[startx][starty] = 1
dfs(startx, starty, '', 's')





# BFS
from collections import deque


maze = '''\
******************@**************.************...****#..*****.********.*****.****.....*****.****.*********......***********************\
'''

start = '@'
target = '#'
road = '.'
wall = '*'
m = 15         # 列的数量

direction = ['d', 's', 'a', 'w']
pace = [
    [0, 1],  # 右
    [1, 0],  # 下
    [0, -1], # 左
    [-1, 0]  # 上
]

n = len(maze) // m
tx = maze.index(target) // m
ty = maze.index(target) % m
startx = maze.index(start) // m
starty = maze.index(start) % m
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


# 队列初始化
que = deque()
que.append(Note(startx, starty, "", 0))
flag = 0

while que:
    head = que.popleft()

    for k in range(4):
        ex = head.x + pace[k][0]
        ey = head.y + pace[k][1]

        if 0 <= ex < n and 0 <= ey < m and maze[ex * m + ey] not in wall and book[ex][ey] == 0:
            book[ex][ey] = 1
            que.append(Note(ex, ey, head.f + direction[k], head.s + 1))

        if ex == tx and ey == ty:
            flag = 1
            break

    if flag == 1:
        break

print(que[-1].s)
print(que[-1].f)
