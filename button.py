import pygame.font

class Button:
    def __init__(self, ai_game, msg, x_position, y_position, width = 200, height = 50):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = width, height
        self.button_color = (0,200,200)
        self.text_color = (0, 200, 200)

        self.font = pygame.font.Font("fonts/pixel.ttf", 32)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        
        self.rect.center = self.screen_rect.center
        self.rect.y = y_position
        self.rect.x = x_position

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self, surface, color):
        button_surface = pygame.Surface(pygame.Rect(self.rect).size, pygame.SRCALPHA)
        pygame.draw.rect(button_surface, color, button_surface.get_rect(), border_radius = 12)
        surface.blit(button_surface, self.rect)
        
        self.screen.blit(self.msg_image, self.msg_image_rect)

class Overlay:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 1200, 820
        self.rect = pygame.Rect(0, 0, self.width, self.height)
    
    def draw_overlay(self, surface):
        button_surface = pygame.Surface(pygame.Rect(pygame.Rect(self.width, self.height, self.width, self.height)).size, pygame.SRCALPHA)
        pygame.draw.rect(button_surface, (0, 0, 0, 220), button_surface.get_rect())
        surface.blit(button_surface, self.rect)