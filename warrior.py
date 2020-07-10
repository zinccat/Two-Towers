# -*- coding: utf-8 -*-
# 在这里定义的是游戏中角色的基本单位---Warrior的类

from config import *

# 父类型


class Warrior:

    def __init__(self, wtype, wteam, wgrid, wpos):

        self.wType = wtype
        self.wTeam = wteam
        self.wGrid = wgrid  # 在三个格子中的哪个 1 2 3
        self.pos = wpos
        self.attacked = 0  # 本回合是否攻击
        self.couldMove = 1


# type 0

# 主塔


class Base(Warrior):

    def __init__(self, wteam, wgrid, wpos=BasePos):

        super().__init__(0, wteam, wgrid, wpos)

        self.wAttack = BaseAttack
        self.wDefence = BaseDefence
        self.wLife = BaseLife
        self.wRange = BaseRange
        self.mCD = BasemCD
        self.aCD = BaseaCD
        self.pos = wpos

    def updatemCD(self, moved):
        if self.mCD > 0:
            self.mCD -= 1
        if moved:
            self.mCD = BasemCD

    def updateaCD(self, attacked):
        if self.aCD > 0:
            self.aCD -= 1
        if attacked:
            self.aCD = BaseaCD


# type 1

# 防御塔


class Turret(Warrior):

    def __init__(self, wteam, wgrid=2, wpos=TurretPos):

        super().__init__(1, wteam, wgrid, wpos)
        self.wAttack = TurretAttack
        self.wDefence = TurretDefence
        self.wLife = TurretLife
        self.wRange = TurretRange
        self.mCD = TurretmCD
        self.aCD = TurretaCD
        self.pos = wpos

    def updatemCD(self, moved):
        if self.mCD > 0:
            self.mCD -= 1
        if moved:
            self.mCD = TurretmCD

    def updateaCD(self, attacked):
        if self.aCD > 0:
            self.aCD -= 1
        if attacked:
            self.aCD = TurretaCD

# type 2

# 骑士


class Knight(Warrior):

    def __init__(self, wteam, wgrid, wpos=0):
        super().__init__(2, wteam, wgrid, wpos)
        self.wAttack = KnightAttack
        self.wDefence = KnightDefence
        self.wLife = KnightLife
        self.wRange = KnightRange
        self.mCD = KnightmCD
        self.aCD = KnightaCD

    def updatemCD(self, moved):
        if self.mCD > 0:
            self.mCD -= 1
        if moved:
            self.mCD = KnightmCD

    def updateaCD(self, attacked):
        if self.aCD > 0:
            self.aCD -= 1
        if attacked:
            self.aCD = KnightaCD


# type 3

# 弓箭手


class Archer(Warrior):

    def __init__(self, wteam, wgrid, wpos=0):
        super().__init__(3, wteam, wgrid, wpos)
        self.wAttack = ArcherAttack
        self.wDefence = ArcherDefence
        self.wLife = ArcherLife
        self.wRange = ArcherRange
        self.mCD = ArchermCD
        self.aCD = ArcheraCD

    def updatemCD(self, moved):
        if self.mCD > 0:
            self.mCD -= 1
        if moved:
            self.mCD = ArchermCD

    def updateaCD(self, attacked):
        if self.aCD > 0:
            self.aCD -= 1
        if attacked:
            self.aCD = ArcheraCD
