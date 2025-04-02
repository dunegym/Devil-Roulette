from 刷新 import *
from 恶魔行为 import *
from 玩家行为 import *
import sys
def no_tool_game(screen,difficulty):
    blood_p,blood_e=5,5
    bullet=[]
    tool_p=[]
    tool_e=[]
    banned=[]
    handcuffs=False
    aim,hit=0,0
    draw(screen,'图片/道具栏.bmp',(300,0))
    draw(screen,'图片/道具栏.bmp',(300,600))
    draw(screen,'图片/背景.bmp',(300,100))
    draw(screen,'图片/标题.bmp',(0,0))
    write(screen,'非道具战即将开始！',(0,100))
    write(screen,'本轮中你和恶魔各有5点生命，',(0,125))
    write(screen,'每个弹匣里有5发子弹，',(0,150))
    write(screen,'可以打自己也可以打恶魔。',(0,175))
    write(screen,'无额外道具。你若胜利则可进入第二轮。',(0,200))
    time.sleep(5)
    draw(screen,'图片/消除文字.bmp',(0,100))
    while blood_e>0 and blood_p>0:
        write(screen,'且听恶魔大哥弹枪一曲......',(0,100))
        draw(screen,'图片/弹枪一曲.bmp',(300,100))
        the_bullet=Bullet(bullet,5)
        bullet,real,blank=the_bullet.trans_bullet()
        time.sleep(1.5)
        write(screen,'该弹匣中有'+str(real)+'发实弹和'+str(blank)+'发虚弹',(0,125))
        time.sleep(3)
        reset(screen)
        shooter=0
        while blood_e>0 and blood_p>0 and len(bullet)>0:
            show_blood(screen,blood_p,blood_e)
            decision=0
            if shooter==0:
                write(screen,'请选择你的下一步行动',(0,150))
                while decision!=9 and decision!=10:
                    decision=decide()
                bullet,tool_p,blood_p,blood_e,shooter,banned,handcuffs,aim,hit\
                    =action_p(screen,decision,bullet,tool_p,blood_p,blood_e,shooter,banned,handcuffs,aim,hit)
            elif shooter==1:
                write(screen,'恶魔正在做出抉择',(0,150))
                time.sleep(1.5)
                if difficulty=='easy':
                    decision=random.randint(9,10)
                elif difficulty=='medium':
                    if bullet.count(0)>bullet.count(1):
                        decision=10
                    else:
                        decision=9
                elif difficulty=='difficult':
                    if bullet[0]==0:
                        decision=10
                    else:
                        decision=9
                bullet,tool_e,blood_p,blood_e,shooter,banned,handcuffs,aim,hit,find\
                    =action_e(screen,decision,bullet,tool_e,blood_p,blood_e,shooter,banned,handcuffs)
            reset(screen)
    if blood_p<=0:
        write(screen,'很遗憾，你被恶魔杀死了！',(0,100))
        draw(screen,'图片/失败结算.bmp',(300,100))
        time.sleep(10)
        sys.exit()
    else:
        write(screen,'恭喜你，取得了本轮的胜利！',(0,100))
        write(screen,'请做好下一轮道具战的准备！',(0,125))
        time.sleep(1.5)
        reset(screen)