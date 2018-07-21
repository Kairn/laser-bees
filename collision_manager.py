# collision_manager.py #
# ============================================================================
# DEFINE FUNCTIONS TO CHECK AND CONTROL COLLISION EVENTS DURING THE GAME.
#

import pygame


def offensive_check(playerammos, enemies):
    """Define the event of the player ship hits a target."""

    ofs_collisions = pygame.sprite.groupcollide(playerammos, enemies,
                                                True, False)

    for ammo, targets in ofs_collisions.items():
        targets[0].health -= ammo.power


def defensive_check(playership, enemyammos):
    """Define the event of the player ship suffers an attack."""

    dfs_collisions = pygame.sprite.spritecollide(playership, enemyammos, False)

    for eammo in dfs_collisions:
        if eammo.booster:
            playership.upgrade()
        else:
            if not playership.get_data()['invincible']:
                playership.downgrade()
                playership.invincible_timer = 120
        eammo.kill()

