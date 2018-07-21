# update_units.py #
# ============================================================================
# DEFINE FUNCTIONS FOR UPDATING THE STATUS OF ALL IN-GAME OBJECTS FOR THE
# GAME TO DRAW THEM PROPERLY ON THE SCREEN FOR EACH FRAME.
#

import random

from characters import PlayerAmmo, Enemy, EnemyAmmo


def update_playership(screen, playership, key_actions):
    """Control the player's main ship."""

    # control the ship's movement direction.
    if '>>>' in key_actions:
        playership.move_right = True
    if '<<<' in key_actions:
        playership.move_left = True
    if '+++' in key_actions:
        playership.upgrade()
    if '---' in key_actions:
        playership.downgrade()
    if '>>=' in key_actions:
        playership.move_right = False
    if '<<=' in key_actions:
        playership.move_left = False
    if 'INV' in key_actions:
        if playership.invincible_timer < 0:
            playership.invincible_timer = 0
        else:
            playership.invincible_timer = -1

    # move the ship.
    if playership.move_right:
        playership.go_right()
    if playership.move_left:
        playership.go_left()

    data = playership.get_data()

    if 0 < data['level'] < 4:
        if data['invincible']:
            screen.blit(playership.ship_inv_img, playership.rect)
        else:
            screen.blit(playership.ship_img, playership.rect)
    elif data['level'] == 4:
        if data['invincible']:
            screen.blit(playership.ship_inv_img, playership.rect)
        else:
            screen.blit(playership.ship_img, playership.rect)
        screen.blit(playership.turret_img, playership.turret_1_rect)
    elif data['level'] >= 5:
        if data['invincible']:
            screen.blit(playership.ship_inv_img, playership.rect)
        else:
            screen.blit(playership.ship_img, playership.rect)
        screen.blit(playership.turret_img, playership.turret_1_rect)
        screen.blit(playership.turret_img, playership.turret_2_rect)
    elif data['level'] == 0:
        return True

    return False


def update_player_ammo(screen, playership, playerammos, key_actions):
    """Control all player ship's ammo objects."""

    ship_data = playership.get_data()

    # turret fire.
    if ship_data['level'] >= 4 and ship_data['turret_ready']:
        playerammos.add(PlayerAmmo(playership, source=1))
        playership.turret_fire()
    if ship_data['level'] >= 5 and ship_data['turret_ready']:
        playerammos.add(PlayerAmmo(playership, source=2))

    # main ship fire.
    if ship_data['fire_ready'] and 'FFF' in key_actions:
        if ship_data['level'] == 1 or ship_data['level'] >= 7:
            playerammos.add(PlayerAmmo(playership))
            playership.ship_fire()
        elif ship_data['level'] == 2:
            playerammos.add(PlayerAmmo(playership, pos=-1),
                            PlayerAmmo(playership, pos=1))
            playership.ship_fire()
        elif ship_data['level'] == 3 or ship_data['level'] == 4 or \
                ship_data['level'] == 5:
            playerammos.add(PlayerAmmo(playership, pos=-1),
                            PlayerAmmo(playership, pos=1),
                            PlayerAmmo(playership))
            playership.ship_fire()
        elif ship_data['level'] == 6:
            playerammos.add(PlayerAmmo(playership, pos=-2),
                            PlayerAmmo(playership, pos=-1),
                            PlayerAmmo(playership, pos=1),
                            PlayerAmmo(playership, pos=2))
            playership.ship_fire()

    playership.cooldown()

    for ammo in playerammos:
        screen.blit(ammo.image, ammo.rect)
        out_of_bound = ammo.update()
        if out_of_bound:
            ammo.kill()


def update_enemies(screen, enemies, key_actions):
    """Control all enemy ship objects."""

    if '++1' in key_actions:
        enemies.add(Enemy(screen, 1))
    if '++2' in key_actions:
        enemies.add(Enemy(screen, 2))
    if '++3' in key_actions:
        enemies.add(Enemy(screen, 3))
    if '++4' in key_actions:
        enemies.add(Enemy(screen, 4))
    if '++0' in key_actions:
        enemies.add(Enemy(screen, 0))
    if 'NXT' in key_actions:
        enemies.empty()

    for enemy in enemies:
        if enemy.check_dead():
            enemy.kill()
        else:
            screen.blit(enemy.image, enemy.rect)
            enemy.update()


def update_enemy_ammo(screen, enemies, enemyammos):
    """Control all enemy's ammo objects."""

    for acting_enemy in enemies:
        # random firing.
        trigger = random.choice(range(210))
        tiny_trigger = random.choice(range(540))

        if 1 <= acting_enemy.type <= 3:
            if tiny_trigger == 1 and acting_enemy.timer == 0:
                enemyammos.add(EnemyAmmo(screen, acting_enemy))
                acting_enemy.reload()
        elif acting_enemy.type == 4 and acting_enemy.timer == 0:
            if trigger == 1:
                enemyammos.add(EnemyAmmo(screen, acting_enemy, 1, 1))
                enemyammos.add(EnemyAmmo(screen, acting_enemy, 1, 2))
                acting_enemy.reload()
            elif trigger == 2:
                enemyammos.add(EnemyAmmo(screen, acting_enemy, 2))
                acting_enemy.reload()
        elif acting_enemy.type == 0 and acting_enemy.drop_booster:
            enemyammos.add(EnemyAmmo(screen, acting_enemy))
            acting_enemy.kill()

        acting_enemy.cooldown()

    for enemy_ammo in enemyammos:
        screen.blit(enemy_ammo.image, enemy_ammo.rect)
        out_range = enemy_ammo.update()
        if out_range:
            enemy_ammo.kill()

