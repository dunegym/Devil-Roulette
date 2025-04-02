from 刷新 import *
from 恶魔行为 import *
from 玩家行为 import *
import sys
def tool_game(screen,bullets,tools,difficulty):
    blood_p,blood_e=bullets,bullets
    bullet=[]
    tool_p=[]
    tool_e=[]
    aim,hit=0,0
    write(screen, '道具战即将开始！', (0, 100))
    write(screen, '本轮中你和恶魔各有'+str(bullets)+'点生命，', (0, 125))
    write(screen, '每个弹匣里有'+str(bullets)+'发子弹，', (0, 150))
    write(screen, '可以打自己也可以打恶魔。', (0, 175))
    write(screen, '每次装弹时发放'+str(tools)+'个道具，', (0, 200))
    write(screen,'道具栏最多容纳8个道具。',(0,225))
    time.sleep(5)
    draw(screen, '图片/消除文字.bmp', (0, 100))
    while blood_e > 0 and blood_p > 0:
        the_tool = Tool(tool_p, tool_e, tools)
        show_tool(screen, tool_p, tool_e)
        tool_p, tool_e = the_tool.trans_tool()
        reset(screen)
        write(screen, '道具已分发完毕', (0, 100))
        time.sleep(3)
        reset(screen)
        write(screen, '且听恶魔大哥弹枪一曲......', (0, 100))
        draw(screen, '图片/弹枪一曲.bmp', (300, 100))
        the_bullet = Bullet(bullet, bullets)
        bullet, real, blank = the_bullet.trans_bullet()
        time.sleep(1.5)
        write(screen, '该弹匣中有' + str(real) + '发实弹和' + str(blank) + '发虚弹', (0, 125))
        time.sleep(3)
        reset(screen)
        banned = []
        handcuffs=False
        shooter, find = 0, 0
        while blood_e > 0 and blood_p > 0 and len(bullet) > 0:
            show_blood(screen, blood_p, blood_e)
            decision = 0
            if shooter == 0:
                write(screen, '请选择你的下一步行动', (0, 150))
                while decision == 0 or len(tool_p) < decision < 9:
                    decision = decide()
                    if decision == 9 or decision == 10:
                        break
                    elif len(tool_p) < decision < 9:
                        continue
                    else:
                        if tool_p[decision - 1] in banned:
                            decision = 0
                            continue
                bullet, tool_p, blood_p, blood_e, shooter, banned, handcuffs, aim, hit \
                    = action_p(screen, decision, bullet, tool_p, blood_p, blood_e, shooter, banned, handcuffs, aim, hit)
            elif shooter == 1:
                write(screen, '恶魔正在做出抉择', (0, 150))
                time.sleep(1.5)
                while len(tool_e) < decision < 9 or decision == 0:
                    decision = random.randint(1, 10)
                    if len(tool_e) < decision < 9:
                        continue
                    elif decision >= 9:
                        if difficulty=='easy':
                            decision=random.randint(9,10)
                        elif difficulty=='medium':
                            if bullet.count(0) > bullet.count(1):
                                decision = 10
                            else:
                                decision = 9
                        elif difficulty=='difficult':
                            if bullet[0]==0:
                                decision=10
                            else:
                                decision=9
                        break
                    if (tool_e[decision - 1] == 1 and bullet.count(0) <= bullet.count(1)) \
                        or (tool_e[decision - 1] == 2 and (bullet.count(0) == 0 or bullet.count(1) == 0 or find != 0)) \
                            or (tool_e[decision - 1] == 4 and (bullet.count(1) < bullet.count(0) or len(bullet) == 1)) \
                                or (tool_e[decision - 1] == 3 and bullet.count(1) <= bullet.count(0)) or (tool_e[decision - 1] in banned):
                        decision = 0
                    if 3 in banned:
                        decision = 9
                    if find == 9 and (3 in tool_e):
                        decision = tool_e.index(3) + 1
                    elif (find == 9 and (3 not in tool_e)) or find == 10:
                        decision = find
                    if 0 in tool_e:
                        decision = tool_e.index(0) + 1
                bullet, tool_e, blood_p, blood_e, shooter, banned, handcuffs, aim, hit, find \
                    = action_e(screen, decision, bullet, tool_e, blood_p, blood_e, shooter, banned, handcuffs, aim, hit,
                               find)
            reset(screen)
            show_tool(screen, tool_p, tool_e)
    if blood_p<=0:
        write(screen,'很遗憾，你被恶魔杀死了！',(0,100))
        draw(screen,'图片/失败结算.bmp',(300,100))
        time.sleep(10)
        sys.exit()
    else:
        write(screen,'恭喜你，取得了本轮的胜利！',(0,100))
        time.sleep(1.5)
        reset(screen)