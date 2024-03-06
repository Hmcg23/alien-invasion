import pygame

class Overlay:
    def __init__(self, ai_game):
        """Initialize the overlay."""
        # Get the screen surface and its rectangle
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.transparency = 0
        self.increasing = True
        self.blink = False

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

    def blink_overlay(self, surface, blink):
        self.blink = blink
        """Draw the overlay on the screen."""
        # Create a surface for the overlay with transparent background
        overlay_surface = pygame.Surface(pygame.Rect(pygame.Rect(self.width, self.height, self.width, self.height)).size, pygame.SRCALPHA)
        # Draw the overlay rectangle with semi-transparent black color

        pygame.draw.rect(overlay_surface, (99, 0, 33, self.transparency), overlay_surface.get_rect())

        surface.blit(overlay_surface, self.rect)

        if self.blink:
            if self.increasing:
                if self.transparency >= 100:
                    self.increasing = False
                else:
                    self.transparency += 5
            elif not self.increasing:
                if self.transparency <= 0:
                    self.increasing = True
                else:
                    self.transparency -= 5
        else:
            self.transparency -= 1
            if self.transparency <= 0:
                self.transparency = 0