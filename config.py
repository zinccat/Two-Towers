# -*- coding: utf-8 -*-
# 在这里设置了游戏运行时所调用的参数

# 定义无穷大
INF = 10000000

# 地图大小
MapLen = None

# 主轴长度
mLen = 48

# 侧轴长度
aLen = 49

# mCD参数 mCD = C / wSpeed
C = 100

# 防御塔据原点距离
dLen = 10

# 奖励
TurretReward = 3  # 击杀防御塔
WarriorReward = 0.5  # 击杀士兵

# 主塔攻击衰减比例, 每有一个本阵营防御塔被攻破就减少1/c的攻击
AttackReduction = 4

# 塔升级参数
UpgradeRate = 1.2

#下面为各种游戏角色的参数, 以后调参都在这里进行

# 主塔 0
BaseAttack = 20
BaseDefence = 6
BaseLife = INF
BaseRange = 10
BasemCD = 0
BaseaCD = 40
BasePos = 0
TrueBaseLife = 500

# 防御塔 1
TurretAttack = 12
TurretDefence = 8
TurretLife = 100
TurretRange = 10
TurretmCD = 0
TurretaCD = 30
TurretPos = 10

# 骑士 2
KnightAttack = 12
KnightDefence = 6
KnightLife = 50
KnightRange = 1
KnightmCD = 40
KnightaCD = 50

# 弓箭手 3
ArcherAttack = 10
ArcherDefence = 4
ArcherLife = 30
ArcherRange = 8
ArchermCD = 30
ArcheraCD = 30
