import pygame
import sys
import random

pygame.init()


def build_text(text, loc, color=(0, 0, 0), size=50):
    font = pygame.font.Font(None, size)
    text = font.render(text, True, color)
    text_rect = text.get_rect(center=loc)
    return text, text_rect


def score_write(text, loc, color=(0, 0, 0), size=50):
    sfont = pygame.font.Font(None, size)
    stext = sfont.render(f"Score: {score_string}", True, (255, 255, 255))
    return stext


# Variables
BG_COLOR = (250, 250, 250)
x = 10
y = 420
d = 20
l = 50
# velocity = 5
circley = 300
circlex = 400
circleYVelocity = -5
circleXVelocity = 0
circlecolor = 'green'
clock = pygame.time.Clock()
game_over = False
score = 0
score_string = ""
difficultyFactor = 0
# screen
screen = pygame.display.set_mode((800, 600))
highest = 0
highest_string = ""

# building text objects

gmover_text, gmover_rect = build_text("game over", (400, 300), 'red', 60)

# main loop
running = True
while running:

    clock.tick(60)

    for event in pygame.event.get():
        # handle quit
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, 'black', (10, 10, 780, 430))
    pygame.draw.rect(screen, 'black', (10, 450, 780, 140))
    # pygame.draw.rect(screen, 'white', (5, 5, 790, 590))

    # Determine if I have a strike / hit
    if circley + 10 == y:
        if x - 10 <= circlex <= (x + l + 10):
            circleYVelocity = -5
            if circlex > 50 and circlex < 750:
                circleXVelocity = random.randint(-5, 5)
            else:
                circleXVelocity = random.randint(-3, 3)
            difficultyFactor += 0.02
            score += 1
            score_string = str(score)

    # circle upper boundary
    if circley <= 30:
        circleYVelocity = 5

    # circle left boundary
    if circlex <= 30:
        circleXVelocity = random.randint(1, 2)

    # circle right boundary
    if circlex >= 770:
        circleXVelocity = random.randint(-1, 0)

    # circle lower boundary
    if circley >= 430:
        game_over = True

    if game_over == False:
        circley += circleYVelocity + difficultyFactor * circleYVelocity
        circlex += circleXVelocity + difficultyFactor * circleXVelocity

    # event loop


    # handle key presses
    keys = pygame.key.get_pressed()
    # right hand movement
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if x <= 735:
            x += 5 + (5 * difficultyFactor)
        else:
            x = 5
    # Left hand movement
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if x >= 15:
            x -= 5 + (5 * difficultyFactor)
        else:
            x = 750
    # Restart the game after loss
    if keys[pygame.K_SPACE] or keys[pygame.K_r]:
        game_over = False
        circley = 300
        circlecolor = 'green'
        circleYVelocity = -5
        score = 0
        score_string = str(score)
        score_text_rect = score_write(score_string, (400, 300), 'white', 60)
        screen.blit(score_text_rect, (50, 500))
        difficultyFactor = 0

        if score > highest:
            highest = score
        highest_string = str(highest)

    # Re-draw the screen with all objects inside it
    pygame.draw.rect(screen, 'blue', (x, y, l, d))
    if game_over:
        screen.blit(gmover_text, gmover_rect)
        circlecolor = 'red'

    pygame.draw.circle(screen, circlecolor, [circlex, circley], 20)
    score_text_rect = score_write(score_string, (400, 300), 'white', 60)
    screen.blit(score_text_rect, (50, 500))

    pygame.display.flip()

pygame.quit()
sys.exit()
