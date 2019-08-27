import pygame
from pygame.locals import *
from Hangman.GameInstance import GameInstance
from Hangman.GameInstance import LETTERCLICKED
from Hangman.GameInstance import PLAY


if __name__ == "__main__":
    pygame.init()
    game = GameInstance(800, 600)
    game.option_screen('start')
    running = True

    while running:

        pygame.display.flip()
        game.is_button_clicked()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            elif event.type == PLAY:
                game.play()
            elif event.type == LETTERCLICKED:
                game.update(event)

        if game.is_won():
            game.option_screen("won")
        elif game.is_lost():
            game.option_screen("lost")
        elif game.is_playing():
            game.play_screen()





    


