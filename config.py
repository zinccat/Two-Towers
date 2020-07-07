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
BaseAttack = 50
BaseLife = INF
BaseRange = 10
BasemCD = 0
BaseaCD = 5
BasePos = 0
TrueBaseLife = 500

# 防御塔 1
TurretAttack = 30
TurretLife = 100
TurretRange = 20
TurretmCD = 0
TurretaCD = 5
TurretPos = 10

# 骑士 2
KnightAttack = 10
KnightLife = 100
KnightRange = 10
KnightmCD = 30
KnightaCD = 10

# 弓箭手 3
ArcherAttack = 10
ArcherLife = 100
ArcherRange = 10
ArchermCD = 20
ArcheraCD = 10
