import pygame
from random import *
pygame.init()

pieceWidth = 200
boardThickness = 30
topMargin = 50

winWidth = 3 * pieceWidth + 2 * boardThickness
winHeight = winWidth + topMargin

window = pygame.display.set_mode((winWidth, winHeight)) 
pygame.display.set_caption("Snake")

xImg = pygame.image.load('X.png')
oImg = pygame.image.load('O.png')
emptyImg = pygame.image.load('Nobody.png')

xWins = 0
oWins = 0
ties = 0

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
xTurn = True

def clearBoard():
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def displayBoard():
    pygame.draw.rect(window, (0,0,0), (0, topMargin, winWidth, winWidth))
    for i in range(0,3):
        for j in range(0,3):
            pos = (i * (pieceWidth + boardThickness), j * (pieceWidth + boardThickness) + topMargin)
            if board[i][j] == "X":
                window.blit(xImg, pos)
            if board[i][j] == "O":
                window.blit(oImg, pos)
            if board[i][j] == " ":
                window.blit(emptyImg,pos)
                
def click(pos, xTurn):
    if pos[0] < pieceWidth:
        if pos[1] < pieceWidth + topMargin:
            if board[0][0] == " ":
                if xTurn:
                    board[0][0] = "X"
                    return True
                else:
                    board[0][0] = "O"
                    return True
        if pos[1] > pieceWidth + boardThickness + topMargin and pos[1] < 2 * pieceWidth + boardThickness + topMargin:
            if board[0][1] == " ":
                if xTurn:
                    board[0][1] = "X"
                    return True
                else:
                    board[0][1] = "O"
                    return True
        if pos[1] > 2 * pieceWidth + boardThickness + topMargin:
            if board[0][2] == " ":
                if xTurn:
                    board[0][2] = "X"
                    return True
                else:
                    board[0][2] = "O"
                    return True
    if pos[0] > pieceWidth + boardThickness and pos[0] < 2 * pieceWidth + boardThickness:
        if pos[1] < pieceWidth + topMargin:
            if board[1][0] == " ":
                if xTurn:
                    board[1][0] = "X"
                    return True
                else:
                    board[1][0] = "O"
                    return True
        if pos[1] > pieceWidth + boardThickness + topMargin and pos[1] < 2 * pieceWidth + boardThickness + topMargin:
            if board[1][1] == " ":
                if xTurn:
                    board[1][1] = "X"
                    return True
                else:
                    board[1][1] = "O"
                    return True
        if pos[1] > 2 * pieceWidth + boardThickness + topMargin:
            if board[1][2] == " ":
                if xTurn:
                    board[1][2] = "X"
                    return True
                else:
                    board[1][2] = "O"
                    return True
    if pos[0] > 2 * pieceWidth + boardThickness:
        if pos[1] < pieceWidth + topMargin:
            if board[2][0] == " ":
                if xTurn:
                    board[2][0] = "X"
                    return True
                else:
                    board[2][0] = "O"
                    return True
        if pos[1] > pieceWidth + boardThickness + topMargin and pos[1] < 2 * pieceWidth + boardThickness + topMargin:
            if board[2][1] == " ":
                if xTurn:
                    board[2][1] = "X"
                    return True
                else:
                    board[2][1] = "O"
                    return True
        if pos[1] > 2 * pieceWidth + boardThickness + topMargin:
            if board[2][2] == " ":
                if xTurn:
                    board[2][2] = "X"
                    return True
                else:
                    board[2][2] = "O"
                    return True

def determineWinner():
    winner = 0
    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        if board[0][0] == "X":
            winner = 1
        if board[0][0] == "O":
            winner = 2
    if board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        if board[1][0] == "X":
            winner = 1
        if board[1][0] == "O":
            winner = 2
    if board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        if board[2][0] == "X":
            winner = 1
        if board[2][0] == "O":
            winner = 2
    if board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        if board[0][0] == "X":
            winner = 1
        if board[0][0] == "O":
            winner = 2
    if board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        if board[0][1] == "X":
            winner = 1
        if board[0][1] == "O":
            winner = 2
    if board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        if board[0][2] == "X":
            winner = 1
        if board[0][2] == "O":
            winner = 2
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        if board[0][0] == "X":
            winner = 1
        if board[0][0] == "O":
            winner = 2
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        if board[0][2] == "X":
            winner = 1
        if board[0][2] == "O":
            winner = 2
    
    if board[0][0] != " " and board[0][1] != " " and board[0][2] != " " and board[1][0] != " " and board[1][1] != " " and board[1][2] != " " and board[2][0] != " " and board[2][1] != " " and board[2][2] != " ":
        winner = 3
        
    return winner


run = True
playing = False

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if playing:
                pos = pygame.mouse.get_pos()
                if click(pos, xTurn):
                    xTurn = not xTurn
                
                winner = determineWinner()
                if winner == 1:
                    xWins += 1
                    print("X Wins")
                    playing = False
                if winner == 2:
                    oWins += 1
                    print("O Wins")
                    playing = False
                if winner == 3:
                    ties += 1
                    print("Its a cats game!")
                    playing = False
            else:
                playing = True
                print("Starting new Game")
                board = clearBoard()
     
    window.fill((255,255,255))
    displayBoard()
    pygame.display.update()
    
     
pygame.quit()