import pgzrun

# 好多数值都用的拼音...

WIDTH=1200
HEIGHT=700

# 账号/昵称
renxiang=Actor('人图标')
#随便输的
wanjia1=str("xxx")
wanjia2=str("yyy")

life0=Actor('血框')
life1=Actor('血块')
life2=Actor('生命值图标')

#这个生命值，随便编的名称随便设的数字，整合的时候要搞这里,
# 0123分别是己方base和防御塔123,4567是敌方
lifezhi=[1,3,6,8,10,2,7,4]

def draw():
    screen.clear()
    screen.fill((128,128,128))
  
    for j in range(8):
        if j>3:
            dfx=945
            dfy=-400
        else:
            dfx=0
            dfy=0
        life0.topleft=25+dfx,300+j*70+dfy
        life2.topleft=27+dfx,281+j*70+dfy
        life0.draw()
        life2.draw()
        for i in range(lifezhi[j]):
            life1.topleft=27+20*i+dfx,303+70*j+dfy
            life1.draw()
        screen.draw.text("Life:%d/10" % lifezhi[j],(50+dfx,282+70*j+dfy))
# 账号/昵称
    renxiang.topleft=25,600
    renxiang.draw()
    renxiang.topleft=970,100
    renxiang.draw()    
    screen.draw.text("player: %s" % wanjia1,(50,602))
    screen.draw.text("player: %s" % wanjia2,(995,102))

#钱数(血量)变化的函数
def lifezhibh(j,lfbh):
    lifezhi[j]=lifezhi[j]+lfbh

# 
def on_mouse_down():
    if lifezhi[3]>=2:
        lifezhibh(3,-2)


pgzrun.go()