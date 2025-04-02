import random
import time
from 刷新 import write
from 刷新 import draw
class Bullet:
    def __init__(self,bullet,bullets):
        self.bullet=bullet
        while abs(self.bullet.count(1)-self.bullet.count(0))>3 or self.bullet==[]:
            self.bullet=[]
            for i in range(bullets):
                j = random.randint(0, 1)
                self.bullet.append(j)
    def trans_bullet(self):
        return self.bullet,self.bullet.count(1),self.bullet.count(0)
#装弹，并将弹匣信息传回主程序
class Tool:
    def __init__(self,tool_p,tool_e,tools):
        self.tool_p=tool_p
        self.tool_e=tool_e
        for i in range(tools):
            if len(self.tool_p)==8:
                break
            tool=random.randint(0,4)
            self.tool_p.append(tool)
        for i in range(tools):
            if len(self.tool_e)==8:
                break
            tool=random.randint(0,4)
            self.tool_e.append(tool)
    def trans_tool(self):
        return self.tool_p,self.tool_e
#分发道具，并将道具信息传回主程序
def action_e(screen,decision,bullet,tool_e,blood_p,blood_e,shooter,banned,handcuffs,aim=0,hit=0,find=0):
    if decision==9:
        write(screen,'恶魔选择向你开枪',(0,175))
        draw(screen,'图片/恶魔瞄准玩家.bmp',(300,100))
        draw(screen,'图片/选择开枪.bmp',(0,600))
        draw(screen,'图片/未选择.bmp',(150,600))
        time.sleep(1.5)
        if bullet[0]==0:
            write(screen,'......',(0,200))
            time.sleep(1.5)
            write(screen,'这是一发虚弹，你躲过一劫！',(0,225))
            del bullet[0]
            aim+=1
            shooter=0
        else:
            write(screen,'砰！',(0,200))
            draw(screen,'图片/恶魔击中玩家.bmp',(300,100))
            time.sleep(1.5)
            write(screen,'这是一发实弹，你被击伤了！',(0,225))
            draw(screen,'图片/恶魔击伤玩家.bmp',(300,100))
            blood_p-=bullet[0]
            del bullet[0]
            aim+=1
            hit+=1
            shooter=0
        if 3 in banned:
            banned.remove(3)
    elif decision==10:
        write(screen, '恶魔选择向自己开枪', (0, 175))
        draw(screen, '图片/恶魔瞄准自己.bmp', (300, 100))
        draw(screen, '图片/未选择.bmp', (0, 600))
        draw(screen, '图片/选择开枪.bmp', (150, 600))
        time.sleep(1.5)
        if bullet[0]==0:
            write(screen,'......',(0,200))
            time.sleep(1.5)
            write(screen, '这是一发虚弹，恶魔又得枪权！', (0, 225))
            del bullet[0]
        else:
            write(screen, '砰！', (0, 200))
            draw(screen, '图片/恶魔击中自己.bmp', (300, 100))
            time.sleep(1.5)
            write(screen, '这是一发实弹，成功击伤恶魔！', (0, 225))
            draw(screen, '图片/恶魔击伤自己.bmp', (300, 100))
            blood_e-=bullet[0]
            del bullet[0]
            hit+=1
            shooter=0
        if 3 in banned:
            banned.remove(3)
    else:
        draw(screen,'图片/选择道具.bmp',(100*(decision+2),0))
        if tool_e[decision-1]==0:
            draw(screen,'图片/恶魔使用华子.bmp',(300,100))
            write(screen,'大哥陪了你一根华子，生命加一',(0,175))
            blood_e+=1
        elif tool_e[decision-1]==1:
            draw(screen,'图片/恶魔使用汽水.bmp',(300,100))
            if bullet[0]==0:
                write(screen,'大哥炫了一罐汽水，并退出一发虚弹',(0,175))
            else:
                write(screen,'大哥炫了一罐汽水，并退出一发实弹',(0,175))
            del bullet[0]
        elif tool_e[decision-1]==2:
            draw(screen,'图片/恶魔使用透镜.bmp',(300,100))
            if bullet[0]==0:
                write(screen,'机智的大哥发现下一发是虚弹',(0,175))
                find=10
            else:
                write(screen,'机智的大哥发现下一发是实弹',(0,175))
                find=9
        elif tool_e[decision-1]==3:
            draw(screen,'图片/恶魔使用小刀.bmp',(300,100))
            write(screen,'恶魔锯短了枪管，下一发子弹伤害翻倍',(0,175))
            bullet[0]*=2
            banned.append(3)
        elif tool_e[decision-1]==4:
            aim,hit=0,0
            draw(screen,'图片/恶魔使用手铐.bmp',(300,100))
            write(screen,'恶魔铐住了你，获得两个枪权',(0,175))
            handcuffs=True
            banned.append(4)
        del tool_e[decision-1]
    if handcuffs is True:
        shooter=1
    if handcuffs is True and (aim==2 or hit==2):
        handcuffs=False
        banned.remove(4)
        shooter,aim,hit=0,0,0
    time.sleep(1.5)
    return bullet,tool_e,blood_p,blood_e,shooter,banned,handcuffs,aim,hit,find