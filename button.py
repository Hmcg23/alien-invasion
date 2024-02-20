import pygame.font

class Button:
    def __init__(self, ai_game, msg, x_position, y_position, width = 200, height = 50):
        """Initialize the button."""
        # Get the screen surface and its rectangle
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set button dimensions and colors
        self.width, self.height = width, height
        self.button_color = (0,200,200)
        self.text_color = (0, 200, 200)

        # Load font and set button rectangle
        self.font = pygame.font.Font("fonts/pixel.ttf", 32)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        
        # Set button position
        self.rect.center = self.screen_rect.center
        self.rect.y = y_position
        self.rect.x = x_position

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Prepare the button's message."""
        # Render the message text onto an image
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        # Center the message image on the button
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self, surface, color):
        """Draw the button on the screen."""
        # Create a surface for the button with transparent background
        button_surface = pygame.Surface(pygame.Rect(self.rect).size, pygame.SRCALPHA)
        pygame.draw.rect(button_surface, color, button_surface.get_rect(), border_radius = 12)
        # Blit the button surface onto the screen at its position
        surface.blit(button_surface, self.rect)
        # Blit the message image onto the screen at its position
        self.screen.blit(self.msg_image, self.msg_image_rect)

class Overlay:
    def __init__(self, ai_game):
        """Initialize the overlay."""
        # Get the screen surface and its rectangle
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set overlay dimensions
        self.width, self.height = 1200, 820
        self.rect = pygame.Rect(0, 0, self.width, self.height)
    
    def draw_overlay(self, surface):
        """Draw the overlay on the screen."""
        # Create a surface for the overlay with transparent background
        overlay_surface = pygame.Surface(pygame.Rect(pygame.Rect(self.width, self.height, self.width, self.height)).size, pygame.SRCALPHA)
        # Draw the overlay rectangle with semi-transparent black color
        pygame.draw.rect(overlay_surface, (0, 0, 0, 220), overlay_surface.get_rect())
        surface.blit(overlay_surface, self.rect)