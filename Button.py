import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, event_type, action, width, height, x, y):
        super(Button, self).__init__()
        self.action = action
        self.surf = pygame.Surface((width, height))
        self.surf.fill((255, 255, 255))
        self.font = pygame.font.Font('LexendDeca-Regular.ttf', 10)
        self.surf2 = self.font.render(action, True, (0, 0, 0), (255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect2 = self.surf2.get_rect()
        self.rect.center = (x, y)
        self.rect2.center = (x, y)
        self.surf = pygame.transform.scale(self.surf, (width, height))
        self.event = pygame.event.Event(event_type, action=self.action)

    def clicked(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.rect.left < mouse[0] < self.rect.right and self.rect.top < mouse[1] < self.rect.bottom:
            if click[0]:
                pygame.event.post(self.event)
                return True

