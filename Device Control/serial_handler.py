#importing libraries
import serial
import time

#setting up connection to the COM7 port at a specified baudrate and timeout
esp = serial.Serial(port='COM7', baudrate=9600, timeout=2)

#A command (which is received from app.py) is sent to the COM7 which then gets read by esp32.py and accordingly a response is sent back via the same port
#and then that response is recieved by this script
def send_command(command):
    try:
        print("Sending:", command)
        esp.reset_input_buffer()
        esp.write((command + '\n').encode())
        time.sleep(0.5)

        if esp.in_waiting:
            response = esp.readline().decode().strip()
            print("Received:", response)
            return response
        else:
            print("Nothing received.")
            return "No response from ESP32."
    except Exception as e:
        print("Exception:", e)
        return f"Error: {e}"

