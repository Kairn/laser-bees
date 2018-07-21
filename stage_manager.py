# stage_manager.py #
# ============================================================================
# DEFINES FUNCTIONS TO CONTROL THE TRANSITION OF IN-GAME STAGES.
#
# STAGE BACKGROUND IMAGES NEED TO BE LOADED FROM THE GRAPHICS FOLDER.
#

import time

from characters import Enemy

current_stage = None


def stage_check(screen, playerammos, enemies, enemyammos, stages, imgs):
    """Define the process of setting up each in-game stage."""

    if stage_clear(enemies):
        try:
            line_up = next(stages)
            time.sleep(0.5)
        except StopIteration:
            return True
        else:
            playerammos.empty()
            enemyammos.empty()
            enemies.empty()

            # spawn new enemies for next stage.
            global current_stage
            current_stage = line_up.id[0]
            for type, amount in enumerate(line_up[1:-1], 1):
                if amount != 0:
                    for new_enemy in range(amount):
                        enemies.add(Enemy(screen, type))

            # spawn the upgrade pack.
            if line_up.upgrade:
                enemies.add(Enemy(screen, 0))

    # display the stage background images.
    if current_stage == '1':
        screen.blit(imgs[0], (0, 0))
    elif current_stage == '2':
        screen.blit(imgs[1], (0, 0))
    elif current_stage == '3':
        screen.blit(imgs[2], (0, 0))

    return False


def stage_clear(enemies):
    """Define the conditions for a stage clear."""

    if len(enemies) == 0:
        return True
    elif len(enemies) == 1:
        for lone_enemy in enemies:
            if lone_enemy.type == 0:
                return True
    else:
        return False

