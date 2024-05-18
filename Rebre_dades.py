import serial
from datetime import datetime

BAUD_RATE = 9600
# nom_port = '/dev/cu.usbserial-1420' #APC
nom_port = "/dev/cu.usbmodem14101"  # Arduino cable

cansat = serial.Serial(nom_port, BAUD_RATE)

while True:
    lectura = cansat.readline().decode('Ascii').rstrip("\r\n")
    
    estat = lectura.split('#') #Separa l'estat del cansat i les dades que ens envia 
    print(estat)
    mode = estat[0]
    if mode==0 :
        print("El cansat està en repòs")
    elif mode==1 :
        print("El cansat està connectat")
    elif mode==2 : 
        print("El cansat s'està localitzant")
    elif mode==3 : 
        print("dades cansat") #afegir les dades de la lectura
    
#Així podem accedir a cada valor i guardar-lo en una variable
dada1 = dades[0]
dada2 = int(dades[1]) # Les dades són un text, per tant, s'han de convertir al tipus que volem
dada3 = dades[2]
dada4 = float(dades[3]) 
dada5 = dades[4]

print(f"Dada 1: {dada1}")
print(f"Dada 2: {dada2}")
print(f"Dada 3: {dada3}")
print(f"Dada 4: {dada4}")
print(f"Dada 5: {dada5}")
    print(lectura)
