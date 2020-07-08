# 所有跑单函数测试的操作都在这里进行
'''
from backstage import *
game = Action()
c1 = Command(1, 2, [0])
c2 = Command(2, 2, [0])
game.ops2.put(c1)
game.ops2.put(c2)
print(game.ops2.get().turnID)
print(2==[2][0])
'''
'''
import easygui as gui
gui.msgbox('你好!欢迎来玩我们的小游戏')
t = gui.enterbox(msg = '请在下方输入用户名并点击确认', title = '注册')
print(t)
'''
import time
while int(time.time()) % 60 != 0:
    time.sleep(1)
