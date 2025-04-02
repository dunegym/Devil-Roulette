from 非道具战 import *
from 道具战 import *
mode=0
win=0
pygame.init()
screen=pygame.display.set_mode((1100,700))
pygame.display.set_caption('恶魔轮盘赌')
draw(screen,'图片/启动.bmp',(440,210))
while mode==0:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            (x,y) = pygame.mouse.get_pos()
            if 440<x<660 and 210<y<280:
                mode=1
            elif 440<x<660 and 280<y<350:
                mode=2
            elif 440<x<660 and 350<y<420:
                mode=3
            elif 440<x<660 and 420<y<490:
                mode=4
screen.fill((0,0,0))
draw(screen,'图片/载入.bmp',(440,280))
time.sleep(1)
if mode==1:
    no_tool_game(screen,'easy')
    tool_game(screen,6,2,'easy')
    tool_game(screen,7,4,'easy')
    write(screen,'你成功获得了奖金！',(0,100))
    draw(screen,'图片/胜利结算.bmp',(300,100))
    time.sleep(10)
elif mode==2:
    no_tool_game(screen, 'medium')
    tool_game(screen, 6, 2, 'medium')
    tool_game(screen, 7, 4, 'medium')
    write(screen, '你成功获得了奖金！', (0, 100))
    draw(screen, '图片/胜利结算.bmp', (300, 100))
    time.sleep(10)
elif mode==3:
    no_tool_game(screen, 'difficult')
    tool_game(screen, 6, 2, 'difficult')
    tool_game(screen, 7, 4, 'difficult')
    write(screen, '你成功获得了奖金！', (0, 100))
    draw(screen, '图片/胜利结算.bmp', (300, 100))
    time.sleep(10)
elif mode==4:
    while True:
        no_tool_game(screen, 'easy')
        tool_game(screen, 6, 2, 'easy')
        tool_game(screen, 7, 4, 'easy')
        win+=1
        write(screen,'真厉害，你已经闯过了'+str(win)+'轮！',(0,100))
        time.sleep(3)
        reset(screen)
        for i in range(3):
            no_tool_game(screen, 'medium')
            tool_game(screen, 6, 2, 'medium')
            tool_game(screen, 7, 4, 'medium')
            win+=1
            write(screen, '真厉害，你已经闯过了' + str(win) + '轮！', (0, 100))
            time.sleep(3)
            reset(screen)
        no_tool_game(screen, 'difficult')
        tool_game(screen, 6, 2, 'difficult')
        tool_game(screen, 7, 4, 'difficult')
        win+=1
        write(screen, '真厉害，你已经闯过了' + str(win) + '轮！', (0, 100))
        time.sleep(3)
        reset(screen)