#This script simulating live temperature readings by sending data that keeps on increasing to COM8 and serial_reader
#this data on COM7.

#importing necessary libraries
import serial
import time

#setting up the serial port to send data
ser = serial.Serial('COM8', 9600)

#initial temperature reading
counter = 0.1

#The temperature is written on COM8 in binary format and the temperature keeps on increasing by 1 every 2 seconds
while True:
    value = f"{counter}\n"
    ser.write(value.encode())
    #log
    print(f"Sent: {counter}")
    counter += 1
    time.sleep(2)
    
