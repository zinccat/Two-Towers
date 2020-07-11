# -*- coding: utf-8 -*-
# 这是没有GUI欢迎界面的游戏客户端, 不需安装easygui即可运行

import pgzrun
import random
from pgzero.actor import Actor
from pgzero.rect import Rect, ZRect
from pgzero.screen import Screen
from backstageNoGUI import flag, game, waiting, ide, clicktime, tcpCliSock, account, target, connect, Game, Command, syncTimeCount
from Roadpos_set import road
from config import *
import threading
from time import sleep, time
from math import ceil
import sys
screen: Screen  # 类型标注

# 升级按钮图标对象
upgradeIcon_main = Actor('upgrade')

upgradeIcon_up = Actor('upgrade')

upgradeIcon_mid = Actor('upgrade')

upgradeIcon_down = Actor('upgrade')

upgrade_button = [upgradeIcon_main, upgradeIcon_up,
                  upgradeIcon_mid, upgradeIcon_down]

# 血量图标对象
player_icon = Actor('人图标')
life_frame = Actor('血框')
life_block = Actor('血块')
life_icon = Actor('生命值图标')
DenfenseTower_icon = Actor('防御塔图标')
Base_icon = Actor('主塔图标')

# 云雾显示对象
yun1 = Actor('云上')
yun1.topleft = 250, 0
yun2 = Actor('云上中')
yun2.topleft = 250, 0
yun3 = Actor('云中')
yun3.topleft = 250, 0
yun4 = Actor('云中下')
yun4.topleft = 250, 0
yun5 = Actor('云下')
yun5.topleft = 250, 0

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


def draw():
    screen.clear()
    screen.fill("white")
    screen.blit('bk', (250, 0))

    # 金钱部分
    money_0.draw()
    money_2.draw()

    for i in range(game.money):
        money_1.topleft = 978 + 20 * i, 103
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
            if w.wType == 1:
                screen.blit('turret', (road[r][w.pos][w.wGrid]))
            elif w.wType == 2:
                screen.blit('knight' + str(ceil(10 * w.wLife /
                                                KnightLife)), (road[r][w.pos][w.wGrid]))
            elif w.wType == 3:
                screen.blit('archer' + str(ceil(10 * w.wLife /
                                                ArcherLife)), (road[r][w.pos][w.wGrid]))
        for w in game.w2[r]:
            if w.wType == 1:
                screen.blit('turret', (road[r][w.pos][w.wGrid]))
            elif w.wType == 2:
                screen.blit('knighte' + str(ceil(10 * w.wLife /
                                                 KnightLife)), (road[r][w.pos][w.wGrid]))
            elif w.wType == 3:
                screen.blit('archere' + str(ceil(10 * w.wLife /
                                                 ArcherLife)), (road[r][w.pos][w.wGrid]))

    #     云雾部分
    if game.life[6] > 0:
        yun3.draw()
        if game.life[5] > 0:
            yun2.draw()
        if game.life[7] > 0:
            yun5.draw()
    if game.life[5] > 0:
        yun1.draw()
    if game.life[7] > 0:
        yun5.draw()

    # 血量部分
    for j in range(8):
        if j > 3:
            dfx = 0
            dfy = -640
        else:
            dfx = 0
            dfy = 0

        life_frame.topleft = 25 + dfx, 440 + j * 70 + dfy
        life_icon.topleft = 24 + dfx, 421 + j * 70 + dfy

        if j <= 3:
            upgrade_button[j].topleft = 230 + dfx, 426 + j * 70 + dfy
            upgrade_button[j].draw()

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
    screen.draw.text(
        "player: %s" % ide[0], (52, 382), color='black', fontname='use', fontsize=20)
    screen.draw.text("player: %s" %
                     ide[1], (52, 22), color='black', fontname='use', fontsize=20)

# 鼠标点击特定位置时执行对应指令


def on_mouse_down(pos):  # 造兵方式
    global clicktime
    if clicktime == 0:
        clicktime = time()
    elif clicktime != 0 and time() - clicktime < 0.3:
        print("点的太快了!")  # 限制点击频率避免同步异常
        return
    else:
        clicktime = time()

    order_command = Command(game.turnID + 30, 0, [0])

    for i in range(4):
        if i == 0:
            if upgrade_button[i].collidepoint(pos) and game.money >= 10:
                game.money -= 10
                order_command.CmdType = 0
                order_command.turnID -= 10  # 相比造兵, 升级指令执行得快一些
                order_command.CmdStr = [0]
        else:
            if upgrade_button[i].collidepoint(pos) and game.money >= 5:
                game.money -= 5
                order_command.CmdType = 0
                order_command.turnID -= 10
                order_command.CmdStr = [i]

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

    if order_command.CmdType >= 0:
        game.ops1.put(order_command)
        game.sendCmd(target[0], order_command, 1)  # 发送指令给对方


def update(dt):
    # 初始化回合
    game.update()
    # 同步
    waiting()
    flag[0] -= 1
    if flag[0] == 0:
        game.sendCmd(target[0], '', 0)
    # 读取命令
    game.ReadCmd()
    # 检查可行的战斗
    game.BattleCheck()
    # 完成战斗
    game.BattleRun()
    # 武士死亡结算
    game.WarriorDeath()
    # 武士移动
    for i in range(3):
        game.WarriorMove(game.w1[i], 1)
        game.WarriorMove(game.w2[i], 2)
    # 主塔死亡结算
    result = game.BaseDeath()
    #若一方主塔死亡, 启动游戏终结机制
    # 更新画面
    draw()
    if result > 0:
        for i in range(5):
            # 多发几次同步指令确保对方正确显示游戏结果
            game.sendCmd(target[0], '', 0)
            sleep(0.2)
        msg = '游戏结束, '
        if result == 1:
            msg += '你赢了!'
        elif result == 2:
            msg += '你挂了!'
        tcpCliSock.close()
        print(msg)
        print('再见!')
        sys.exit(0)


def on_music_end():
    music.play_once(random.choice(['东方_1', '东方_2']))

def startGame():
    # 开始游戏的流程仍需处理
    connect()  # 连接到服务器
    # 账号/昵称
    ide.append(str(account[0]))
    ide.append(str(target[0]))
    global game
    # 创建新游戏并初始化
    game = Game()
    game.reset()
    # 打开通信接口
    getCmd = game.getCmd(game)  # 命令接收线程
    getCmd.start()
    game.sendCmd(target[0], '', 0)
    waiting()  # 等待对手上线
    print('游戏开始了!')
    # 放音乐
    music.set_volume(0.3)
    music.play_once('bgm_1')
    # 同时开启游戏和接受命令的线程
    g = threading.Thread(target=pgzrun.go())  # 游戏线程
    g.start()
    getCmd.join()
    g.join()


startGame()
