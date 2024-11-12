import pygame
import random


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole = (0, 0)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Mole was clicked
                    if event.pos[0] // 32 == mole[0] and event.pos[1] // 32 == mole[1]:
                        mole = (random.randrange(0, 20), random.randrange(0, 15))
            screen.fill("light green")
            # vertical lines
            for i in range(20):
                pygame.draw.line(screen, "dark green", (i * 32, 0), (i * 32, 512))
            # Horizontal lines
            for i in range(16):
                pygame.draw.line(screen, "dark green", (0, i * 32), (640, i * 32))
            screen.blit(
                mole_image,
                mole_image.get_rect(topleft=(mole[0] * 32, mole[1] * 32)),
            )
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()