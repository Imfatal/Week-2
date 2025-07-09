#importing necessary libraries
import serial

#creating a dictionary 
_latest_data = {"value": ""}
ser = None

#function that connects to COM7
def read_serial_data(port='COM7', baudrate=9600):
    global _latest_data, ser
    try:
        #opening the port COM7 with a specified baudrate and timeout
        ser = serial.Serial(port, baudrate, timeout=1)
        print(f"Connected to {port}, waiting for data...")

        #going to an infinite loop where it keeps on writing the data received from COM7 to the _latest_data dictionary
        while True:
            #since data comes in binary format, we have to decode the data 
            line = ser.readline().decode().strip()
            if line:
                print("Received from COM7:", line)
                #data gets stored in the dictionary
                _latest_data["value"] = line

    #exceptions like Ctrl+C will trigger this block
    except Exception as e:
        print("Serial read error:", e)
    #if the try block is exited, this block runs and ensures that the port is closed
    finally:
        if ser and ser.is_open:
            ser.close()
            print("Serial port closed.")

#function to get lates reading from the dictionary
def get_latest_data():
    return _latest_data["value"]
