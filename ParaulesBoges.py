"""
Helena Herrera Aviles
22/2/2024
"""
import random
#region declarar funcions
def text_correcte():
    # Demanar un text
    text = input("Introdueix un text: ")
    return text

def paraula_desordenada(paraula):
    # Desordenar les lletres d'una paraula
    lletres = list(paraula)
    return ''.join(lletres)

def mantenir_extrems(paraula):
    # Mantenir els extrems de la paraula i desordenar el mig
    if len(paraula) <= 2:
        return paraula
    primera = paraula[0]
    ultima = paraula[-1]
    mig = list(paraula[1:-1])
    random.shuffle(mig)
    return primera + ''.join(mig) + ultima

def escriure_desordenat(text):
    # Escriure el text desordenat
    paraules = text.split()
    frase_desordenada = ' '.join(mantenir_extrems(paraula_desordenada(paraula)) for paraula in paraules)
    print(frase_desordenada)

def resultat():
    # Programa principal
    text = text_correcte()
    escriure_desordenat(text)

#endregion

#region mainprogram
try:
    resultat()
except:
    print("Error en el programa")
#endregion

