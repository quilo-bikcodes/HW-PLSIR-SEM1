import pygame
pygame.init()

width, height = 800,  600
backgroundColor = 100,  0,  230

win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bikcodes')

def main():
    run = True
    while run:
        win.fill(backgroundColor)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

if __name__ == '__main__':
    main()