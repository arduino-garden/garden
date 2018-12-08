import serial
import sys

ser = serial.Serial('/dev/ttyACM0',9600)
s = [0]

while True:
		read_serial=ser.readline()
	
		#split -> json 
	
		#print read_serial
	
		#write to file with utc timestamp
		if read_serial:
			file.write(read_serial)
			break
