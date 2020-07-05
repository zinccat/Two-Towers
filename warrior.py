# -*- coding: utf-8 -*-

# Warrior类的内容写在这里


from config import *


# 父类型


class Warrior:

    def __init__(self, wtype, wteam, wgrid, wpos):

        self.wType = wtype
        self.wTeam = wteam
        self.wGrid = wgrid  # 在三个格子中的哪个 0 1 2
        self.pos = wpos
        self.attacked = 0  # 本回合是否攻击


# type 0

# 主塔


class Base(Warrior):

    def __init__(self, wteam, wgrid, wpos=0):

        super().__init__(0, wteam, wgrid, wpos)

        self.wAttack = BaseAttack

        self.wLife = BaseLife

        self.wRange = BaseRange

        self.mCD = BasemCD

        self.aCD = BaseaCD

        self.pos = BasePos

    def updatemCD(self):
        if self.mCD > 0:
            self.mCD -= 1
        else:
            self.mCD = BasemCD

    def updateaCD(self):
        if self.aCD > 0:
            self.aCD -= 1
        else:
            self.aCD = BaseaCD


# type 1

# 防御塔


class DefenseTower(Warrior):

    def __init__(self, wteam, wgrid=2, wpos=0):

        super().__init__(1, wteam, wgrid, wpos)

        self.wAttack = DefenseTowerAttack

        self.wLife = DefenseTowerLife

        self.wRange = DefenseTowerRange

        self.mCD = DefenseTowermCD

        self.aCD = DefenseToweraCD

        self.pos = DefenseTowerPos

    def updatemCD(self):
        if self.mCD > 0:
            self.mCD -= 1
        else:
            self.mCD = DefenseTowermCD

    def updateaCD(self):
        if self.aCD > 0:
            self.aCD -= 1
        else:
            self.aCD = DefenseToweraCD

# type 2

# 骑士


class Knight(Warrior):

    def __init__(self, wteam, wgrid, wpos=0):

        super().__init__(2, wteam, wgrid, wpos)

        self.wAttack = KnightAttack

        self.wLife = KnightLife

        self.wRange = KnightRange

        self.mCD = KnightmCD

        self.aCD = KnightaCD

    def updatemCD(self):
        if self.mCD > 0:
            self.mCD -= 1
        else:
            self.mCD = KnightmCD

    def updateaCD(self):
        if self.aCD > 0:
            self.aCD -= 1
        else:
            self.aCD = KnightaCD


# type 3

# 弓箭手


class Archer(Warrior):

    def __init__(self, wteam, wgrid, wpos=0):

        super().__init__(3, wteam, wgrid, wpos)

        self.wAttack = ArcherAttack

        self.wLife = ArcherLife

        self.wRange = ArcherRange

        self.mCD = ArchermCD

        self.aCD = ArcheraCD

    def updatemCD(self):
        if self.mCD > 0:
            self.mCD -= 1
        else:
            self.mCD = ArchermCD

    def updateaCD(self):
        if self.aCD > 0:
            self.aCD -= 1
        else:
            self.aCD = ArcheraCD
