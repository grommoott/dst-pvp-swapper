import keyboard

isEnabled = False
isPressed = False


def onEnable():
    global isEnabled
    isEnabled = not isEnabled
    keyboard.release("h")

    if isEnabled:
        print("Enabled")
    else:
        print("Disabled")


keyboard.add_hotkey("ctrl+shift+f", onEnable)


def onAttackPress(event):
    global isPressed
    if isEnabled and not isPressed:
        isPressed = True
        keyboard.press("1")
        keyboard.release("1")
        keyboard.press("h")


def onAttackRelease(event):
    global isPressed
    if isEnabled:
        isPressed = False
        keyboard.press("1")
        keyboard.release("1")
        keyboard.release("h")


keyboard.on_press_key("f", onAttackPress)
keyboard.on_release_key("f", onAttackRelease)

keyboard.wait()
