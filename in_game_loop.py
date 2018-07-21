# in_game_loop.py #
# ============================================================================
# DEFINE A LARGE FUNCTION TO MANAGE THE ENTIRE IN-GAME LOOP BETWEEN THE START
# AND THE END OF A GAME SESSION.
#
# GAME STAGES ARE ALSO DEFINED IN THIS MODULE, AND THEY CAN BE MODIFIED TO
# CHANGE THE DIFFICULTY OF THE GAME.
#
# SCREEN BACKGROUND IMAGES NEED TO BE LOADED FROM THE IMAGES FOLDER.
# 

import sys
import time
from collections import namedtuple

import pygame

import update_manager
import characters
from stage_manager import stage_check
import collision_manager


def in_game(clock, settings, screen, active=True):
    """Manage all events in an active game session."""

    debug = settings.debug_mode

    win_bg = pygame.image.load('images/screen_images/victory_screen.jpg')
    loss_bg = pygame.image.load('images/screen_images/game_over_screen.jpg')

    # set up game stages.
    stage_imgs = [pygame.image.load('images/backgrounds/stage_1.jpg'),
                  pygame.image.load('images/backgrounds/stage_2.jpg'),
                  pygame.image.load('images/backgrounds/stage_3.jpg')]

    Stage = namedtuple('stage', 'id A B C D upgrade')
    game_stages = iter(
        [
            Stage('1-1', 6, 0, 0, 0, False), Stage('1-2', 8, 0, 0, 0, True),
            Stage('1-3', 9, 0, 0, 0, False), Stage('1-4', 10, 0, 0, 0, True),
            Stage('1-5', 6, 2, 0, 0, False), Stage('1-6', 8, 2, 0, 0, True),
            Stage('1-7', 9, 2, 0, 0, False), Stage('1-8', 10, 3, 0, 0, True),
            Stage('1-9', 12, 0, 0, 0, False), Stage('1-10', 12, 2, 1, 0, True),
            Stage('2-1', 8, 4, 0, 0, False), Stage('2-2', 10, 4, 0, 0, True),
            Stage('2-3', 12, 0, 2, 0, False), Stage('2-4', 10, 2, 2, 0, True),
            Stage('2-5', 18, 0, 0, 0, False), Stage('2-6', 12, 0, 4, 0, True),
            Stage('2-7', 14, 1, 1, 1, False), Stage('2-8', 12, 3, 3, 0, True),
            Stage('2-9', 12, 3, 2, 1, False), Stage('2-10', 16, 2, 2, 1, True),
            Stage('3-1', 6, 6, 3, 0, False), Stage('3-2', 8, 4, 4, 1, True),
            Stage('3-3', 8, 0, 4, 2, False), Stage('3-4', 10, 10, 0, 0, True),
            Stage('3-5', 16, 2, 2, 2, False), Stage('3-6', 8, 8, 6, 0, True),
            Stage('3-7', 0, 6, 6, 4, False), Stage('3-8', 10, 0, 0, 5, True),
            Stage('3-9', 7, 6, 5, 3, False), Stage('3-10', 9, 9, 4, 4, True),
        ]
    )

    game_playership = characters.PlayerShip(settings, screen)
    game_playerammos = pygame.sprite.Group()
    game_enemies = pygame.sprite.Group()
    game_enemyammos = pygame.sprite.Group()

    while active:

        pause = False
        key_actions = set()

        # respond to key presses/releases.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_e:
                    active = False
                if event.key == pygame.K_RIGHT:
                    key_actions.add('>>>')
                    key_actions.add('<<=')
                elif event.key == pygame.K_LEFT:
                    key_actions.add('<<<')
                    key_actions.add('>>=')
                if event.key == pygame.K_z and debug:
                    key_actions.add('+++')
                elif event.key == pygame.K_x and debug:
                    key_actions.add('---')
                if event.key == pygame.K_SPACE:
                    key_actions.add('FFF')
                if event.key == pygame.K_g and debug:
                    key_actions.add('INV')
                if event.key == pygame.K_1 and debug:
                    key_actions.add('++1')
                if event.key == pygame.K_2 and debug:
                    key_actions.add('++2')
                if event.key == pygame.K_3 and debug:
                    key_actions.add('++3')
                if event.key == pygame.K_4 and debug:
                    key_actions.add('++4')
                if event.key == pygame.K_0 and debug:
                    key_actions.add('++0')
                if event.key == pygame.K_n and debug:
                    key_actions.add('NXT')
                if event.key == pygame.K_p:
                    pause = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    key_actions.add('>>=')
                if event.key == pygame.K_LEFT:
                    key_actions.add('<<=')

        # pause/resume the game.
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pause = False
            clock.tick(30)

        screen.fill(settings.action_bg_color)

        # update in-game objects.
        win_check = stage_check(screen, game_playerammos, game_enemies,
                                game_enemyammos, game_stages, stage_imgs)
        loss_check = update_manager.update_playership(screen, game_playership,
                                                    key_actions)
        update_manager.update_enemies(screen, game_enemies, key_actions)
        update_manager.update_player_ammo(screen, game_playership,
                                        game_playerammos, key_actions)
        update_manager.update_enemy_ammo(screen, game_enemies, game_enemyammos)

        # check collisions.
        collision_manager.offensive_check(game_playerammos, game_enemies)
        collision_manager.defensive_check(game_playership, game_enemyammos)

        # check for game-ending events.
        if loss_check:
            screen.blit(loss_bg, (0, 0))
            pygame.display.flip()
            time.sleep(4)
            active = False
        if win_check:
            screen.blit(win_bg, (0, 0))
            pygame.display.flip()
            time.sleep(5)
            active = False

        clock.tick(settings.frame_rate)
        pygame.display.flip()

