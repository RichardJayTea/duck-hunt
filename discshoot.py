import pygame, sys
import random
from pygame.locals import *
import time
import mod

rect1 = [0,0,0,0]
rect2 = [0,0,0,0]
rect3 = [0,0,0,0]
rect4 = [0,0,0,0]
rect5 = [0,0,0,0]

RIGHT = 6
LEFT = 4

def spawnRect(b):
	spawncoord = random.randint(0,600)
	destcoord = random.randint(0,600)
	side = random.randint(0,1)
	if side == 0:
		b['rect'].left = 0
	else:
		b['rect'].right = 1300
	b['rect'].top = spawncoord
	diffofCoord = destcoord - spawncoord
	if ((diffofCoord != 0) and (diffofCoord >= 52)):
		s = (int(1300 / diffofCoord))
	elif ((diffofCoord < 52) and (diffofCoord >= 0)):
		diffofCoord += 52
		s = (int(1300 / diffofCoord))
	else:
		diffofCoord -= 52
		s = (int(1300 / diffofCoord))
	print(s)
	return s
def moveRect(c, rect):
        rect[0] = spawnRect(c)
        if (rect[0] < 0):
                rect[1] = -1
        elif (rect[0] > 0):
                rect[1] = 1
        else:
                rect[1] = 0
        rect[2] = abs(rect[0])
def updateRect(c, rect, mul):
        if c['rect'].left == 0:
                rect[3] = 6
        if c['rect'].right == 1300:
                rect[3] = 4
        if rect[3] == 6:
                c['rect'].top += (rect[1] * mul)
                c['rect'].left += (rect[2] * mul)
        if rect[3] == 4:
                c['rect'].top += (rect[1] * mul)
                c['rect'].left -= (rect[2] * mul)
def drawObj(c, rect):
	screen.blit(alphaRect, (c['rect'].left, c['rect'].top))
	pygame.draw.rect(alphaRect, c['color'], c['rect'])
	if rect[3] == 6:
		screen.blit(bird1stretch, c['rect'])
	else:
		screen.blit(bird2stretch, c['rect'])
def changeScore(score):
	score[0] += 1
	drawScore = playerscore.render(str(score), 1, (0, 255, 0))
	screen.blit(drawScore, (0,0))

