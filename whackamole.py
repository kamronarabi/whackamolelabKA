import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole = (0,0)
        checkMole = (0, 0)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                   click = (event.pos[0]//32,event.pos[1]//32)
                   if click == checkMole:
                     newx = random.randrange(0, 20)
                     newy = random.randrange(0, 16)
                     mole = (newx*32, newy*32)
                     checkMole = (newx, newy)

            screen.fill("light green")
            for i in range(20):
                pygame.draw.line(screen, "blue", (i*32,0),(i*32,512))
            for i in range(16):
                pygame.draw.line(screen, "red", (0,i*32),(640,i*32))
            screen.blit(mole_image, mole_image.get_rect(topleft=mole))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
