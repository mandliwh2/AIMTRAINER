import pygame
import random
import time
import json

# initialize the pygame module
pygame.init()
# Time
clock = pygame.time.Clock()
# Screen
cell = 140
iconImg = pygame.image.load("Images/cursorImg.png")
screen = pygame.display.set_mode((cell * 4, cell * 3))
pygame.display.set_caption("Aim Trainer By @mandliwh2")
pygame.display.set_icon(iconImg)
# positons
_X = [0]
_Y = [0]
for i in range(15):
    _X.append(_X[-1] + 35)
for i in range(11):
    _Y.append(_Y[-1] + 35)

# target
targetX = random.choice(_X)
targetY = random.choice(_Y)
_Size = cell / 4
_Color = pygame.Color("black")


def _Target(Rect):
    pygame.draw.ellipse(screen, _Color, Rect)


end = 0
_Over = False

_Data = {
    "Score": 0
}

score = 0

with open("HIGHSCORE.TXT") as ScoreFile:
    _Data = json.load(ScoreFile)

print(_Data["Score"])
# Game Loop
_IsEnd = False
running = True
while running:
    start = time.time()
    screen.fill(pygame.Color("white"))
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if _Data["Score"] <= score:
                with open("HIGHSCORE.TXT", 'w') as ScoreFile:
                    json.dump(_Data, ScoreFile)

            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if pygame.Rect(targetX, targetY, _Size, _Size).collidepoint(x, y):
                targetX = random.choice(_X)
                targetY = random.choice(_Y)
                score += 1
                if _Data["Score"] <= score:
                    _Data["Score"] = score
                end = time.time()
                _IsEnd = True
    if _IsEnd:
        if (start - end) >= 5:
            _Over = True
            font = pygame.font.Font("freesansbold.ttf", 32)
            final = font.render("GAME OVER", True, _Color)
            screen.blit(final, (180, 220))
    if not _Over:
        _Target(pygame.Rect(targetX, targetY, _Size, _Size))
        fontS = pygame.font.Font("freesansbold.ttf", 25)
        fontZ = pygame.font.Font("freesansbold.ttf", 25)
        final = fontS.render("SCORE : " + str(score), True, _Color)
        _High = fontZ.render("HIGHSCORE : " + str(_Data["Score"]), True, _Color)
        screen.blit(final, (10, 10))
        screen.blit(_High, (350, 10))

    pygame.display.update()
    clock.tick(60)
