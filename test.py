import pygame

pygame.init()
screen = pygame.display.set_mode((196, 100))
pygame.display.set_caption("pygame.mouse函数")

while True:
    event=pygame.event.wait()
    if event.type == pygame.QUIT:
        exit()
    b=pygame.mouse.get_pressed()   #获取鼠标按键的情况（是否被按下）
    #返回一个由布尔值组成的列表，代表所有鼠标按键被按下的情况。True意味着在调用此方法时该鼠标按键正被按下
    #(1, 0, 1)  表示左键和右键被按下(左键、中键、右键)
    #这条语句没有体现滚轮的滚动
    # #必须先调用pygame.event.wait等语句后才能工作


    print(b)

    pygame.display.update()

