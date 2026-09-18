#Funcion para determinar estados

def state_determinator (hist, dist, distd, sujeto):
    
    distw = distd + 500
    his = 50
    
    if hist == 1:  # histerisis apagada
        if dist <= distd and dist > 0:
            return "danger"
        elif dist <= distw and dist > distd:
            return "warning"
        elif dist > distw:
            return "safe"
        else:
            return "dead"
    
    else: # HIsterisis activada
        if sujeto == "danger":  #Comprueba estado actual del sujeto
            if dist <= 0:
                return "dead"
            
            elif dist > distd + his: #Si esta en danger, para volver a warning debe
                return "warning"     #superar el umbrarl de peligro mas histerisis

            else:
                return "danger"
        elif sujeto == "warning":
            if dist <= distd - his: #SI esta en warning, para ir a danger debe
                return "danger"     #decender hasta el umbral de peligro menos histerisis
   
            elif dist >= distw + his:
                return "safe"
         
            else:
                return "warning"
        elif sujeto == "safe":
            if dist <= distw - his:
                return "warning"
         
            else:
                return "safe"
