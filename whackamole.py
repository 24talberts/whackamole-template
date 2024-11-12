import pygame

import random


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))

        def draw_grid():
            # draw horizontal lines
            for i in range(1, 16):
                pygame.draw.line(
                    screen,
                    (255, 0, 0),
                    (0, i * 32),
                    (640, i * 32),
                )

            for i in range(1, 20):
                pygame.draw.line(
                    screen,
                    (255, 0, 0),
                    (i * 32, 0),
                    (i * 32, 512),
                )

        clock = pygame.time.Clock()
        mole_pos_x = 0
        mole_pos_y = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if x in range(mole_pos_x, mole_pos_x + 32) and y in range(mole_pos_y, mole_pos_y + 32):
                        mole_pos_x = random.randrange(0,608, 32)
                        mole_pos_y = random.randrange(0,480, 32)

            screen.fill("light green")
            draw_grid()
            screen.blit(mole_image, mole_image.get_rect(topleft= (mole_pos_x, mole_pos_y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
