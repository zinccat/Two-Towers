import pgzrun
import random
from Roadpos_set import*
from backstage import*


# 该命令所生效的回合
turnID = 0


# 显示页面大小
WIDTH = 1200
HEIGHT = 700

BOX = Rect((0, 250), (1200, 250))
# Rect(left, top, width, height) -> Rect
# Rect((left, top), (width, height)) -> Rect
RED = 200, 0, 0


# 创建造兵按钮 #长宽70

warrior_up = Actor('小兵', (70, 385))
archer_up = Actor('弓箭手', (166, 385))
warrior_mid = Actor('小兵', (70, 510))
archer_mid = Actor('弓箭手', (166, 510))
warrior_down = Actor('小兵', (70, 635))
archer_down = Actor('弓箭手', (166, 635))
warrior_up.x = 70
warrior_up.y = 385
archer_up.x = 166
archer_up.y = 385

# 创建小兵对象

Warrior_image_1 = Actor('小兵色块')
Warrior_image_2 = Actor('小兵色块')
image = ['小兵色块', '小兵色块']
print(image)


def draw():
    screen.clear()
    screen.fill("white")
    screen.blit('bk', (0, 0))

    # 兵营部分
    screen.blit('arsenal', (20, 190))
    screen.blit('soldier', (21, 280))
    warrior_up.draw()  # (35, 350))
    archer_up.draw()   # (131, 350))
    warrior_mid.draw()  # (35, 350))
    archer_mid.draw()  # (131, 350))
    warrior_down.draw()  # (35, 350))
    archer_down.draw()  # (131, 350))
    # 路线部分
    '''
    for k in range(1, 4):
        for i in range(50):
            screen.blit("purchase", (road[0][i][k][0], road[0][i][k][1]))
    for k in range(1, 4):
        for i in range(49):
            screen.blit("purchase", (road[1][i][k][0], road[1][i][k][1]))
    for k in range(1, 4):
        for i in range(50):
            screen.blit("purchase", (road[2][i][k][0], road[2][i][k][1]))
    '''
    # 兵种部分
    for r in range(3):
        for w in w1[r]:
            screen.blit(image[w.wType - 2], (road[r][w.pos][w.wGrid]))
        for w in w2[r]:
            screen.blit(image[w.wType - 2], (road[r][w.pos][w.wGrid]))

    '''
    for k in range (1, 4):
        for i in range (50):
            screen.blit("小兵色块",(road[0][i][k][0] + 5, road[0][i][k][1] + 5))
    for k in range (1, 4):
        for i in range (49):
            screen.blit("弓箭手色块",(road[1][i][k][0] + 5, road[1][i][k][1] + 5))
    for k in range (1, 4):
        for i in range (50):
            screen.blit("小兵色块",(road[2][i][k][0] + 5, road[2][i][k][1] + 5))
    '''


def on_mouse_down(pos):  # 造兵方式
    order_command = Command(game.turnID, 0, [0])

    if warrior_up.collidepoint(pos):
        order_command.CmdType = 2
        order_command.CmdStr = [1]
    elif archer_up.collidepoint(pos):
        order_command.CmdType = 3
        order_command.CmdStr = [1]
    elif warrior_mid.collidepoint(pos):
        order_command.CmdType = 2
        order_command.CmdStr = [2]
    elif archer_mid.collidepoint(pos):
        order_command.CmdType = 3
        order_command.CmdStr = [2]
    elif warrior_down.collidepoint(pos):
        order_command.CmdType = 2
        order_command.CmdStr = [3]
    elif archer_down.collidepoint(pos):
        order_command.CmdType = 3
        order_command.CmdStr = [3]
    # if order_command.CmdType > 0


# 返回Command
def info():
    return order_command


def update():
    global turnID
    turnID += 1
    draw()


pgzrun.go()
