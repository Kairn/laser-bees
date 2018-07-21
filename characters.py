# characters.py #
# ============================================================================
# DEFINE ALL IN-GAME OBJECT TYPES.
# THEY NEED SPRITE FILES IN THE IMAGES FOLDER TO INITIALIZE PROPERLY.
#

import pygame
from random import choice


class PlayerShip(pygame.sprite.Sprite):
    """Define the main ship the player controls."""

    def __init__(self, settings, screen):
        super().__init__()
        self._data = {}
        self.screen_rect = screen.get_rect()
        self.level = 1
        self.speed = settings.playership_speed
        self.move_left = False
        self.move_right = False
        self.ship_cooldown = 0
        self.turret_cooldown = 0
        self.invincible_timer = 0

        self.ship_img = pygame.image.load('images/objects/battlers/player_ship.png')
        self.ship_inv_img = pygame.image.load('images/objects/battlers/player_ship_inv.png')
        self.turret_img = pygame.image.load('images/objects/battlers/turret.png')
        self.rect = self.ship_img.get_rect()
        self.turret_1_rect = self.turret_img.get_rect()
        self.turret_2_rect = self.turret_img.get_rect()

        self.set_initial_position()

    def set_initial_position(self):
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx
        self.turret_1_rect.bottom = self.screen_rect.bottom
        self.turret_2_rect.bottom = self.screen_rect.bottom
        self.turret_1_rect.right = self.rect.left - 5
        self.turret_2_rect.left = self.rect.right + 5

    def go_right(self):
        if self.turret_2_rect.right < self.screen_rect.right:
            self.rect.centerx += self.speed
            self.turret_1_rect.centerx += self.speed
            self.turret_2_rect.centerx += self.speed

    def go_left(self):
        if self.turret_1_rect.left > 0:
            self.rect.centerx -= self.speed
            self.turret_1_rect.centerx -= self.speed
            self.turret_2_rect.centerx -= self.speed

    def ship_fire(self):
        self.ship_cooldown = 60

    def turret_fire(self):
        self.turret_cooldown = 90

    def cooldown(self):
        if self.ship_cooldown > 0:
            self.ship_cooldown -= 1
        if self.turret_cooldown > 0:
            self.turret_cooldown -= 1
        if self.invincible_timer > 0:
            self.invincible_timer -= 1

    def upgrade(self):
        if self.level < 10:
            self.level += 1

    def downgrade(self):
        if self.level > 0:
            self.level -= 1

    def get_data(self):
        self._data['ship_pos'] = self.rect
        self._data['level'] = self.level
        self._data['t1_pos'] = self.turret_1_rect
        self._data['t2_pos'] = self.turret_2_rect
        self._data['fire_ready'] = self.ship_cooldown == 0
        self._data['turret_ready'] = self.turret_cooldown == 0
        self._data['invincible'] = self.invincible_timer != 0

        return self._data


