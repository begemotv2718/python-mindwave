import serial
class SerialSocket(serial.Serial):
    def recv(self,n):
        return self.read(n)

def serial_connect():
    socket = SerialSocket('/dev/ttyUSB0',57600)
    return socket, "serial"
