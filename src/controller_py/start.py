import json
from typing import List, Tuple
import microcontroller

class PinConfiguration:
    """
    Reads the pin configuration from a json file
    """
    def __init__(self, json_path: str) -> None:
        self.face_button_pins: List[str] = []
        self.dpad_button_pins: List[str] = []
        self.trigger_button_pins: List[str] = []
        self.button_pins: List[str] = []
        self.joystick1_pins: Tuple[str, str] = ()
        self.joystick2_pins: Tuple[str, str] = ()
        self._json_path = json_path
        self.read_json()

    def read_json(self):
        try:
            f = open(self._json_path, 'r')
            data_string = f.read()
            f.close()
            self._extract_pins(json_data=data_string)
        except:
            print('settings file load failed')

    def _extract_pins(self, json_data: str) -> None:
        data = json.loads(json_data)

        pin_mappings = data.get("pins", {})
        self.face_button_pins = [
            getattr(microcontroller.pin,pin_mappings.get("button_a", "")),
            getattr(microcontroller.pin,pin_mappings.get("button_b", "")),
            getattr(microcontroller.pin,pin_mappings.get("button_x", "")),
            getattr(microcontroller.pin,pin_mappings.get("button_y", ""))
        ]
        self.dpad_button_pins = [
            getattr(microcontroller.pin,pin_mappings.get("dpad_up", "")),
            getattr(microcontroller.pin,pin_mappings.get("dpad_down", "")),
            getattr(microcontroller.pin,pin_mappings.get("dpad_left", "")),
            getattr(microcontroller.pin,pin_mappings.get("dpad_right", ""))
        ]
        self.trigger_button_pins = [
            getattr(microcontroller.pin,pin_mappings.get("button_lb", "")),
            getattr(microcontroller.pin,pin_mappings.get("button_rb", "")),
            getattr(microcontroller.pin,pin_mappings.get("button_lt", "")),
            getattr(microcontroller.pin,pin_mappings.get("button_rt", ""))
        ]
        self.button_pins = [
            getattr(microcontroller.pin,pin_mappings.get("button_start", "")),
            getattr(microcontroller.pin,pin_mappings.get("button_select", "")),
            getattr(microcontroller.pin,pin_mappings.get("left_joy_button", "")),
            getattr(microcontroller.pin,pin_mappings.get("right_joy_button", ""))
        ]
        self.joystick1_pins = (
            getattr(microcontroller.pin,pin_mappings.get("left_joy_x", "")),
            getattr(microcontroller.pin,pin_mappings.get("left_joy_y", ""))
        )

        self.joystick2_pins = (
            getattr(microcontroller.pin,pin_mappings.get("right_joy_x", "")),
            getattr(microcontroller.pin,pin_mappings.get("right_joy_y", ""))
        )


# Example usage
# json_data = '''
# {
#     "pins": {
#         "left_joy_x": "gpio26",
#         "left_joy_y": "gpio27",
#         "right_joy_x": "gpio28",
#         "right_joy_y": "gpio29",
#         "button_a": "gpio0",
#         "button_b": "gpio1",
#         "button_x": "gpio2",
#         "button_y": "gpio3",
#         "button_select": "gpio4",
#         "button_start": "gpio5",
#         "left_joy_button": "gpio6",
#         "right_joy_button": "gpio7",
#         "button_lb": "gpio8",
#         "button_rb": "gpio9",
#         "button_lt": "gpio10",
#         "button_rt": "gpio11",
#         "dpad_up": "gpio12",
#         "dpad_down": "gpio13",
#         "dpad_left": "gpio14",
#         "dpad_right": "gpio15"
#     }
# }
# '''

# pin_config = PinConfiguration("json_data.json")

# print("button_pins:", pin_config.button_pins)
# print("face_button_pins:", pin_config.face_button_pins)
# print("dpad_button_pins:", pin_config.dpad_button_pins)
# print("trigger_button_pins:", pin_config.trigger_button_pins)
# print("joystick1_pins:", pin_config.joystick1_pins)
# print("joystick2_pins:", pin_config.joystick2_pins)
