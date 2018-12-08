import serial
import sys

ser = serial.Serial('/dev/ttyACM0', 9600)
s = [0]

while True:
    read_serial = ser.readline()

    # write to file with utc timestamp
    if read_serial:
        entries = read_serial.split()
        print(str(entries[0]))
        break
