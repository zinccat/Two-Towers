import pgzrun
import random
from Roadpos_set import*
from backstage import*


game = Action()

# 命令所生效的回合
game.turnID = 0


# 金钱图标对象
money_0 = Actor('金钱框')
money_0.topleft = 975, 100
money_2 = Actor('钱币图标')
money_2.topleft = 975, 77
money_1 = Actor('金钱块')

Money = 0       # 金钱数
time_count = 0  # 记录帧数


# 钱数变化函数
def Money_accumulate(x):
    global Money
    Money += x


# 显示页面大小
WIDTH = 1200
HEIGHT = 700


# 创建造兵按钮 #长宽70

warrior_up = Actor('小兵', (70 + 960, 385))
archer_up = Actor('弓箭手', (166 + 960, 385))
warrior_mid = Actor('小兵', (70 + 960, 510))
archer_mid = Actor('弓箭手', (166 + 960, 510))
warrior_down = Actor('小兵', (70 + 960, 635))
archer_down = Actor('弓箭手', (166 + 960, 635))

# 创建小兵对象

Knight_image = Actor('小兵色块')
Archer_image = Actor('弓箭手色块')

worrior_image = ['基地', '防御塔', '小兵色块', '弓箭手色块']


def draw():
    screen.clear()
    screen.fill("white")
    screen.blit('bk', (0, 0))

    # 金钱部分
    money_0.draw()
    money_2.draw()
    for i in range(Money):
        money_1.topleft = 978+20*i, 103
        money_1.draw()
    screen.draw.text("Money:%d/10" % Money, (1000, 82), color='black')

    # 兵营部分
    screen.blit('arsenal', (20 + 960, 190))
    screen.blit('soldier', (21 + 960, 280))
    warrior_up.draw()  # (35, 350))
    archer_up.draw()   # (131, 350))
    warrior_mid.draw()  # (35, 350))
    archer_mid.draw()  # (131, 350))
    warrior_down.draw()  # (35, 350))
    archer_down.draw()  # (131, 350))

    # 路线部分
    for k in range(1, 4):
        for i in range(50):
            screen.blit("purchase", (road[0][i][k][0], road[0][i][k][1]))
    for k in range(1, 4):
        for i in range(49):
            screen.blit("purchase", (road[1][i][k][0], road[1][i][k][1]))
    for k in range(1, 4):
        for i in range(50):
            screen.blit("purchase", (road[2][i][k][0], road[2][i][k][1]))

    
    # 兵种部分
    for r in range(3):
        for w in game.w1[r]:
            screen.blit(worrior_image[w.wtype], (road[r][w.pos][w.wgrid]))
        for w in game.w2[r]:
            screen.blit(worrior_image[w.wtype], (road[r][w.pos][w.wgrid]))


def on_mouse_down(pos):  # 造兵方式
    order_command = Command(game.turnID, 0, [0])
    global Money
    if warrior_up.collidepoint(pos) and Money >= 2:
        Money -= 2
        order_command.CmdType = 2
        order_command.CmdStr = [1]
    elif archer_up.collidepoint(pos) and Money >= 3:
        Money -= 3
        order_command.CmdType = 3
        order_command.CmdStr = [1]
    elif warrior_mid.collidepoint(pos) and Money >= 2:
        Money -= 2
        order_command.CmdType = 2
        order_command.CmdStr = [2]
    elif archer_mid.collidepoint(pos) and Money >= 3:
        Money -= 3
        order_command.CmdType = 3
        order_command.CmdStr = [2]
    elif warrior_down.collidepoint(pos) and Money >= 2:
        Money -= 2
        order_command.CmdType = 2
        order_command.CmdStr = [3]
    elif archer_down.collidepoint(pos) and Money >= 3:
        Money -= 3
        order_command.CmdType = 3
        order_command.CmdStr = [3]


'''
    if order_command.CmdType > 0:
        game.ops1.put(order_command)
        # chat(target, order_command)
        # 此处添加发送命令语句
'''


def update():

    # 金钱更新
    global time_count
    time_count += 1
    if time_count == 60:
        time_count = 0
        if Money < 10:
            Money_accumulate(1)

    # 回合数更新
    global game
    game.turnID += 1

    # 绘图
    draw()


pgzrun.go()
