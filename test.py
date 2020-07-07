# 所有跑单函数测试的操作都在这里进行
from backstage import *
game = Action()
c1 = Command(1, 2, [0])
c2 = Command(2, 2, [0])
game.ops1.put(c1)
game.ops1.put(c2)
print(game.ops1.get().turnID)