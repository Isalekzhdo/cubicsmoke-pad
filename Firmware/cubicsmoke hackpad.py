import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [
    board.A0,  # GPIO26/A0 - SW1
    board.A1,  # GPIO27/A1 - SW2
    board.A2,  # GPIO28/A2 - SW3
    board.A3,  # GPIO29/A3 - SW4
    board.D6,  # GPIO6 - SW5
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,  # Buttons pull to GND when pressed
)

keyboard.keymap = [
    [
        KC.A,                                                      # SW1
        KC.DELETE,                                                 # SW2
        KC.MACRO("Hello world!"),                                  # SW3
        KC.MACRO(Press(KC.LGUI), Tap(KC.S), Release(KC.LGUI)),    # SW4 - Save
        KC.B,                                                      # SW5
    ]
]

if __name__ == '__main__':
    keyboard.go()