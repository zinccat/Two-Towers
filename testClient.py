import pgzrun
import random
from print_Warrior import *
from backstage import *
from gameClient import *

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
warrior_up.x = 70
warrior_up.y = 385
archer_up.x = 166
archer_up.y = 385


def draw():
    screen.clear()
    screen.fill("white")
    #screen.blit('bk', (0, 0))
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
        chat(target, order_command)
        # 此处添加发送命令语句


def update():
    game.update(game.w1)
    game.update(game.w2)
    # 此处添加接收命令语句
    game.ReadCmd(game.ops1, game.w1, 1)
    game.ReadCmd(game.ops2, game.w2, 2)
    game.BattleCheck()
    game.BattleRun(game.BattleList)
    result = game.BaseDeath()
    if result > 0:
        game.end(result)
    game.WarriorDeath(game.w1)
    game.WarriorDeath(game.w2)
    posOccu = dict()  # 记录某格是否被敌方占领
    for i in range(3):
        game.WarriorMove(game.w1[i], posOccu, 1)
        game.WarriorMove(game.w2[i], posOccu, 2)
    draw()


try:
    tcpCliSock.connect(ADDR)
    print('Connected with server')
    while True:
        reg = register()
        if reg:
            break
except:
    print('error')
    sys.exit(0)
target = input('想打谁?')

game = Action()
game.reset()
g = threading.Thread(target=pgzrun.go())
receiveCmd = threading.Thread(target=game.ReceiveCmd())
receiveCmd.start()
g.start()
# pgzrun.go()
# g.join()
# receiveCmd.join(())
