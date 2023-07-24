import time
import pickle
import pyautogui
import keyboard
import threading

ralent = 0.002
playing = False

def play_macro(file_name, delay=ralent):
    global playing
    with open(file_name, 'rb') as file:
        macro_data = pickle.load(file)

    print("Reproduciendo macro... (presiona 'F10' para detener)")

    # Deshabilitar pausa y mensajes de espera para mejorar el rendimiento de pyautogui
    pyautogui.PAUSE = ralent
    pyautogui.FAILSAFE = False

    playing = True
    for x, y, keys_pressed in macro_data:
        pyautogui.moveTo(x, y)

        # Simular las teclas presionadas durante el registro
        for key in keys_pressed:
            keyboard.press(key)

        # Eliminar el tiempo de espera entre acciones
        time.sleep(delay)

        # Liberar las teclas al final
        for key in keys_pressed:
            keyboard.release(key)

        if not playing:
            break

    print("Macro reproducida")

def stop_playing():
    global playing
    playing = False

def play_macro_wrapper():
    # Iniciar la reproducción en un hilo separado para permitir la detección de la tecla 'F10'
    player_thread = threading.Thread(target=play_macro, args=("macro_data.pkl",))
    player_thread.start()

    # Esperar a que el usuario presione 'F10' para detener la reproducción
    while player_thread.is_alive():
        if keyboard.is_pressed("F10"):
            stop_playing()
            break

if __name__ == "__main__":
    play_macro_wrapper()
