import pgzrun
import random
from print_Warrior import *
from backstage import*


turnID = 0 # 该命令所生效的回合

# order_command = Command(turnID, CmdType, CmdStr)


# 显示页面大小
WIDTH = 1200
HEIGHT = 700

BOX = Rect((0,250),(1200,250)) 
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
    screen.blit('bk', (0, 0))
    # 兵营部分
    screen.blit('arsenal', (20, 190))
    screen.blit('soldier', (21, 280))
    warrior_up.draw()    #(35, 350))
    archer_up.draw()   # (131, 350))
    warrior_mid.draw() #(35, 350))
    archer_mid.draw()  #(131, 350))
    warrior_down.draw()  #(35, 350))
    archer_down.draw()  #(131, 350))

    '''
    # 打印小兵
    for i in range(69):
        if road_1[0][i]['Knight'] != 0 or road_1[0][i]['Archer'] != 0:
            for k in range (road_1[0][i]['Knight']):

            for k in range (road_1[0][i]['Archer']):

        if road_1[2][i]['Knight'] != 0 or road_1[2][i]['Archer'] != 0:
            for k in range (road_1[2][i]['Knight']):

            for k in range (road_1[2][i]['Archer']):
        
        if road_2[0][i]['Knight'] != 0 or road_2[0][i]['Archer'] != 0:
            for k in range (road_2[0][i]['Knight']):

            for k in range (road_2[0][i]['Archer']):
        
        if road_2[2][i]['Knight'] != 0 or road_2[2][i]['Archer'] != 0:
            for k in range (road_2[2][i]['Knight']):

            for k in range (road_2[2][i]['Archer']):

    for i in range(49):
        if road_1[1][i]['Knight'] != 0 or road_1[1][i]['Archer'] != 0:
            for k in range (road_1[1][i]['Knight']):

            for k in range (road_1[1][i]['Archer']):

        if road_2[1][i]['Knight'] != 0 or road_2[1][i]['Archer'] != 0:
            for k in range (road_2[1][i]['Knight']):

            for k in range (road_2[1][i]['Archer']):        
    '''
    #打印小兵结束

    
    #screen.draw.text("A R S E N A L", (20, 200), color="pink", gcolor="VioletRed2", fontsize=50)

    #建筑信息



def on_mouse_down(pos): #造兵方式
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
    else:
        order_command = []    # 这里需要商讨




'''
# 读取三条线路信息

road_1 = [[], [], []] # 己方的小兵 第三阶的dict代表（兵种，个数）
road_2 = [[], [], []] # 地方的小兵



tower_1 
tower_2 



# 初始化路径信息
def init_soldier():
    for i in range(69):
        road_1[0].append({'Knight': 0, 'Archer': 0})
        road_1[2].append({'Knight': 0, 'Archer': 0})
        road_2[0].append({'Knight': 0, 'Archer': 0})
        road_2[2].append({'Knight': 0, 'Archer': 0})

    for i in range(49):
        road_1[1].append({'Knight': 0, 'Archer': 0})
        road_2[1].append({'Knight': 0, 'Archer': 0})
    print(road_1, "\n", road_2) 


def save_soldier():
    for i in range(3):
        for k in range(len(w1[i])):
            if w1[i][k].wtype == 2:
                road_1[i][w1[i][k].pos]['Knight'] += 1
            if w1[i][k].wtype == 3:
                road_1[i][w1[i][k].pos]['Archer'] += 1
        for k in range(len(w2[i])):
            if w2[i][k].wtype == 2:
                road_2[i][w2[i][k].pos]['Knight'] += 1
            if w1[i][k].wtype == 3:
                road_2[i][w2[i][k].pos]['Archer'] += 1
        


def print_soldier():
    warrior_up.draw() 


'''


# 返回Command
def info():
    return order_command









def update():
    global turnID
    turnID += 1
    draw()









pgzrun.go()

