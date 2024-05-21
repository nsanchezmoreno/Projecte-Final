def separar_mode_lectura(lectura):
    estat = lectura.split("#") [0]
def separar_dades_lectura(lectura):
    dades = lectura.split("#") [1]

def dades_lectura():
    dades_separades = dades.split(",") 
    dada1 = int(dades_separades[0]) #nombre de paquet
    dada2 = dades_separades[1] #nom del cansat
    dada3 = int(dades_separades[2]) #temperatura del termistor
    dada4 = int(dades_separades[3]) #pressió BMP280
    dada5 = int(dades_separades[4]) #temperatura BMP280
   #afegir més dades si són necessàries

    print(f"Dada 1: {dada1}")
    print(f"Dada 2: {dada2}")
    print(f"Dada 3: {dada3}")
    print(f"Dada 4: {dada4}")
    print(f"Dada 5: {dada5}")
    
