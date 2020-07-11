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
UpgradeRate = 1.1

# 造钱速度加成 在特定回合造钱速度*特定倍数
AccTurn1 = 7500
AccTurn2 = 14000
AccSpeed1 = 1.5
AccSpeed2 = 2

#下面为各种游戏角色的参数, 以后调参都在这里进行

# 主塔 0
BaseAttack = 20
BaseDefence = 6
BaseLife = INF
BaseRange = 10
BasemCD = 0
BaseaCD = 40
BasePos = 0
TrueBaseLife = 300

# 防御塔 1
TurretAttack = 30
TurretDefence = 10
TurretLife = 150
TurretRange = 10
TurretmCD = 0
TurretaCD = 25
TurretPos = 15

# 骑士 2
KnightAttack = 20
KnightDefence = 15
KnightLife = 75
KnightRange = 1
KnightmCD = 40
KnightaCD = 50

# 弓箭手 3
ArcherAttack = 15
ArcherDefence = 10
ArcherLife = 45
ArcherRange = 8
ArchermCD = 25
ArcheraCD = 20
