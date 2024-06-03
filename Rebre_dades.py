import serial
from datetime import datetime
import funcions_rebre

BAUD_RATE = 9600
# nom_port = '/dev/cu.usbserial-1420' #APC
nom_port = "/dev/cu.usbmodem14101"  # Arduino cable

cansat = serial.Serial(nom_port, BAUD_RATE)

comptador_zeros = 0 #Iniciam un comptador que s'utilitzarà quan el cansat ens envii dades del senor IR. Dins aquest comptador es guardaran els 0 que ens arribin per a després transcriure-ls.

while True:

    lectura = funcions_rebre.rebre_dades(cansat) #La lectura es determina a partir de la funció de rebre_dades, situada al document de funcions_rebre
    print(lectura) #Imprimeix la lectura.
    estat = funcions_rebre.separar_mode(lectura) # L'estat es determina a partir de la funció de separar_mode, situada al document funcins_rebre.
    missatge = funcions_rebre.separar_missatge(lectura) #El missatge es determina a partir de la funció separar_missatge, situada al document funcions_rebre.

    if estat == 3: #Quan l'estat és el nombre 3, s'imprimeixen les dades analitzades a la funció analisis_dades, situada al document funcions.rebre.
        funcions_rebre.analisis_dades(missatge)
    if estat == 4: #Quan l'estat és el 4, s'analitzen les dades del sensor IR a través del següent programa
        if missatge == "0":
            comptador_zeros += 1
            if len(comptador_zeros) >10: #Si el nombre de zeros és major que 10, hi ha hagut un error
                print("\n") 
            elif len(comptador_zeros) <= 4: #si el nombre de zeros és més petit o equivalent a 4 significa que ens envien un ·
                print("·") 
            else: #Si el nombre de zeros és igual o major a 5, en estan enviant una -
                print("-") 
    else:
        funcions_rebre.mostrar_missatge(missatge)
