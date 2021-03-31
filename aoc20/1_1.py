inputA = [
    1721,
    979,
    366,
    299,
    675,
    1456
]

inputA = [int(x) for x in open('input1_1.txt').read().split()]

def leseEingabeListe(zahlenListeDatei:str):
    result = []
    with open(zahlenListeDatei) as file:
        inputText = file.read()
        zeilenListe = inputText.split()
        
        for zeile in zeilenListe:
            zahl = int(zeile)
            result.append(zahl)

    return result
inputA = leseEingabeListe("input1_1.txt")

[x*y*z for z in inputA for y in inputA for x in inputA if x+y+z==2020][0]