class PlayerAmmo(pygame.sprite.Sprite):
    """Define all ammo types fired from the main ship."""

    # load ammo sprites.
    ammo_std = pygame.image.load('images/objects/projectiles/ammo_1.png')
    ammo_big1 = pygame.image.load('images/objects/projectiles/ammo_2.png')
    ammo_big2 = pygame.image.load('images/objects/projectiles/ammo_3.png')
    ammo_big3 = pygame.image.load('images/objects/projectiles/ammo_4.png')
    ammo_super = pygame.image.load('images/objects/projectiles/ammo_5.png')

    def __init__(self, playership, source=0, pos=0):
        super().__init__()
        self.ship_data = playership.get_data()
        self.ship_rect = self.ship_data['ship_pos']
        self.t1_rect = self.ship_data['t1_pos']
        self.t2_rect = self.ship_data['t2_pos']
        self.level = self.ship_data['level']
        self.source = source
        self.pos = pos

        self.load_ammo()

    def load_ammo(self):
        if self.source == 0:
            if self.level <= 6:
                self.speed = 3
                self.power = 1
                self.image = PlayerAmmo.ammo_std
                self.rect = self.image.get_rect()
                self.rect.bottom = self.ship_rect.top
                self.rect.centerx = self.ship_rect.centerx + self.pos * 7
            elif self.level == 7:
                self.speed = 4
                self.power = 4
                self.image = PlayerAmmo.ammo_big1
                self.rect = self.image.get_rect()
                self.rect.bottom = self.ship_rect.top
                self.rect.centerx = self.ship_rect.centerx
            elif self.level == 8:
                self.speed = 5
                self.power = 5
                self.image = PlayerAmmo.ammo_big2
                self.rect = self.image.get_rect()
                self.rect.bottom = self.ship_rect.top
                self.rect.centerx = self.ship_rect.centerx
            elif self.level == 9:
                self.speed = 6
                self.power = 6
                self.image = PlayerAmmo.ammo_big3
                self.rect = self.image.get_rect()
                self.rect.bottom = self.ship_rect.top
                self.rect.centerx = self.ship_rect.centerx
            elif self.level == 10:
                self.speed = 6
                self.power = 7
                self.image = PlayerAmmo.ammo_super
                self.rect = self.image.get_rect()
                self.rect.bottom = self.ship_rect.top
                self.rect.centerx = self.ship_rect.centerx
        elif self.source == 1:
            self.speed = 2
            self.power = 1
            self.image = PlayerAmmo.ammo_std
            self.rect = self.image.get_rect()
            self.rect.bottom = self.t1_rect.top
            self.rect.centerx = self.t1_rect.centerx
        elif self.source == 2:
            self.speed = 2
            self.power = 1
            self.image = PlayerAmmo.ammo_std
            self.rect = self.image.get_rect()
            self.rect.bottom = self.t2_rect.top
            self.rect.centerx = self.t2_rect.centerx

    def update(self):
        self.rect.centery -= self.speed
        return self.rect.bottom <= 0


class Enemy(pygame.sprite.Sprite):
    """Define all enemy ship types and the upgrade pack."""

    typeA = pygame.image.load('images/objects/battlers/enemy_a.png')
    typeB = pygame.image.load('images/objects/battlers/enemy_b.png')
    typeC = pygame.image.load('images/objects/battlers/enemy_c.png')
    typeD = pygame.image.load('images/objects/battlers/enemy_d.png')
    upgrade_pack = pygame.image.load('images/objects/battlers/treasure_chest.png')

    def __init__(self, screen, type):
        super().__init__()
        self.screen_rect = screen.get_rect()
        self.type = type
        self.timer = 120
        self.mov = choice((-1, 1))
        self.drop_booster = False

        self.prepare_unit()

    def prepare_unit(self):
        if self.type == 1:
            self.health = 3
            self.speed = 1
            self.cooldown_time = 270
            self.image = Enemy.typeA
            self.rect = self.image.get_rect()
            self.rect.top = self.screen_rect.top

            # random spawning location.
            self.rect.centerx = choice(range(self.rect.width,
                                       self.screen_rect.width
                                       - self.rect.width))
        elif self.type == 2:
            self.health = 6
            self.speed = 1
            self.cooldown_time = 120
            self.image = Enemy.typeB
            self.rect = self.image.get_rect()
            self.rect.top = self.screen_rect.top
            self.rect.centerx = choice(range(self.rect.width,
                                             self.screen_rect.width
                                             - self.rect.width))
        elif self.type == 3:
            self.health = 9
            self.speed = 3
            self.cooldown_time = 90
            self.image = Enemy.typeC
            self.rect = self.image.get_rect()
            self.rect.top = self.screen_rect.top
            self.rect.centerx = choice(range(self.rect.width,
                                             self.screen_rect.width
                                             - self.rect.width))
        elif self.type == 4:
            self.health = 15
            self.speed = 4
            self.cooldown_time = 120
            self.image = Enemy.typeD
            self.rect = self.image.get_rect()
            self.rect.top = self.screen_rect.top
            self.rect.centerx = choice(range(self.rect.width,
                                             self.screen_rect.width
                                             - self.rect.width))
        elif self.type == 0:
            self.health = 1
            self.speed = 1
            self.cooldown_time = 0
            self.image = Enemy.upgrade_pack
            self.rect = self.image.get_rect()
            self.rect.top = self.screen_rect.top
            self.rect.centerx = choice(range(self.rect.width,
                                             self.screen_rect.width
                                             - self.rect.width))

    def update(self):
        if self.timer > 0:
            self.timer -= 1

        # random horizontal movements.
        if self.rect.right >= self.screen_rect.right:
            self.mov = -1
        elif self.rect.left <= self.screen_rect.left:
            self.mov = 1
        else:
            if choice(range(150)) == 2:
                self.mov *= -1
        self.rect.centerx += self.speed * self.mov

    def reload(self):
        self.timer += self.cooldown_time

    def cooldown(self):
        if self.timer > 0:
            self.timer -= 1

    def check_dead(self):
        if self.health <= 0 and self.type != 0:
            return True
        elif self.health <= 0 and self.type == 0:
            self.drop_booster = True
            return False


