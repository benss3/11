time = 0

def on_button_pressed_ab():
    global time
    time = 0
    basic.show_number(time)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
