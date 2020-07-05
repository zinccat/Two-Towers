import pgzrun
import random


WIDTH = 1200
HEIGHT = 700

# 图标对象
money_0 = Actor('金钱框')
money_0.topleft = 25, 200
money_2 = Actor('钱币图标')
money_2.topleft = 25, 177
money_1 = Actor('金钱块')

Money = 0       # 设置成interface.py的全局变量
time_count = 0  # 记录帧数


def draw():
    screen.clear()
    screen.fill((128, 128, 128))
    money_0.draw()
    money_2.draw()
    for i in range(Money):
        money_1.topleft = 28+20*i, 203
        money_1.draw()
    screen.draw.text("Money:%d/10" % Money, (50, 182))


def update():
    global time_count
    time_count += 1
    if time_count == 60:
        time_count = 0
        if Money < 10:
            Money_accumulate(1)


# 钱数变化的函数
def Money_accumulate(x):
    global Money
    Money += x


''' 以下整合到interface的on_mouse_down()里

def on_mouse_down(pos):
    global Money
    Money -= random.randint(1,Money)
'''

# 记得加一句检测语句在interface的on_mouse_down()里，并且对global Money进行修改

pgzrun.go()