class EnemyAmmo(pygame.sprite.Sprite):
    """Define all ammo types fired from enemy ships and the upgrade star."""

    silver_bolt = pygame.image.load('images/objects/projectiles/ammo_a.png')
    fire_blast = pygame.image.load('images/objects/projectiles/ammo_b.png')
    mana_blast = pygame.image.load('images/objects/projectiles/ammo_c.png')
    bounce_ball = pygame.image.load('images/objects/projectiles/ammo_d_1.png')
    laser_bolt = pygame.image.load('images/objects/projectiles/ammo_d_2.png')
    booster = pygame.image.load('images/objects/projectiles/star.png')

    def __init__(self, screen, enemy, kind=1, pos=1):
        super().__init__()
        self.screen_rect = screen.get_rect()
        self.enemy = enemy
        self.enemy_rect = self.enemy.rect
        self.kind = kind
        self.direction = 0
        self.pos = pos
        self.booster = False

        self.load_ammo()

    def load_ammo(self):
        if self.enemy.type == 1:
            self.speed = 2
            self.image = EnemyAmmo.silver_bolt
            self.rect = self.image.get_rect()
            self.rect.top = self.enemy_rect.bottom
            self.rect.centerx = self.enemy_rect.centerx
        elif self.enemy.type == 2:
            self.speed = 3
            self.image = EnemyAmmo.fire_blast
            self.rect = self.image.get_rect()
            self.rect.top = self.enemy_rect.bottom
            self.rect.centerx = self.enemy_rect.centerx
        elif self.enemy.type == 3:
            self.speed = 4
            self.image = EnemyAmmo.mana_blast
            self.rect = self.image.get_rect()
            self.rect.top = self.enemy_rect.bottom
            self.rect.centerx = self.enemy_rect.centerx
        elif self.enemy.type == 4:
            if self.kind == 1:
                self.speed = 5
                self.image = EnemyAmmo.laser_bolt
                self.rect = self.image.get_rect()
                self.rect.centerx = self.enemy_rect.centerx
                if self.pos == 1:
                    self.rect.top = self.enemy_rect.bottom
                elif self.pos == 2:
                    self.rect.top = self.enemy_rect.bottom + self.rect.height
            elif self.kind == 2:
                self.speed = 3
                self.direction = choice((1, -1))
                self.image = EnemyAmmo.bounce_ball
                self.rect = self.image.get_rect()
                self.rect.top = self.enemy_rect.bottom
                self.rect.centerx = self.enemy_rect.centerx
        elif self.enemy.type == 0:
            self.speed = 2
            self.booster = True
            self.image = EnemyAmmo.booster
            self.rect = self.image.get_rect()
            self.rect.top = self.enemy_rect.bottom
            self.rect.centerx = self.enemy_rect.centerx

    def update(self):
        if self.kind == 2:
            self.rect.centery += self.speed
            self.rect.centerx += self.speed * self.direction
            if self.rect.left <= 0:
                self.rect.left = 0
                self.direction *= -1
            elif self.rect.right >= self.screen_rect.width:
                self.rect.right = self.screen_rect.width
                self.direction *= -1
        elif self.kind == 1:
            self.rect.centery += self.speed
        return self.rect.top >= self.screen_rect.height

