# -*- coding: utf-8 -*-
# Warrior类的内容写在这里


class Warrior:
    def __init__(self, wtype, wside):
        self.wType = wtype
        self.wSide = wside

#type 1
class Knight(Warrior):
    def __init__(self, wtype, wside):
        super().__init__(wtype, wside)
        self.wAttack = 10
        self.wLife = 10
        self.wSpeed = 10
        self.mCD = 0
        self.aCD = 0

#type 2
class Archer(Warrior):
    def __init__(self, wtype, wside):
        super().__init__(wtype, wside)
        self.wAttack = 10
        self.wLife = 10
        self.wSpeed = 10
        self.mCD = 0
        self.aCD = 0