import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    running = True

    pigeon = pygame.image.load("pizon.png")

    font = pygame.font.Font('splash.ttf', 50)

    count = 0

    text = font.render(str(count), True, (0,255,0), (0,0,255))
    textRect = text.get_rect()
    textRect.center = (800 // 2, 600 // 2)


    while running:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                count += 1
                print("OK")


        text = font.render(str(count), True, (0,255,0), (0,0,255))

        screen.blit(pigeon, (0,0))
        screen.blit(text, textRect)
        pygame.display.flip()


if __name__ == "__main__":
    main()


