# -*- coding: utf-8 -*-
# 命令接口


class op:
    def __init__(self, turnID, team, moveType, additionalInfo):
        self.turnID = turnID
        self.team = team
        self.moveType = moveType
        self.additionalInfo = additionalInfo
    # 比较函数, 确定执行命令的优先级
    def __cmp__(self, other):
        self.turnID < other.turnID