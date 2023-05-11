import pygame, sys, random, os

# 欄位
column = 3
cellNums = column * column
FPS = 40

# 退出畫面
def terminate():
    pygame.quit()
    sys.exit()

# 遊戲畫面
def gameBoard():
    
    # 生成拼圖變數
    board = []
    for i in range(cellNums):
        board.append(i)
    nullCell = cellNums - 1
    board[nullCell] = -1

    # 隨機移動空格的位置
    for i in range(100):
        direction = random.randint(0, 3)
        if (direction == 0):
            nullCell = moveUp(board, nullCell)
        elif (direction == 1):
            nullCell = moveDown(board, nullCell)
        elif (direction == 2): 
            nullCell = moveLeft(board, nullCell)
        else:
            nullCell = moveRight(board, nullCell)

    return board, nullCell


# 空格在最下面就不用動，不是就往上一格
def moveUp(board, nullCell):
    if nullCell >= cellNums - column:
        return nullCell
    board[nullCell + column], board[nullCell] = board[nullCell], board[nullCell + column]
    return nullCell + column

# 空格在最上面就不用動，不是就往下一格
def moveDown(board, nullCell):
    if nullCell < column:
        return nullCell
    board[nullCell - column], board[nullCell] = board[nullCell], board[nullCell - column]
    return nullCell - column

# 空格在最左邊就不用動，不是就往左邊一格
def moveRight(board, nullCell):
    if nullCell % column == 0:
        return nullCell
    board[nullCell - 1], board[nullCell] = board[nullCell], board[nullCell - 1]
    return nullCell - 1

# 空格在最右邊就不用動，不是就往右邊一格
def moveLeft(board, nullCell):
    if nullCell % column == column - 1:
        return nullCell
    board[nullCell + 1], board[nullCell] = board[nullCell], board[nullCell + 1]
    return nullCell + 1

# 判斷除了空格以外的拼圖是否有照順序(有沒有成功)
def isFinished(board):
    for i in range(cellNums - 1):
        if board[i] != i:
            return False
    return True

font_name = os.path.join("font.ttf")
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_serface = font.render(text, True, (255, 255, 255))
    text_rect = text_serface.get_rect()
    text_rect.centerx = x 
    text_rect.top = y
    surf.blit(text_serface, text_rect)

def draw_init():
    draw_text(screen, '拼圖遊戲', 64, imageRect.width/2, imageRect.height/4)
    draw_text(screen, '可以利用鍵盤方向鍵或滑鼠左鍵移動拼圖', 22, imageRect.width/2, imageRect.height/2)
    draw_text(screen, '按任意鍵開始遊戲', 18, imageRect.width/2, imageRect.height*3/4)
    pygame.display.update()
    waiting = True
    while waiting:
        fps_clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # 鍵盤事件
            if event.type == pygame.KEYUP:
                waiting = False
        
# 初始化
pygame.init()
fps_clock = pygame.time.Clock()

# 圖片處理
image = pygame.image.load('default.jpg')
imageRect = image.get_rect()

# 基礎設置
screen = pygame.display.set_mode((imageRect.width, imageRect.height))
pygame.display.set_caption('拼圖遊戲')

cellWidth = int(imageRect.width / column)
cellHeight = int(imageRect.height / column)

finish = False
show_init = True

board, nullCell = gameBoard()

# 遊戲運行
while True:
    if show_init:
        draw_init()
        show_init = False
    fps_clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if finish:
            continue
        # 鍵盤事件
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                nullCell = moveLeft(board, nullCell)
            elif event.key == pygame.K_RIGHT:
                nullCell = moveRight(board, nullCell)
            elif event.key == pygame.K_UP:
                nullCell = moveUp(board, nullCell)
            elif event.key == pygame.K_DOWN:
                nullCell = moveDown(board, nullCell)
        
        # 滑鼠事件
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1:
            x, y = pygame.mouse.get_pos()
            col = int(x / cellWidth)
            row = int(y / cellHeight)
            index = col + row * column
            # 將點擊的跟空白互換，如果是相鄰那側的話
            if(index == nullCell - 1 or 
            index == nullCell + 1 or 
            index == nullCell - column or 
            index == nullCell + column):
                board[nullCell], board[index] = board[index], board[nullCell]
                nullCell = index 
    # 判斷完成與否
    if (isFinished(board)):
        board[nullCell] = cellNums - 1
        finish = True

    screen.fill((255, 255, 255))

    # 圖片設置  
    for i in range(cellNums):
        rowDst = int(i / column)
        colDst = int(i % column)
        rectDst = pygame.Rect(colDst * cellWidth, rowDst * cellHeight, cellWidth, cellHeight)

        if board[i] == -1:
            continue

        rowArea = int(board[i] / column)
        colArea = int(board[i] % column)
        rectArea = pygame.Rect(colArea * cellWidth, rowArea * cellHeight, cellWidth, cellHeight)
        screen.blit(image, rectDst, rectArea)

    #畫面更新
    pygame.display.update()

    


