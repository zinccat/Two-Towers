import pgzrun
from backstage import*
from config import*

game = Action()

# 好多数值都用的拼音...
# 账号/昵称的显示也在这里面

WIDTH = 1200
HEIGHT = 700

# 账号/昵称
player_icon = Actor('人图标')

# 随便输的
wanjia1 = str("xxx")
wanjia2 = str("yyy")

life_frame = Actor('血框')
life_block = Actor('血块')
life_icon = Actor('生命值图标')
DenfenseTower_icon = Actor('防御塔图标')
Base_icon = Actor('主塔图标')

# 这个生命值，随便编的名称随便设的数字，整合的时候要搞这里,
# 0123分别是己方base和防御塔123,4567是敌方


game = Action()

life_display = [0, 0, 0, 0, 0, 0, 0, 0]

def update_life():
    life_display[0] = TrueBaseLife
    life_display[4] = TrueBaseLife
    for i in range (3):
        life_display[0] -= int(INF - game.w1[i][0].wLife)
        life_display[4] -= int(INF - game.w2[i][0].wLife)
        life_display[i + 1] = game.w1[i][1].wLife
        life_display[i + 5] = game.w2[i][1].wLife

update_life()
print(life_display)


def draw():
    screen.clear()
    screen.fill((128, 128, 128))

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
            screen.draw.text("Base", (170+dfx, 422+70*j+dfy))
        else:
            DenfenseTower_icon.topleft = 218+dfx, 417+j*70+dfy
            DenfenseTower_icon.draw()
            if (j-1) % 4 == 0:
                screen.draw.text("Turret(top)", (138+dfx, 422+70*j+dfy))
            elif (j-2) % 4 == 0:
                screen.draw.text("Turret(mid)", (138+dfx, 422+70*j+dfy))
            else:
                screen.draw.text("Turret(bot)", (138+dfx, 422+70*j+dfy))
        life_frame.draw()
        life_icon.draw()
        for i in range(life_display[j]):
            if j%4==0:
                life_block.topleft = 27+2*i//5+dfx, 443+70*j+dfy
            else:
                life_block.topleft = 27+2*i+dfx, 443+70*j+dfy
            life_block.draw()
        if j%4==0:
            screen.draw.text("Life:%d/500" % life_display[j], (43+dfx, 422+70*j+dfy))
        else:
            screen.draw.text("Life:%d/100" % life_display[j], (43+dfx, 422+70*j+dfy))
        
# 账号/昵称
    player_icon.topleft = 27, 380
    player_icon.draw()
    player_icon.topleft = 27, 20
    player_icon.draw()
    screen.draw.text("player: %s" % wanjia1, (52, 382))
    screen.draw.text("player: %s" % wanjia2, (52, 22))



# 钱数(血量)变化的函数
def life_change(j, lfbh):
    life_display[j] = life_display[j]+lfbh


pgzrun.go()

