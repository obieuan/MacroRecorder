import json
import pyautogui
import time
import winput

# Función para simular el movimiento del mouse
def move_mouse(x, y):
    pyautogui.moveTo(x, y, duration=0.5)

# Función para simular el clic del mouse
def click(x, y, pressed):
    pyautogui.moveTo(x, y, duration=0.1)
    if pressed:
        winput.press_mouse_button(winput.LEFT_MOUSE_BUTTON)
    else:
        winput.release_mouse_button(winput.LEFT_MOUSE_BUTTON)


# Función para simular la presión de una tecla
def press_key(key):
    pyautogui.press(key)

# Función para leer el JSON y ejecutar las acciones
def run_macro_from_json(file_path):
    with open(file_path, 'r') as file:
        macro_data = json.load(file)

    for action in macro_data:
        if action['type'] == 'move':
            move_mouse(action['x'], action['y'])
        elif action['type'] == 'click':
            click(action['x'], action['y'], action['pressed'])
        elif action['type'] == 'keypress':
            press_key(action['key'])
        # Pausa de 0.1 segundos entre cada acción
        time.sleep(0.1)

