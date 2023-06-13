import json
from typing import List, Tuple

class PinConfiguration:
    def __init__(self, json_data: str) -> None:
        self.button_pins: List[str] = []
        self.joystick1_pins: Tuple[str, str] = ()
        self.joystick2_pins: Tuple[str, str] = ()

        self._extract_pins(json_data)

    def _extract_pins(self, json_data: str) -> None:
        data = json.loads(json_data)

        pin_mappings = data.get("pins", {})

        self.button_pins = [
            pin_mappings.get("button_a", ""),
            pin_mappings.get("button_b", ""),
            pin_mappings.get("button_x", ""),
            pin_mappings.get("button_y", ""),
            pin_mappings.get("button_start", ""),
            pin_mappings.get("button_select", ""),
            pin_mappings.get("left_joy_button", ""),
            pin_mappings.get("right_joy_button", ""),
            pin_mappings.get("button_lb", ""),
            pin_mappings.get("button_rb", ""),
            pin_mappings.get("button_lt", ""),
            pin_mappings.get("button_rt", ""),
        ]

        self.joystick1_pins = (
            pin_mappings.get("left_joy_x", ""),
            pin_mappings.get("left_joy_y", "")
        )

        self.joystick2_pins = (
            pin_mappings.get("right_joy_x", ""),
            pin_mappings.get("right_joy_y", "")
        )


# Example usage
json_data = '''
{
    "pins": {
        "left_joy_x": "gpio26",
        "left_joy_y": "gpio27",
        "right_joy_x": "gpio28",
        "right_joy_y": "gpio29",
        "button_a": "gpio0",
        "button_b": "gpio1",
        "button_x": "gpio2",
        "button_y": "gpio3",
        "button_select": "gpio4",
        "button_start": "gpio5",
        "left_joy_button": "gpio6",
        "right_joy_button": "gpio7",
        "button_lb": "gpio8",
        "button_rb": "gpio9",
        "button_lt": "gpio10",
        "button_rt": "gpio11"
    }
}
'''

pin_config = PinConfiguration(json_data)

print("button_pins:", pin_config.button_pins)
print("joystick1_pins:", pin_config.joystick1_pins)
print("joystick2_pins:", pin_config.joystick2_pins)
