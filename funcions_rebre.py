import math
def separar_mode(lectura):
    estat = lectura.split("/") [0]
    return estat
    
def separar_missatge(lectura):
    dades = lectura.split("/") [1]
    return dades

def crear_array(dades):
    dades_separades = dades.split(',')
    return dades_separades

def num_paquet(dades_separades):
    num_paquet = int(dades_separades[0]) #nombre de paquet
    return num_paquet 

def nom_cansat(dades_separades):
    nom_cansat= dades_separades[1] #nom del cansat
    return nom_cansat
    
def temperatura(dades_separades):
    temperatura= int(dades_separades[2]) #temperatura del termistor
    return temperatura

def pressio(dades_separades):
    pressio= int(dades_separades[3]) #pressió BMP280
    return pressio
    
def temperatura_BMP(dades_separades):
    temperatura_BMP = int(dades_separades[4]) #temperatura BMP280
    return temperatura_BMP
    

def mostrar_missatge(missatge):
    print(missatge)

def analisis_dades(missatge):
    dades_separades=crear_array(missatge)
    num_paquet = num_paquet(dades_separades)
    nom_cansat = nom_cansat(dades_separades)
    temperatura = temperatura(dades_separades)
    pressio = pressio(dades_separades)
    temperatura_BMP = temperatura_BMP(dades_separades)
    #Calcular temperatura a partir de la lectura del termistor
    r_aux = 10 #kilohms

    vol_ter = (5*temperatura)/1023 #Calcula els volts del termistor

    r_ter = (vol_ter*r_aux)/(5-vol_ter) #Calcula la resistència del termistor a partir dels volts

    t = round(73.74 - 21.06*math.log(r_ter),3) #Calcula la temperatura real en ºC

    #test
    print(f"Número de paquet: {num_paquet}")
    print(f"Nom del cansat: {nom_cansat}")
    print(f"La temperatura del termistor és de {t}ºC")
    print(f"La pressió és de {pressio} Pa")
    print(f"La temperatura del BMP és de {temperatura_BMP}ºC")


def rebre_dades(cansat):
    lectura= cansat.readline().decode('Ascii').rstrip("\r\n")
    return lectura