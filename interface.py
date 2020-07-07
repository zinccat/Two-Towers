import pgzrun
import random
from Roadpos_set import*
from backstage import*

game = Action()

for i in range(50):
    game.w1[0].append(Knight(1, i % 3 + 1, i))

for i in range(49):
    game.w2[random.randint(0, 2)].append(Archer(1, random.randint(1, 3), i))


# 账号/昵称
wanjia1 = str("xxx")
wanjia2 = str("yyy")


# 血量图标对象
player_icon = Actor('人图标')
life_frame = Actor('血框')
life_block = Actor('血块')
life_icon = Actor('生命值图标')
DenfenseTower_icon = Actor('防御塔图标')
Base_icon = Actor('主塔图标')


life_display = [0, 0, 0, 0, 0, 0, 0, 0]
# 更新血量数值


def update_life():
    life_display[0] = TrueBaseLife
    life_display[4] = TrueBaseLife
    for i in range(3):
        life_display[0] -= int(INF - game.w1[i][0].wLife)
        life_display[4] -= int(INF - game.w2[i][0].wLife)
        life_display[i + 1] = game.w1[i][1].wLife
        life_display[i + 5] = game.w2[i][1].wLife


# 金钱图标对象
money_0 = Actor('金钱框')
money_0.topleft = 975, 100
money_2 = Actor('钱币图标')
money_2.topleft = 975, 77
money_1 = Actor('金钱块')

Money = 0
timeCount = 0


# 显示页面大小
WIDTH = 1200
HEIGHT = 700


# 创建造兵按钮 #长宽70

warrior_up = Actor('小兵', (70 + 960, 385))
archer_up = Actor('弓箭手', (166 + 960, 385))
warrior_mid = Actor('小兵', (70 + 960, 510))
archer_mid = Actor('弓箭手', (166 + 960, 510))
warrior_down = Actor('小兵', (70 + 960, 635))
archer_down = Actor('弓箭手', (166 + 960, 635))


# 创建小兵对象
Knight_image = Actor('小兵色块')
Archer_image = Actor('弓箭手色块')
worrior_image = [0, '防御塔色块', '小兵色块', '弓箭手色块']


def draw():
    screen.clear()
    screen.fill("white")
    screen.blit('bk', (250, 0))

    # 金钱部分
    money_0.draw()
    money_2.draw()
    for i in range(game.money):
        money_1.topleft = 978+20*i, 103
        money_1.draw()
    screen.draw.text("Money:%d/10" % game.money, (1000, 82), color='black')

    # 兵营部分
    screen.blit('arsenal', (20 + 960, 190))
    screen.blit('soldier', (21 + 960, 280))
    warrior_up.draw()
    archer_up.draw()
    warrior_mid.draw()
    archer_mid.draw()
    warrior_down.draw()
    archer_down.draw()

    # 兵种部分
    for r in range(3):
        for w in game.w1[r]:
            if w != game.w1[r][0]:
                screen.blit(worrior_image[w.wType], (road[r][w.pos][w.wGrid]))
        for w in game.w2[r]:
            if w != game.w2[r][0]:
                screen.blit(worrior_image[w.wType], (road[r][w.pos][w.wGrid]))

    # 血量部分

    for j in range(8):
        if j > 3:
            dfx = 0
            dfy = -640
        else:
            dfx = 0
            dfy = 0
        life_frame.topleft = 25+dfx, 440+j*70+dfy
        life_icon.topleft = 24+dfx, 421+j*70+dfy
        if j % 4 == 0:
            Base_icon.topleft = 211+dfx, 416+j*70+dfy
            Base_icon.draw()
            screen.draw.text("Base", (170+dfx, 422+70*j+dfy), color='black')
        else:
            DenfenseTower_icon.topleft = 218+dfx, 417+j*70+dfy
            DenfenseTower_icon.draw()
            if (j-1) % 4 == 0:
                screen.draw.text(
                    "Turret(top)", (138+dfx, 422+70*j+dfy), color='black')
            elif (j-2) % 4 == 0:
                screen.draw.text(
                    "Turret(mid)", (138+dfx, 422+70*j+dfy), color='black')
            else:
                screen.draw.text(
                    "Turret(bot)", (138+dfx, 422+70*j+dfy), color='black')
        life_frame.draw()
        life_icon.draw()
        for i in range(life_display[j]):
            if j % 4 == 0:
                life_block.topleft = 27+2*i//5+dfx, 443+70*j+dfy
            else:
                life_block.topleft = 27+2*i+dfx, 443+70*j+dfy
            life_block.draw()
        if j % 4 == 0:
            screen.draw.text(
                "Life:%d/500" % life_display[j], (43+dfx, 422+70*j+dfy), color='black')
        else:
            screen.draw.text(
                "Life:%d/100" % life_display[j], (43+dfx, 422+70*j+dfy), color='black')
    player_icon.topleft = 27, 380
    player_icon.draw()
    player_icon.topleft = 27, 20
    player_icon.draw()
    screen.draw.text("player: %s" % wanjia1, (52, 382), color='black')
    screen.draw.text("player: %s" % wanjia2, (52, 22), color='black')


def on_mouse_down(pos):  # 造兵方式
    order_command = Command(game.turnID, 0, [0])
    if warrior_up.collidepoint(pos) and game.money >= 2:
        game.money -= 2
        order_command.CmdType = 2
        order_command.CmdStr = [1]
    elif archer_up.collidepoint(pos) and game.money >= 3:
        game.money -= 3
        order_command.CmdType = 3
        order_command.CmdStr = [1]
    elif warrior_mid.collidepoint(pos) and game.money >= 2:
        game.money -= 2
        order_command.CmdType = 2
        order_command.CmdStr = [2]
    elif archer_mid.collidepoint(pos) and game.money >= 3:
        game.money -= 3
        order_command.CmdType = 3
        order_command.CmdStr = [2]
    elif warrior_down.collidepoint(pos) and game.money >= 2:
        game.money -= 2
        order_command.CmdType = 2
        order_command.CmdStr = [3]
    elif archer_down.collidepoint(pos) and game.money >= 3:
        game.money -= 3
        order_command.CmdType = 3
        order_command.CmdStr = [3]
    if order_command.CmdType > 0:

        game.ops1.put(order_command)

        sendOp(target[0], order_command)


def update():

    update_life()

    global timeCount
    if game.money < 10:
        game.timeCount += 1
        if game.timeCount == 60:
            game.MoneyAccumulate(1)
            game.timeCount = 0

    # 回合数更新
    game.turnID += 1

    # 绘图
    draw()


pgzrun.go()


# 需要修改 1. update函数中money （已修改） 2.玩家ID  3.各种字体颜色 4.地图侧方路径

