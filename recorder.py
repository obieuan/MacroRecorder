# recorder.py
import json
import threading
from pynput import mouse

# Global variable to store the recorded events
recorded_events = []

# Global variable to signal the recording process to stop
stop_recording_event = threading.Event()

# Function to start recording the mouse events
def start_recording(button_number):
    global recorded_events

    def on_click(x, y, button, pressed):
        if pressed:
            # Add the event data to the list
            event_data = {'type': 'click', 'x': x, 'y': y, 'button': button.name}
            recorded_events.append(event_data)

    def on_move(x, y):
        # Add the event data to the list
        event_data = {'type': 'move', 'x': x, 'y': y}
        recorded_events.append(event_data)

    # Start the mouse listener
    with mouse.Listener(on_click=on_click, on_move=on_move) as listener:
        print(f"Recording macro {button_number}. Press 'Ctrl + C' or click 'Stop' to stop recording.")
        stop_recording_event.clear()
        try:
            # Keep the script running until the 'stop_recording_event' is set
            while not stop_recording_event.is_set():
                pass
        except KeyboardInterrupt:
            pass

    # Save the recorded events to a JSON file
    output_file = f"macros/macro_data_{button_number}.json"
    with open(output_file, 'w') as f:
        json.dump(recorded_events, f)

    print(f"Macro {button_number} data saved to '{output_file}'")
    recorded_events = []

# Function to stop recording
def stop_recording():
    stop_recording_event.set()
