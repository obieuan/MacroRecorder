import time
import pickle
import pyautogui
import keyboard
import threading

recording = False

def record_macro(file_name):
    global recording
    macro_data = []

    print("Grabando macro... (presiona 'Ctrl + Alt + P' para detener)")

    def recording_thread():
        while recording:
            try:
                if keyboard.is_pressed("Ctrl") and keyboard.is_pressed("Alt") and keyboard.is_pressed("P"):
                    break

                time.sleep(0.01)  # Asegurar un pequeño retraso para no sobrecargar el sistema

                # Registrar la posición actual del mouse y las teclas presionadas
                x, y = pyautogui.position()
                keys = keyboard._pressed_events  # Acceder a las teclas presionadas (uso interno)
                keys_pressed = [k for k, v in keys.items() if v]

                macro_data.append((x, y, keys_pressed))
            except:
                break

        # Guardar los datos de la macro en un archivo
        with open(file_name, 'wb') as file:
            pickle.dump(macro_data, file)

        print("Macro grabada y guardada en", file_name)

    recording = True
    thread = threading.Thread(target=recording_thread)
    thread.start()

def stop_recording():
    global recording
    recording = False
