#Sistema para determinar distancia
import random

def sensor(mode, sujeto, dist):
    
    if mode == 0:  # Se activa el modo automatico del sensor
        
        #Segun el estado del sujeto, se determina la posibilidad de volver un paso  
        
        if sujeto == "safe":
            p = 30
        elif sujeto == "warning":
            p = 10
        else:
            p = 3   #Mietras mas cerca este, mayor sera la posibilidad de volver 
            
        s = random.randint(1,p)   #Dejo el que avance o retroceda a la suerte:
        if s == p:                
                return dist + 50 #Posibilidad de volver = 1/p
        else:
                return dist - 50
    else:
        dist = int(input("Distancia: ")) #Modo manual del sensor
        return dist
