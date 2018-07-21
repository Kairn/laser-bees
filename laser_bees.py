# laser_bees.py #
# ============================================================================
# RUNNING THIS SCRIPT WILL LAUNCH THE GAME.
# PLEASE MAKE SURE ALL ASSOCIATED FILES ARE INCLUDED IN THE SAME DIRECTORY.
#
# IF THE GAME DOES NOT START PROPERLY, CHECK WHETHER YOU HAVE PYGAME INSTALLED.
# CURRENTLY PYGAME DOES NOT SUPPORT PYTHON3 ON LINUX, SO THIS GAME CAN ONLY BE
# RUN ON A WINDOWS PLATFORM.
#
# RUN COMMAND: python Laser_Bees.py
# 

import sys

import pygame

import settings
from in_game_loop import in_game


def run_game():
    """Load data, set up the game environment, and launch the main event loop."""

    pygame.init()
    pygame.display.set_caption("Laser Bees")
    game_clock = pygame.time.Clock()

    in_game_state = False
    game_settings = settings.Settings(debug=True)      # change this to True to enable cheat mode.
    game_screen = pygame.display.set_mode(game_settings.window_size)

    start_bg = pygame.image.load('images/screen_images/start_screen.jpg')

    while True:                                         # the main game loop.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()                          # ESC key for quitting.
                elif event.key == pygame.K_RETURN:
                    in_game_state = True                # Enter key to start.

        if in_game_state:
            in_game(game_clock, game_settings, game_screen)
            in_game_state = False

        # game_screen.fill(game_settings.inert_bg_color)
        game_screen.blit(start_bg, (0, 0))

        game_clock.tick(game_settings.frame_rate)
        pygame.display.flip()


if __name__ == '__main__':
    run_game()
