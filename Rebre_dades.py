import serial
from datetime import datetime
import funcions_rebre

BAUD_RATE = 9600
# nom_port = '/dev/cu.usbserial-1420' #APC
nom_port = "/dev/cu.usbmodem14101"  # Arduino cable

cansat = serial.Serial(nom_port, BAUD_RATE)

while True:
    lectura = cansat.readline().decode('Ascii').rstrip("\r\n")
    print (lectura)
    funcions_rebre.separar_mode_lectura(lectura)
    