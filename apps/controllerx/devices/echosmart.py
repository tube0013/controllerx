from core import LightController, MediaPlayerController, Stepper, action
from const import Light, MediaPlayer


class ZBT_CCTSwitch_D0001(LightController):
    # Different states reported from the controller:
    # on, off, brightness_toggle_click, brightness_toggle_hold, color_temp_toggle_click


    def get_zha_actions_mapping(self):
        return {
            "on": Light.TOGGLE,
            "off": Light.TOGGLE,
            "move_to_level": Light.CLICK_BRIGHTNESS_TOGGLE,
            "move_to_color_temp": Light.CLICK_COLOR_TEMP_TOGGLE,
            "move": Light.HOLD_BRIGHTNESS_TOGGLE,
            "step_with_on_off_0_43_5": Light.CLICK_BRIGHTNESS_UP,
            "stop": Light.RELEASE,
        }

    def default_delay(self):
        return 1000
