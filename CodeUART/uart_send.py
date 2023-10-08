import time
import  serial

sport = serial.Serial(
    port = '/dev/ttyAMA0',
	baudrate = 115200,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1
    )
print("Raspberry's sending : ")
 
try:
    while True:
    	sport.write(b'hehe')
    	sport.flush()
    	print("hehe")
    	time.sleep(1)
except KeyboardInterrupt:
	sport.close()