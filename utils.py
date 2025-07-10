import random
import time

def gerar_sinal(casa):
    confianca = random.randint(90, 99)
    return {
        "entrada": "Aposta em X2",
        "confianca": f"{confianca}%",
        "hora": time.strftime("%H:%M:%S")
    }