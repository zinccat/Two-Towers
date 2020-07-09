# -*- coding: utf-8 -*-
# 可以调节的参数写在这里

# 无穷大
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

#下面为各种游戏角色的参数, 以后调参都在这里进行

# 主塔 0
BaseAttack = 30
BaseLife = INF
BaseRange = 10
BasemCD = 0
BaseaCD = 20
BasePos = 0
TrueBaseLife = 500

# 防御塔 1
TurretAttack = 5
TurretLife = 100
TurretRange = 10
TurretmCD = 0
TurretaCD = 30
TurretPos = 10

# 骑士 2
KnightAttack = 8
KnightLife = 80
KnightRange = 1
KnightmCD = 40
KnightaCD = 50

# 弓箭手 3
ArcherAttack = 5
ArcherLife = 30
ArcherRange = 8
ArchermCD = 30
ArcheraCD = 30