pygame.init()
initTime = 0
score = [0]
currentDiff = 1
screen = pygame.display.set_mode((1300, 800), 0, 32)
start = pygame.font.SysFont("monospace", 100)
end = pygame.font.SysFont("monospace", 100)
playerscore = pygame.font.SysFont("monospace", 60)
finalScore = pygame.font.SysFont("monospace", 80)
actualScore = pygame.font.SysFont("monospace", 170)
playAgain = pygame.font.SysFont("monospace", 80)
quit = pygame.font.SysFont("monospace", 80)
backdrop = pygame.Rect(0,0, 1300, 800)
alphaRect = pygame.Surface((60,40))
alphaRect.set_alpha(0)
alphaRect.fill((0,0,0))
alphaplayAgain = pygame.Surface((320,60))
alphaplayAgain.set_alpha(0)
alphaplayAgain.fill((0,0,0))
alphaquit = pygame.Surface((200, 60))
alphaquit.set_alpha(0)
alphaquit.fill((0,0,0))
b1 = {'rect':pygame.Rect(0, 0, 60, 40), 'color': (0,0,0), 'dir': 6}
b2 = {'rect':pygame.Rect(0, 0, 60, 40), 'color': (0,0,0), 'dir': 6}
b3 = {'rect':pygame.Rect(0, 0, 60, 40), 'color': (0,0,0), 'dir': 6}
b4 = {'rect':pygame.Rect(0, 0, 60, 40), 'color': (0,0,0), 'dir': 6}
b5 = {'rect':pygame.Rect(0, 0, 60, 40), 'color': (0,0,0), 'dir': 6}
startRect = {'rect': pygame.Rect(535, 370, 230, 60), 'color': (0,255,0)}
playagainRect = {'rect':pygame.Rect(100, 235, 320, 60), 'color':(0,0,0)}
quitRect = pygame.Rect(950, 235, 160, 60)
quitRectBeg = pygame.Rect(580, 450, 160, 60)
blocks = [b1, b2, b3]
xpback = pygame.image.load('xpback.jpg')
bird1 = pygame.image.load('bird.png')
bird1stretch = pygame.transform.scale(bird1,(60,60))
bird2 = pygame.image.load('bird2.png')
bird2stretch = pygame.transform.scale(bird2,(60,60))
menuChoice = 0
numofBirds = 3

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	if menuChoice == 0:
		screen.blit(xpback, (0,0))
		drawStart = start.render("[START]", 1, (0,255,0))
		screen.blit(drawStart, startRect['rect'])
		drawQuit = quit.render("[QUIT]", 1, (0,255,0))
		screen.blit(drawQuit, (quitRectBeg.left, quitRectBeg.top))
		pygame.draw.rect(alphaquit,(0,0,0), quitRectBeg)
		if event.type == MOUSEBUTTONDOWN:
			if (startRect['rect'].left < event.pos[0]) and (startRect['rect'].right > event.pos[0]) and (startRect['rect'].top < event.pos[1]) and (startRect['rect'].bottom > event.pos[1]):
				menuChoice = 1
			if (quitRectBeg.left < event.pos[0]) and (quitRectBeg.right > event.pos[0]) and (quitRectBeg.top < event.pos[1]) and (quitRectBeg.bottom > event.pos[1]):
                                pygame.quit()
                                sys.exit()
		if event.type == KEYDOWN:
			if event.key == ord('e'):
				menuChoice = 2
		pygame.display.update()
	elif menuChoice == 1:
		if initTime == 0:
			initTime = time.time()
		if event.type == MOUSEBUTTONDOWN:
			if (b1['rect'].left < event.pos[0]) and (b1['rect'].right > event.pos[0]) and (b1['rect'].top < event.pos[1]) and (b1['rect'].bottom > event.pos[1]):
				
				changeScore(score)
				moveRect(b1, rect1)
				updateRect(b1, rect1, currentDiff)
				pygame.draw.rect(alphaRect, b1['color'], b1['rect'])
				pygame.display.update()
			if (b2['rect'].left < event.pos[0]) and (b2['rect'].right > event.pos[0]) and (b2['rect'].top < event.pos[1]) and (b2['rect'].bottom > event.pos[1]):
				
				changeScore(score)
				moveRect(b2, rect2)
				updateRect(b2, rect2, currentDiff)
				pygame.draw.rect(alphaRect, b2['color'], b2['rect'])
				pygame.display.update()
			if (b3['rect'].left < event.pos[0]) and (b3['rect'].right > event.pos[0]) and (b3['rect'].top < event.pos[1]) and (b3['rect'].bottom > event.pos[1]):
				
				changeScore(score)
				moveRect(b3, rect3)
				updateRect(b3, rect3, currentDiff)
				pygame.draw.rect(alphaRect, b3['color'], b3['rect'])
				pygame.display.update()
			if (numofBirds == 5 and b4['rect'].left < event.pos[0]) and (b4['rect'].right > event.pos[0]) and (b4['rect'].top < event.pos[1]) and (b4['rect'].bottom > event.pos[1]):

                                changeScore(score)
                                moveRect(b4, rect4)
                                updateRect(b4, rect4, currentDiff)
                                pygame.draw.rect(alphaRect, b4['color'], b4['rect'])
                                pygame.display.update()
			if (numofBirds == 5 and b5['rect'].left < event.pos[0]) and (b5['rect'].right > event.pos[0]) and (b5['rect'].top < event.pos[1]) and (b5['rect'].bottom > event.pos[1]):

                                changeScore(score)
                                moveRect(b5, rect5)
                                updateRect(b5, rect5, currentDiff)
                                pygame.draw.rect(alphaRect, b5['color'], b5['rect'])
                                pygame.display.update()
		if event.type == KEYDOWN:
			if event.key == ord('p'):
				menuChoice = 0
		if ((b1['rect'].top <= 0) or (b1['rect'].left <= 0) or (b1['rect'].right >= 1300) or (b1['rect'].bottom >= 800)):
			moveRect(b1, rect1)
		
		if ((b2['rect'].top <= 0) or (b2['rect'].left <= 0) or (b2['rect'].right >= 1300) or (b2['rect'].bottom >= 800)):
			moveRect(b2, rect2)

		if ((b3['rect'].top <= 0) or (b3['rect'].left <= 0) or (b3['rect'].right >= 1300) or (b3['rect'].bottom >= 800)):
			moveRect(b3, rect3)
		if (numofBirds == 5 and ((b4['rect'].top <= 0) or (b4['rect'].left <= 0) or (b4['rect'].right >= 1300) or (b4['rect'].bottom >= 800))):
                        moveRect(b4, rect4)
		if (numofBirds == 5 and ((b5['rect'].top <= 0) or (b5['rect'].left <= 0) or (b5['rect'].right >= 1300) or (b5['rect'].bottom >= 800))):
                        moveRect(b5, rect5)
		diffTime = int(time.time() - initTime)
		if (diffTime > 10 and diffTime < 20):
			currentDiff = 5
		elif (diffTime > 20 and diffTime < 30):
			numofBirds = 5
		elif (diffTime >= 30):
			menuChoice = 2
		updateRect(b1, rect1, currentDiff)
		updateRect(b2, rect2, currentDiff)
		updateRect(b3, rect3, currentDiff)
		if numofBirds == 5:
			updateRect(b4, rect4, currentDiff)
			updateRect(b5, rect5, currentDiff)
		screen.blit(xpback, (0,0))
		drawObj(b1, rect1)
		drawObj(b2, rect2)
		drawObj(b3, rect3)
		if numofBirds == 5:
			drawObj(b4, rect4)
			drawObj(b5, rect5)
		drawScore = playerscore.render(str(score[0]), 1, (0, 255, 0))
		screen.blit(drawScore, (0,0)) 
		pygame.display.update()
		time.sleep(0.0166)
	
	elif menuChoice == 2:
		screen.blit(xpback, (0,0))
		drawEnd = end.render("Game Over!", 1, (0,255,0))
		screen.blit(drawEnd, (480, 200))
		drawfinalScore = finalScore.render("Final Score: ", 1,(0,255,0))
		screen.blit(drawfinalScore, (520, 270))
		drawactualScore = actualScore.render(str(score[0]), 1, (0,255,0))
		screen.blit(drawactualScore, (640, 340))
		pygame.draw.rect(alphaplayAgain, playagainRect['color'], playagainRect['rect'])
		drawplayAgain = playAgain.render("[PLAY AGAIN]", 1, (0,255,0))
		screen.blit(drawplayAgain, (playagainRect['rect'].left, playagainRect['rect'].top))
		drawQuit = quit.render("[QUIT]", 1, (0,255,0))
		screen.blit(drawQuit, (quitRect.left, quitRect.top))
		pygame.draw.rect(alphaquit,(0,0,0), quitRect)
		pygame.display.update()
		if event.type == MOUSEBUTTONDOWN:
			if (playagainRect['rect'].left < event.pos[0]) and (playagainRect['rect'].right > event.pos[0]) and (playagainRect['rect'].top < event.pos[1]) and (playagainRect['rect'].bottom > event.pos[1]):
				currentDiff = 1
				initTime = 0
				score[0] = 0
				numofBirds = 3
				menuChoice = 1
				moveRect(b1, rect1)
				moveRect(b2, rect2)
				moveRect(b3, rect3)
				moveRect(b4, rect4)
			if (quitRect.left < event.pos[0]) and (quitRect.right > event.pos[0]) and (quitRect.top < event.pos[1]) and (quitRect.bottom > event.pos[1]):
				pygame.quit()
				sys.exit()
