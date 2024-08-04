import keyboard

enabled = False
isPressed = False


def on_enable():
    global enabled
    enabled = True
    keyboard.release("h")
    print("Enabled")


keyboard.add_hotkey("ctrl+shift+f", on_enable)


def on_attack_press(event):
    global isPressed
    if enabled and not isPressed:
        isPressed = True
        keyboard.press("1")
        keyboard.release("1")
        keyboard.press("h")


def on_attack_release(event):
    global isPressed
    if enabled:
        isPressed = False
        keyboard.press("1")
        keyboard.release("1")
        keyboard.release("h")


keyboard.on_press_key("f", on_attack_press)
keyboard.on_release_key("f", on_attack_release)

keyboard.wait()
