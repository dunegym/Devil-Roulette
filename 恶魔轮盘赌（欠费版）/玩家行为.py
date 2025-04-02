import pygame
import time
from 刷新 import write
from 刷新 import draw
def decide():
    x,y=0,0
    while x==0 or y==0:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                (x,y)=pygame.mouse.get_pos()
    if 0<x<150 and 600<y<700:
        return 9
    elif 150<x<300 and 600<y<700:
        return 10
    elif 300<x<400 and 600<y<700:
        return 1
    elif 400<x<500 and 600<y<700:
        return 2
    elif 500<x<600<y<700:
        return 3
    elif 600<x<700 and 600<y<700:
        return 4
    elif 600<y<700<x<800:
        return 5
    elif 800<x<900 and 600<y<700:
        return 6
    elif 900<x<1000 and 600<y<700:
        return 7
    elif 1000<x<1100 and 600<y<700:
        return 8
    else:
        return 0
#玩家决策
def action_p(screen,decision,bullet,tool_p,blood_p,blood_e,shooter,banned,handcuffs,aim,hit):
    if decision==9:
        write(screen,'你选择向自己开枪',(0,175))
        draw(screen,'图片/玩家瞄准自己.bmp',(300,100))
        draw(screen,'图片/选择开枪.bmp',(0,600))
        draw(screen,'图片/未选择.bmp',(150,600))
        time.sleep(1.5)
        if bullet[0]==0:
            write(screen,'......',(0,200))
            time.sleep(1.5)
            write(screen,'这是一发虚弹，你又获得枪权！',(0,225))
            del bullet[0]
        else:
            write(screen,'砰！',(0,200))
            draw(screen,'图片/玩家击中自己.bmp',(300,100))
            time.sleep(1.5)
            write(screen,'这是一发实弹，你弄巧成拙！',(0,225))
            draw(screen,'图片/玩家击伤自己.bmp',(300,100))
            blood_p-=bullet[0]
            del bullet[0]
            hit+=1
            shooter=1
        if 3 in banned:
            banned.remove(3)
    elif decision==10:
        write(screen, '你选择向恶魔开枪', (0,175))
        draw(screen, '图片/玩家瞄准恶魔.bmp', (300,100))
        draw(screen, '图片/未选择.bmp', (0,600))
        draw(screen, '图片/选择开枪.bmp', (150, 600))
        time.sleep(1.5)
        if bullet[0]==0:
            write(screen,'......',(0,200))
            time.sleep(1.5)
            write(screen, '这是一发虚弹，你错失良机！', (0,225))
            del bullet[0]
            aim+=1
            shooter=1
        else:
            write(screen, '砰！', (0,200))
            draw(screen, '图片/玩家击中恶魔.bmp', (300,100))
            time.sleep(1.5)
            write(screen, '这是一发实弹，成功击伤恶魔！', (0,225))
            draw(screen, '图片/玩家击伤恶魔.bmp', (300, 100))
            blood_e-=bullet[0]
            del bullet[0]
            aim+=1
            hit+=1
            shooter=1
        if 3 in banned:
            banned.remove(3)
    else:
        draw(screen,'图片/选择道具.bmp',(100*(decision+2),600))
        if tool_p[decision-1]==0:
            draw(screen,'图片/玩家使用华子.bmp',(300,100))
            write(screen,'你陪了大哥一根华子，生命加一',(0,175))
            blood_p+=1
        elif tool_p[decision-1]==1:
            draw(screen,'图片/玩家使用汽水.bmp',(300,100))
            if bullet[0]==0:
                write(screen,'你炫了一罐汽水，并退出一发虚弹',(0,175))
            else:
                write(screen,'你炫了一罐汽水，并退出一发实弹',(0,175))
            del bullet[0]
        elif tool_p[decision-1]==2:
            if bullet[0]==0:
                write(screen,'明察秋毫的你，发现下一发是虚弹',(0,175))
                draw(screen,'图片/玩家发现虚弹.bmp',(300,100))
            else:
                write(screen,'明察秋毫的你，发现下一发是实弹',(0,175))
                draw(screen,'图片/玩家发现实弹.bmp',(300,100))
        elif tool_p[decision-1]==3:
            draw(screen,'图片/玩家使用小刀.bmp',(300,100))
            write(screen,'你锯短了枪管，下一发子弹伤害翻倍',(0,175))
            bullet[0]*=2
            banned.append(3)
        elif tool_p[decision-1]==4:
            aim,hit=0,0
            draw(screen,'图片/玩家使用手铐.bmp',(300,100))
            write(screen,'你铐住了恶魔，获得两个枪权',(0,175))
            handcuffs=True
            banned.append(4)
        del tool_p[decision-1]
    if handcuffs is True:
        shooter=0
    if handcuffs is True and (aim==2 or hit==2):
        handcuffs=False
        banned.remove(4)
        shooter,aim,hit=1,0,0
    time.sleep(1.5)
    return bullet,tool_p,blood_p,blood_e,shooter,banned,handcuffs,aim,hit