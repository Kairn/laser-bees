# settings.py #
# ============================================================================
# DEFINE THE SETTINGS CLASS FOR THE GAME TO SET UP A SPECIFIED ENVIRONMENT.
#
# WARNING: THE GAME MIGHT NOT BEHAVE PROPERLY IF YOU CHANGE THE VALUES IN THIS
# FILE. BACK UP THIS FILE IF YOU WISH TO EDIT ANYTHING.
#


class Settings:
    """Define all in-game specifications."""

    def __init__(self, debug=False):

        self._debug_mode = debug
        self._window_size = (675, 900)
        self._inert_bg_color = (255, 255, 255)
        self._action_bg_color = (253, 237, 236)
        self._frame_rate = 60

        self._playership_speed = 3

    @property
    def debug_mode(self):
        """Currently support force game-over; upgrade/downgrade the
        player ship; set player ship invincible/normal; spawn single enemy or
        upgrade pack; enter next stage;"""
        return self._debug_mode

    @property
    def window_size(self):
        return self._window_size

    @property
    def inert_bg_color(self):
        """This is for testing only."""
        return self._inert_bg_color

    @property
    def action_bg_color(self):
        """This is for testing only."""
        return self._action_bg_color

    @property
    def frame_rate(self):
        return self._frame_rate

    @property
    def playership_speed(self):
        return self._playership_speed

