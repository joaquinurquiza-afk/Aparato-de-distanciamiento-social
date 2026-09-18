#Color que toma el LED

def led_color(sujeto):
    if sujeto == "safe": #Comprueba el estado el sujeto
        return "verde" #Devuelve un color
    elif sujeto == "warning":
        return "amarillo"
    else:
        return "rojo"
       
