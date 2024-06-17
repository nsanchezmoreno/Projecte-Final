import serial
from datetime import datetime
import funcions_rebre

BAUD_RATE = 9600
# nom_port = '/dev/cu.usbserial-1420' #APC
nom_port = "/dev/ttyUSB0"  # Arduino cable

cansat = serial.Serial(nom_port, BAUD_RATE)

comptador_zeros = 0 #Comptador de zeros per a l'analisi morse

while True:

    lectura = funcions_rebre.rebre_dades(cansat)   #Determina que la lectura es troba a partir de la funció rebre_dades del fitxer funcions_rebre
    estat = funcions_rebre.separar_mode(lectura)   #Determina que l'estat es troba a partir de la funció separar_mode del fitxer funcions_rebre
    missatge = funcions_rebre.separar_missatge(lectura)   #Determina que el missatge es troba a partir de la funció separar_missatge del fitxer funcions_rebre
    
    if estat == 3: #Quan l'estat és 3 es printen les dades analitzades a la funció analisis_dades del fitxer funcions_rebre
        funcions_rebre.analisis_dades(missatge)
        nom_fitxer = "Dades_Cansat.csv"


        # 'a' significa 'append' i fa que afegim línies a un fitxer sense borrar lo que ja tenim
        with open(nom_fitxer, 'a') as file_object:
                file_object.write(f"{missatge}\n")

    elif estat == 4: #Quan l'estat és 4 es passa a descodificar el codi morse
        while True:
                print(missatge) #Es printa el missatge
                missatge=lectura
                if missatge == "0": #Quan el missatge és un '0' es suma 1 al comptador de zeros
                        comptador_zeros += 1
                else: #Quan el missatge és un '1' la funció es romp
                        break
        
        if comptador_zeros >10: #Si el nombre de zeros és major que 10, fa un bot de línia per a indicar que aquella lletra ja ha acabat
                break
        elif comptador_zeros <= 4 and comptador_zeros >=1: #si el nombre de zeros és més petit o equivalent a 4 significa que ens envien un ·
                print("·") 
        elif comptador_zeros >= 5: #Si el nombre de zeros és igual o major a 5, en estan enviant una -
                print("-") 
    else: #Si és quasevol altre estat només printa el missatge que rep
        funcions_rebre.mostrar_missatge(missatge)
    