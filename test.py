import serial
from serial.tools import list_ports
import time
if __name__ == "__main__":
    for i in list_ports.comports():
        print(i)
    arduino = serial.Serial('COM5',9600,timeout = 1)
    time.sleep(2)
    arduino.write(bytes("2.0",'utf-8'))
    time.sleep(1)  # import time  # import time
    arduino.write(b'0')