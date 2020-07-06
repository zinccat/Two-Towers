import pgzrun
import random
from Roadpos_set import*
from backstage import*


game = Action()

# 命令所生效的回合
game.turnID = 0

# 金钱图标对象
money_0 = Actor('金钱框')
money_0.topleft = 25, 100
money_2 = Actor('钱币图标')
money_2.topleft = 25, 77
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

    #金钱部分
    money_0.draw()
    money_2.draw()
    for i in range(Money):
        money_1.topleft = 28+20*i, 103
        money_1.draw()
    screen.draw.text("Money:%d/10" % Money, (50, 82))
    
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
            screen.blit(image[w.wtype - 2], (road[r][w.pos][w.wroute]))
        for w in game.w2[r]:
            screen.blit(image[w.wtype - 2], (road[r][w.pos][w.wroute]))


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
