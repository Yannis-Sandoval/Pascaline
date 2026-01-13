Symbols = ["+","-","*","/","(",")"]


#Vérifie si le caractère est valide entre chiffres, symboles et parenthèses
def testvalidinput(Character):
    Validinput = False
    if Character in Symbols:
        Validinput = "Symbol"
    else:
        try:
            Character = int(Character)
            Validinput = "Integer"
        except:
            print("Erreur")
            print("Veuillez entrer des caractères valides")
    return Validinput

# Vérifie si les calculs sont authorités
def testvalidcalculation(Character,NextCharacter):
    if Character == "/":
        if NextCharacter == "0":
            print("Erreur")
            print("Chiffre non valide")
            return False
    else:
        return True


#Vérifie le type de caractère entre chiffres, symboles et parenthèses
def testinputtype(Calculation):
    Currentnumber = ""
    Intlist = ""
    Symblist = ""
    for i in range(len(Calculation)):
        Inputtype = testvalidinput(Calculation[i])
        if Inputtype == "Integer":
            Currentnumber = Currentnumber + Inputtype
        elif Inputtype == "Symbol":
            Symblist = Symblist + [Inputtype]
            if testvalidinput(Calculation[i-1]) == "Integer":
                Intlist = Intlist + [int(Currentnumber)]
                Currentnumber = ""


#Vérifie la priorité actuelle
def testpriority():



#Effectue le calcul à la plus haute priorité
def currentcalculation(Value1,Symbols,Value2):

    if Symbols == "+":
        Result = Value1 + Value2
    elif Symbols == "-":
        Result = Value1 - Value2
    elif Symbols == "*":
        Result = Value1 * Value2
    elif Symbols == "/":
        Result = Value1 / Value2
    return Result
    

#Branche principale de la calculette
def calculator(calcule):
    
    

calculator(input("Entrer le calcul"))