import pgzrun
import random
# from print_Warrior import *
from backstage import *
from Roadpos_set import*
import threading
import time

# 显示页面大小
WIDTH = 1200
HEIGHT = 700

BOX = Rect((0, 250), (1200, 250))
# Rect(left, top, width, height) -> Rect
# Rect((left, top), (width, height)) -> Rect
RED = 200, 0, 0


# 创建造兵按钮 #长宽70
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


def draw():
    screen.clear()
    screen.fill("white")
    # screen.blit('bk', (0, 0))

    # 兵营部分
    screen.blit('arsenal', (20, 190))
    screen.blit('soldier', (21, 280))
    warrior_up.draw()  # (35, 350))
    archer_up.draw()   # (131, 350))
    warrior_mid.draw()  # (35, 350))
    archer_mid.draw()  # (131, 350))
    warrior_down.draw()  # (35, 350))
    archer_down.draw()  # (131, 350))


def on_mouse_down(pos):  # 造兵方式
    global target
    order_command = Command(game.turnID + 10, 0, 0)
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
    if order_command.CmdType > 0:
        game.ops1.put(order_command)
        sendOp(target, order_command)
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
    # 同时开启游戏和接受命令的线程
    receiveCmd = game.getdata()
    tcpCliSock.settimeout(0.1)
    receiveCmd.start()
    g = threading.Thread(target=pgzrun.go())
    g.start()
    receiveCmd.join()
    g.join()


startGame()
