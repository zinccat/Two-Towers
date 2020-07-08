import pgzrun

import random

from backstage import *

from Roadpos_set import *

import threading

from time import sleep

ide = []
# 血量图标对象

player_icon = Actor('人图标')

life_frame = Actor('血框')

life_block = Actor('血块')

life_icon = Actor('生命值图标')

DenfenseTower_icon = Actor('防御塔图标')

Base_icon = Actor('主塔图标')


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


# 创建小兵图片对象

Knight_image = Actor('小兵色块')
Archer_image = Actor('弓箭手色块')
worrior_image = [0, '防御塔色块', '小兵色块', '弓箭手色块']


def draw():
    screen.clear()
    screen.fill("white")
    screen.blit('bk', (250, 0))

    # 金钱部分
    money_0.draw()
    money_2.draw()

    for i in range(game.money):
        money_1.topleft = 978+20*i, 103
        money_1.draw()

    screen.draw.text("Money:%d/10" % game.money, (1000, 82), color='black')

    # 兵营部分

    screen.blit('arsenal', (20 + 960, 190))
    screen.blit('soldier', (21 + 960, 280))
    warrior_up.draw()
    archer_up.draw()
    warrior_mid.draw()
    archer_mid.draw()
    warrior_down.draw()
    archer_down.draw()

    # 兵种部分

    for r in range(3):
        for w in game.w1[r]:
            if w.wType != 0:
                screen.blit(worrior_image[w.wType], (road[r][w.pos][w.wGrid]))
        for w in game.w2[r]:
            if w.wType != 0:
                screen.blit(worrior_image[w.wType], (road[r][w.pos][w.wGrid]))
    # 血量部分
    for j in range(8):
        if j > 3:
            dfx = 0
            dfy = -640
        else:
            dfx = 0
            dfy = 0

        life_frame.topleft = 25+dfx, 440+j*70+dfy
        life_icon.topleft = 24+dfx, 421+j*70+dfy

        if j % 4 == 0:

            Base_icon.topleft = 211+dfx, 416+j*70+dfy
            Base_icon.draw()
            screen.draw.text("Base", (170+dfx, 422+70*j+dfy), color='black')

        else:
            DenfenseTower_icon.topleft = 218+dfx, 417+j*70+dfy
            DenfenseTower_icon.draw()
            if (j-1) % 4 == 0:
                screen.draw.text(
                    "Turret(top)", (138+dfx, 422+70*j+dfy), color='black')
            elif (j-2) % 4 == 0:
                screen.draw.text(
                    "Turret(mid)", (138+dfx, 422+70*j+dfy), color='black')
            else:
                screen.draw.text(
                    "Turret(bot)", (138+dfx, 422+70*j+dfy), color='black')

        life_frame.draw()
        life_icon.draw()
        for i in range(game.life[j]):
            if j % 4 == 0:
                life_block.topleft = 27+2*i//5+dfx, 443+70*j+dfy
            else:
                life_block.topleft = 27+2*i+dfx, 443+70*j+dfy
            life_block.draw()
        if j % 4 == 0:
            screen.draw.text(
                "Life:%d/500" % game.life[j], (43+dfx, 422+70*j+dfy), color='black')

        else:
            screen.draw.text(
                "Life:%d/100" % game.life[j], (43 + dfx, 422 + 70 * j + dfy), color='black')

    player_icon.topleft = 27, 380
    player_icon.draw()
    player_icon.topleft = 27, 20
    player_icon.draw()
    screen.draw.text("player: %s" % ide[0], (52, 382), color='black')
    screen.draw.text("player: %s" % ide[1], (52, 22), color='black')


def on_mouse_down(pos):  # 造兵方式

    order_command = Command(game.turnID + 60, 0, [0])
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
        sendOp(target[0], order_command) # 发送指令给对方


def update():
    # 初始化回合
    game.update()

    # 读取命令
    game.ReadCmd()
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

    game.WarriorDeath()

    # 战士移动

    for i in range(3):

        game.WarriorMove(game.w1[i], 1)
        game.WarriorMove(game.w2[i], 2)

    # 更新画面
    draw()
    if result > 0:
        sleep(10)
        print('游戏结束')
        sys.exit(0)


def startGame():

    # 开始游戏的流程仍需处理

    connect()  # 连接到服务器
    
    # 账号/昵称
    ide.append(str(userAccount[0]))
    ide.append(str(target[0]))
    print('游戏加载中...')

    global game

    game = Action()

    sleep(3)

    game.reset()

    print('游戏开始了!')

    # 同时开启游戏和接受命令的线程

    getCmd = game.getCmd(game)

    tcpCliSock.settimeout(0.02)

    getCmd.start()

    g = threading.Thread(target=pgzrun.go())

    g.start()

    getCmd.join()

    g.join()


startGame()
