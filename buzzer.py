#Sonido del buzzer.

def sound_buzzer(sujeto):
    if sujeto == "danger":
        return "bip bip bip"  #Al estar en peligro, activa la alarma por un segundo
        
    else:
        return "apagado" #De lo contrario, lo apaga 
