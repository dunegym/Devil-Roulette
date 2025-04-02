import pygame
def draw(screen,path,location):
    image=pygame.image.load(path)
    rect=image.get_rect(topleft=location)
    screen.blit(image,rect)
    pygame.display.flip()
#在界面里载入图片
def write(screen,content,location):
    word=pygame.font.Font('思源黑体.otf',16)
    rendering=word.render(content,True,(255,255,255))
    rect=rendering.get_rect(topleft=location)
    screen.blit(rendering,rect)
    pygame.display.flip()
#在界面里显示文字
def show_blood(screen,blood_p,blood_e):
    write(screen,'你还剩'+str(blood_p)+'点生命',(0, 100))
    write(screen,'恶魔剩'+str(blood_e)+'点生命',(0, 125))
#展示血量
def show_tool(screen,tool_p,tool_e):
    draw(screen, '图片/已解锁.bmp', (300, 0))
    draw(screen, '图片/已解锁.bmp', (300, 600))
    tool = ['华子','汽水','透镜','小刀','手铐']
    num=1
    for i in tool_p:
        draw(screen,'图片/'+tool[i]+'.bmp',(100*(num+2),600))
        num+=1
    num=1
    for i in tool_e:
        draw(screen,'图片/'+tool[i]+'.bmp',(100*(num+2),0))
        num+=1
#展示道具
def reset(screen):
    draw(screen,'图片/向自己开枪.bmp',(0,600))
    draw(screen,'图片/向恶魔开枪.bmp',(150,600))
    draw(screen,'图片/消除文字.bmp',(0,100))
    draw(screen,'图片/背景.bmp',(300,100))
#玩家射击结束后刷新界面（第二三轮中与show_tool(screen,tool_p,tool_e)搭配使用）