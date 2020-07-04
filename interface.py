import pgzrun
import random


WIDTH = 1200
HEIGHT = 700

BOX = Rect((0,250),(1200,250)) 
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



# 造兵列表
makeSoldier = []



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
    #screen.draw.text("A R S E N A L", (20, 200), color="pink", gcolor="VioletRed2", fontsize=50)

    #建筑信息



def on_mouse_down(pos): #造兵方式
    if warrior_up.collidepoint(pos):
        makeSoldier = [2, 1]
    if archer_up.collidepoint(pos):
        makeSoldier = [3, 1]
    if warrior_mid.collidepoint(pos):
        makeSoldier = [2, 2]
    if archer_mid.collidepoint(pos):
        makeSoldier = [3, 2]
    if warrior_down.collidepoint(pos):
        makeSoldier = [2, 3]
    if archer_down.collidepoint(pos):
        makeSoldier = [3, 3]



def update():
    draw()


pgzrun.go()
