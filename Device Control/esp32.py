#importing libraries
import serial

#sets up communication with COM8 port at a specified baudrate and timeout
esp_sim = serial.Serial('COM8', 9600, timeout=1)

print("ESP32 emulator started (COM8)")

#the loops keeps on running and ckecks if there is any data available in the port, if yes then reads it and accordingly
#send a reponse on the same port
while True: 
    # Check if there is data available to read
    if esp_sim.in_waiting:
        #reading by decon=ding the msg received from the port
        cmd = esp_sim.readline().decode().strip()
        print("Received:", cmd)
        
        #generating the appropriate response and sending it back
        if cmd == "ON":
            esp_sim.write(b"LED ON\n")
        elif cmd == "OFF":
            esp_sim.write(b"LED OFF\n")
        else:
            esp_sim.write(b"Unknown command\n")
