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
class A:
    def __init__(self, n):
        self.n = n
    # def __str__(self):
    #     return str(self.n)
    def __int__(self):
        return 2

print(A(3))