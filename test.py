import pgzrun
import random
from print_Warrior import *
from backstage import*

# 显示页面大小
WIDTH = 1200
HEIGHT = 700

BOX = Rect((0, 250), (1200, 250))
# Rect(left, top, width, height) -> Rect
# Rect((left, top), (width, height)) -> Rect
RED = 200, 0, 0


# 创建造兵按钮 #长宽70
warrior_up = Actor('purchase', (70, 385))
archer_up = Actor('purchase copy', (166, 385))
warrior_mid = Actor('purchase copy 2', (70, 510))
archer_mid = Actor('purchase copy 3', (166, 510))
warrior_down = Actor('purchase copy 4', (70, 635))
archer_down = Actor('purchase copy 5', (166, 635))
warrior_up.x = 70
warrior_up.y = 385
archer_up.x = 166
archer_up.y = 385


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


def on_mouse_down(pos):  # 造兵方式
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


def update():
    game.update()
    game.ReadCmd()
    draw()


game = Action()
game.reset()
pgzrun.go()
