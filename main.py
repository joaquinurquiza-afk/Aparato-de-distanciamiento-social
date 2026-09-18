from estado import state_determinator
from sensor import sensor
from rgb import led_color
from buzzer import sound_buzzer
from sistema import sistem
import random
import time

#Algoritmo Principal - Menu


distd = 300

print("=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_")
print("    MODO DEL SENSOR")
print("____________________________________")

mode = int(input("0 - Automatico\n\n1 - Manual  "))
print("")
print("=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_")
print("    ACTIVAR HISTERISIS")
print("____________________________________")

hist = int(input("0 - Activada\n\n1 - Desactivada  "))
print("")
print("=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_")
print("    SENSOR DE DISTANCIAMIENTO")
print("  por defecto: DANGER = 300mm")
print("____________________________________")

ch = int(input("0 - INICIAR  \n\n1 - CALIBRAR  "))  

if ch == 1:
        
        distd = 100
        print("")
        print("*************************************")
        print("A cuantos milimetros entra en DANGER")
        print()
        print("0 - Agregar 100mm \n\n1 - Terminar")
        print("*************************************")
         
        while True: 
            print("=_=_=_=_=_=_=_=_=_=_=_=")
            print(f"Distancia de DANGER: {distd}mm")
            ch2 = int(input("(0 - 1) : "))
            
            if ch2 == 0:
                distd = distd + 100
            else:
                break

else:
    None
    
dist = distd + 1200 # Distancia de inicio
sujeto = "safe" #Estado inicial del suejto (para la histerisis)

while True: #Inicio del bucle
    
    #Determina el nuevo estado del sujeto y sus indicadores
    
    sujeto = state_determinator(hist, dist, distd, sujeto)
    color = led_color(sujeto)
    buz = sound_buzzer(sujeto)
    
    fin_bucle = sistem(sujeto) #Sistema para cuando la distanacia es 0
    
    if fin_bucle:
        print("Te moriste :(")
        break
    #Activa los indicadores: en este caso solo lo muestra en la pantalla
    print("=================================")
    print(f"Distancia {dist}, Estado {sujeto.upper()}\n\nLED {color}, Sonido {buz.upper()}")
    
    dist = sensor(mode, sujeto, dist) #Nueva distancia

    time.sleep(0.5) #Toma valores cada 0.5 segundos(500ms)
