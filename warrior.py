# -*- coding: utf-8 -*-
# Warrior类的内容写在这里

from config import *

# 父类型


class Warrior:
    def __init__(self, wtype, wteam):
        self.wType = wtype
        self.wTeam = wteam
        if wteam == 1:
            self.pos = 0
        else:
            self.pos = mLen #这里需要改机制, 判断在哪条路上, 可以考虑在这里加一个路的参数
        self.attacked = 0 #本回合是否攻击

# type 0
# 主塔


class Base(Warrior):
    def __init__(self, wtype, wteam):
        super().__init__(wtype, wteam)
        self.wAttack = 10
        self.wLife = 10
        self.wSpeed = 10
        self.wASpeed = 10
        self.mCD = 0
        self.aCD = 0

# type 1
# 防御塔


class DefenseTower(Warrior):
    def __init__(self, wtype, wteam):
        super().__init__(wtype, wteam)
        self.wAttack = 10
        self.wLife = 10
        self.wSpeed = 10
        self.wASpeed = 10
        self.mCD = 0
        self.aCD = 0
        self.pos = 10


# type 2
# 骑士


class Knight(Warrior):
    def __init__(self, wtype, wteam):
        super().__init__(wtype, wteam)
        self.wAttack = 10
        self.wLife = 10
        self.wSpeed = 10
        self.wASpeed = 10
        self.mCD = 0
        self.aCD = 0

# type 3
# 弓箭手


class Archer(Warrior):
    def __init__(self, wtype, wteam):
        super().__init__(wtype, wteam)
        self.wAttack = 10
        self.wLife = 10
        self.wSpeed = 10
        self.wASpeed = 10
        self.mCD = 0
        self.aCD = 0
