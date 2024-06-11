import math
def separar_mode(lectura): #Funció per a separar el mode
    estat = int(lectura.split("/") [0]) #Amb la funció ".split" separam l'estat, i amb la funció "int" passam el nombre de text a enter
    return estat
    
def separar_missatge(lectura): #Funció per a separar el missatge 
    dades = lectura.split("/") [1] #Amb la funció ".split" separam les dades de l'estat
    return dades

def crear_array(dades): #Funció per a crear una llista
    dades_separades = dades.split(',') #Separa les dades amb comes
    return dades_separades

def extreu_num_paquet(dades_separades): #Funció per a extreure el número de paquet de les dades
    num_paquet = int(dades_separades[0]) #Extreu el nombre de paquet de la llista creada anteriorment, aquesta dada es troba al primer lloc i la transformam en un enter
    return num_paquet 

def extreu_nom_cansat(dades_separades): #Funció per a extreure el nom del cansat de les dades
    nom_cansat= dades_separades[1] #Extreu el nom del cansat de la llista creada anteriorment, aquesta dada es troba al segon lloc 
    return nom_cansat
    
def temperatura(dades_separades): #Funció per a extreure la temperatura del termistor 
    temperatura= int(dades_separades[2]) #Extreu la temperatura del termistor de la llista creada anteriorment, aquesta dada es troba al tercer lloc i la transformam en un enter
    return temperatura

def pressio(dades_separades): #Funció per a extreure la pressió del BMP280
    pressio= float(dades_separades[3]) #Extreu la pressió del BMP280 de la llista creada anteriorment, aquesta dada es troba al quart lloc i la transformam en un decimal
    return pressio
    
def temperatura_BMP(dades_separades): #Funció per a extreure la temperatura del BMP280
    temperatura_BMP = float(dades_separades[4]) #Extreu la temperatura del BMP280 de la llista creada anteriorment, aquesta dada es troba al cinquè lloc i la transformam en un decimal
    return temperatura_BMP
    

def mostrar_missatge(missatge): #Funció que mostra el missatge
    print(missatge)

def analisis_dades(missatge): #Funció que analitza les dades
    dades_separades=crear_array(missatge) #Les dades separades fan referència a la llista creada anteriorment
    num_paquet = extreu_num_paquet(dades_separades) #El númeru de paquet fa referència a la funció que extreu el número de paquet
    nom_cansat = extreu_nom_cansat(dades_separades)  #El nom del cansat fa referència a la funció que extreu el nom del cansat
    temp = temperatura(dades_separades) #Temp fa referència a la funció que extreu la temeratura
    pressio_BMP = pressio(dades_separades) #Pressio_BMP fa referència a la funció que extreu la pressió
    temp_BMP = temperatura_BMP(dades_separades) #temp_BMP fa referència a la funció que extreu la temeratura del BMP280
    #Calcular temperatura a partir de la lectura del termistor
    r_aux = 10 #kilohms

    vol_ter = (5*temp)/1023 #Calcula els volts del termistor

    r_ter = (vol_ter*r_aux)/(5-vol_ter) #Calcula la resistència del termistor a partir dels volts

    t = round(73.74 - 21.06*math.log(r_ter),3) #Calcula la temperatura real en ºC

    #posar-ho polit
    print(f"Número de paquet: {num_paquet}")
    print(f"Nom del cansat: {nom_cansat}")
    print(f"La temperatura del termistor és de {t}ºC")
    print(f"La pressió és de {pressio_BMP} Pa")
    print(f"La temperatura del BMP és de {temp_BMP}ºC")
    


def rebre_dades(cansat):
    lectura= cansat.readline().decode('Ascii').rstrip("\r\n")
    return lectura