import pgzrun

import random

from backstage import *

from Roadpos_set import *

import threading

import time



# 金钱图标对象

money_0 = Actor('金钱框')

money_0.topleft = 975, 100

money_2 = Actor('钱币图标')

money_2.topleft = 975, 77

money_1 = Actor('金钱块')



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

    # screen.blit('bk', (0, 0))



    # 金钱部分

    money_0.draw()

    money_2.draw()

    for i in range(game.money):

        money_1.topleft = 978+20*i, 103

        money_1.draw()

    screen.draw.text("Money:%d/10" %

                     game.money, (1000, 82), color='black')



    # 兵营部分

    screen.blit('arsenal', (20 + 960, 190))

    screen.blit('soldier', (21 + 960, 280))

    warrior_up.draw()  # (35, 350))

    archer_up.draw()   # (131, 350))

    warrior_mid.draw()  # (35, 350))

    archer_mid.draw()  # (131, 350))

    warrior_down.draw()  # (35, 350))

    archer_down.draw()  # (131, 350))

    '''

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

            screen.blit(worrior_image[w.wType], (road[r][w.pos][w.wroute]))

        for w in game.w2[r]:

            screen.blit(worrior_image[w.wType], (road[r][w.pos][w.wroute]))

    '''





def on_mouse_down(pos):  # 造兵方式

    order_command = Command(game.turnID + 10, 0, 0)

    if warrior_up.collidepoint(pos) and game.money >= 2:

        game.money -= 2

        order_command.CmdType = 2

        order_command.CmdStr = [1]

    elif archer_up.collidepoint(pos) and game.money >= 3:

        game.money -= 3

        order_command.CmdType = 3

        order_command.CmdStr = [1]

    elif warrior_mid.collidepoint(pos) and game.money >= 2:

        game.money -= 2

        order_command.CmdType = 2

        order_command.CmdStr = [2]

    elif archer_mid.collidepoint(pos) and game.money >= 3:

        game.money -= 3

        order_command.CmdType = 3

        order_command.CmdStr = [2]

    elif warrior_down.collidepoint(pos) and game.money >= 2:

        game.money -= 2

        order_command.CmdType = 2

        order_command.CmdStr = [3]

    elif archer_down.collidepoint(pos) and game.money >= 3:

        game.money -= 3

        order_command.CmdType = 3

        order_command.CmdStr = [3]

    if order_command.CmdType > 0:

        game.ops1.put(order_command)

        sendOp(target[0], order_command)

        # 此处添加发送命令语句





def update():

    # 初始化回合

    game.update(game.w1)

    game.update(game.w2)

    # 读取命令

    game.ReadCmd(game.ops1, game.w1, 1)

    game.ReadCmd(game.ops2, game.w2, 2)

    # 检查可行的战斗

    game.BattleCheck()

    # 完成战斗

    game.BattleRun(game.BattleList)

    # 主塔死亡结算

    result = game.BaseDeath()

    #若一方主塔死亡, 启动游戏终结机制

    if result > 0:

        game.end(result)

    # 战士死亡结算

    game.WarriorDeath(game.w1)

    game.WarriorDeath(game.w2)

    # 战士移动

    posOccu = dict()  # 记录某格是否被敌方占领

    for i in range(3):

        game.WarriorMove(game.w1[i], posOccu, 1)

        game.WarriorMove(game.w2[i], posOccu, 2)

    # 更新画面

    draw()





def startGame():

    # 开始游戏的流程仍需处理

    connect()  # 连接到服务器

    print('游戏加载中...')

    global game

    game = Action()

    time.sleep(3)

    game.reset()

    print('游戏开始了!')

    print(target[0])

    # 同时开启游戏和接受命令的线程

    getCmd = game.getCmd()

    tcpCliSock.settimeout(0.1)

    getCmd.start()

    g = threading.Thread(target=pgzrun.go())

    g.start()

    getCmd.join()

    g.join()





startGame()