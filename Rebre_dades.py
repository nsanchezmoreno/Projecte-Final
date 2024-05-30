import serial
from datetime import datetime
import funcions_rebre

BAUD_RATE = 9600
# nom_port = '/dev/cu.usbserial-1420' #APC
nom_port = "/dev/cu.usbmodem14101"  # Arduino cable

cansat = serial.Serial(nom_port, BAUD_RATE)

comptador_zeros = 0

while True:

    lectura = funcions_rebre.rebre_dades(cansat)
    print(lectura)
    estat = funcions_rebre.separar_mode(lectura)
    missatge = funcions_rebre.separar_missatge(lectura)

    if estat == 3:
        funcions_rebre.analisis_dades(missatge)
    if estat == 4:
        if missatge == "0":
            comptador_zeros += 1
    # escriure quants de uns són un punt i una retxa
    #intentar passar de codi morse a lletres
    else:
        funcions_rebre.mostrar_missatge(missatge)
