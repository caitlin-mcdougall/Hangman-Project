import random
import pygame
from pygame.locals import *
from Hangman.Person import Person
from Hangman.Button import Button

black = (0, 0, 0)
background_color = (161, 241, 255)
LETTERCLICKED = USEREVENT + 1
PLAY = USEREVENT + 2


class GameInstance:
    hidden_word = ""
    displayed_word = ""
    category = ""
    buttons = []
    words = {}
    playing = False
    incorrect_guesses = 0
    correct_guesses = 0

    def __init__(self, w, h):
        self.screen_width = w
        self.screen_height = h
        self.screen = pygame.display.set_mode((w, h))
        self.person = Person()
        self.font = 'LexendDeca-Regular.ttf'
        self.form_word_dict()

    def form_word_dict(self):
        file = open('words.txt', 'r')

        for line in file:
            if line:
                temp_arr = line.split(", ")
                self.words[temp_arr[0]] = temp_arr[1]

        file.close()

    def generate_word(self):
        self.hidden_word = random.choice(list(self.words.keys()))
        self.category = self.words[self.hidden_word]
        self.displayed_word = '_ ' * len(self.hidden_word)

    def generate_keyboard(self):
        buttons = []
        w = 20
        h = 20
        x_margin = 50
        y_margin = 30
        for i in range(97, 110):
            x = (i - 97) * (2 * w) + x_margin
            y = y_margin
            button = Button(LETTERCLICKED, chr(i), w, h, x, y)
            buttons.append(button)
        for j in range(110, 123):
            x = (j - 110) * (2 * w) + x_margin
            y = 2 * h + y_margin
            button = Button(LETTERCLICKED, chr(j), w, h, x, y)
            buttons.append(button)
        self.buttons = buttons

    def is_button_clicked(self):
        for but in self.buttons:
            if but.clicked():
                self.buttons.remove(but)

    def is_won(self):
        if self.displayed_word.replace(" ", "") == self.hidden_word and self.correct_guesses != 0:
            self.playing = False
            return True
        return False

    def is_lost(self):
        if self.incorrect_guesses == 6:
            self.playing = False
            return True
        return False

    def play(self):
        self.reset()
        self.playing = True

    def is_playing(self):
        return self.playing

    def update(self, guess):

            found = False
            for x in range(0, len(self.hidden_word)):
                if self.hidden_word[x] == guess.action:
                    l_displayed_word = list(self.displayed_word)
                    l_displayed_word[x*2] = guess.action
                    new = ''
                    for i in l_displayed_word:
                        new += i
                    self.displayed_word = new
                    found = True
            if found:
                self.correct_guesses += 1
            else:
                self.incorrect_guesses += 1
                self.person.hang(self.incorrect_guesses)

    def reset(self):
        self.buttons = []
        self.generate_keyboard()
        self.hidden_word = ""
        self.displayed_word = ""
        self.category = ""
        self.generate_word()
        self.incorrect_guesses = 0
        self.correct_guesses = 0
        pygame.event.clear()

    def draw_basics(self):

        self.screen.fill(background_color)
        self.screen.blit(self.person.image, self.person.rect)
        for but in self.buttons:
            self.screen.blit(but.surf, but.rect)
            self.screen.blit(but.surf2, but.rect2)

    def play_screen(self):
        self.draw_basics()

        word_font = pygame.font.Font(self.font, 20)
        guess_word_text = word_font.render(self.displayed_word, True, black)
        word_rect = guess_word_text.get_rect()
        word_rect.center = (self.person.rect.right + 50, self.person.rect.center[1])
        category_text = word_font.render(self.category, True, black)
        category_rect = category_text.get_rect()
        category_rect.center = (word_rect.center[0], word_rect.top - 20)

        self.screen.blit(category_text, category_rect)
        self.screen.blit(guess_word_text, word_rect)

    def option_screen(self, state):
        self.buttons = []
        width = 60
        height = 40
        play_but = Button(PLAY, 'Play', width, height, self.screen_width/4, self.screen_height/5 * 4)
        quit_but = Button(QUIT, 'Exit', width, height, self.screen_width/4 * 3, self.screen_height/5 * 4)
        self.buttons.append(play_but)
        self.buttons.append(quit_but)
        self.draw_basics()
        if state == 'won':
            s = 'You won this round!'
        elif state == 'lost':
            s = 'Uh Oh... He died.'
        elif state == 'start':
            s = 'Hang that Man!'
        else:
            s = 'Something went wrong'
        message1_font = pygame.font.Font(self.font, 40)
        message1 = message1_font.render(s, True, black)
        message1_rect = message1.get_rect()
        message1_rect.center = (self.screen_width/2, height + 20)
        self.screen.blit(message1, message1_rect)
        if state != 'start':
            message2_font = pygame.font.Font(self.font, 20)
            message2 = message2_font.render('The answer was ' + self.hidden_word, True, black)
            message2_rect = message2.get_rect()
            message2_rect.center = (self.person.rect.right + 30, self.person.rect.center[1])
            self.screen.blit(message2, message2_rect)








