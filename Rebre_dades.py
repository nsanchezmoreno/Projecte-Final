import serial
from datetime import datetime
import funcions_rebre

BAUD_RATE = 9600
# nom_port = '/dev/cu.usbserial-1420' #APC
nom_port = "/dev/ttyUSB0"  # Arduino cable

cansat = serial.Serial(nom_port, BAUD_RATE)

comptador_zeros = 0

while True:

    lectura = funcions_rebre.rebre_dades(cansat)
    #print(lectura)
    
    estat = funcions_rebre.separar_mode(lectura)
    missatge = funcions_rebre.separar_missatge(lectura)
    if estat ==0:
        print(lectura)
    elif estat ==1:
        print(lectura)
    elif estat == 2:
        print(lectura)
    elif estat == 3:
        print(funcions_rebre.analisis_dades(missatge))
    elif estat == 4:
        contador_zeros=""
        misatge=""
        while len(misatge)<4:
            while True:
                misatge=lectura
                if missatge == "0":
                    comptador_zeros += misatge
                else:
                    break
            if len(comptador_zeros) >10: #Si el nombre de zeros és major que 10, fa un bot de línia per a indicar que aquella lletra ja ha acabat
                break
            elif len(comptador_zeros) <= 4: #si el nombre de zeros és més petit o equivalent a 4 significa que ens envien un ·
                print("·") 
            else: #Si el nombre de zeros és igual o major a 5, en estan enviant una -
                print("-") 
    else:
        funcions_rebre.mostrar_missatge(missatge)
    