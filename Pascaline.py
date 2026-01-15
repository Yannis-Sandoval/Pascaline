Symbols = ["+","-","*","/"]

# Annonce le type d'erreur de la part de l'utilisateur
def errormessage(cause):
    if cause == 

#Vérifie si le caractère est valide entre chiffres, symboles et parenthèses
def testvalidinput(Character):
    Validinput = False
    if Character in Symbols:
        Validinput = "Symbol"
    if Character == "(":
        Validinput = "OpenParenthesis"
    if Character == ")":
        Validinput = "CloseParenthesis"
    elif isinstance(Character,int):
        Validinput = "Integer"
    else:
        errormessage("Char")
    return Validinput

# Vérifie si les calculs sont authorités
def testvalidcalculation(Character,NextCharacter):
    if Character == "/":
        if NextCharacter == "0":
            errormessage("Cal")
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
        if testvalidcalculation(Calculation[i],Calculation[i+1]) or Inputtype == False:
            Inputtype = False
            break
        elif Inputtype == "Integer":
            Currentnumber = Currentnumber + int(Inputtype)
        elif Inputtype == "Symbol":
            Symblist = Symblist + [Inputtype]
            if testvalidinput(Calculation[i-1]) == "Integer":
                Intlist = Intlist + [int(Currentnumber)]
                Currentnumber = ""
        elif Inputtype == "OpenParenthesis":
            Intlist = Intlist + [calculator(Calculation[i+1:])]
        elif Inputtype == "CloseParenthesis":
            break
    if Inputtype == False:
        return False


#Vérifie la priorité actuelle
def testpriority(Symblist):
    AddSub = ""
    TimeDiv = ""
    for i in range(Symblist):
        if Symblist[i] == "+" or "-":
            AddSub += i
        elif Symblist[i] == "*" or "/":
            TimeDiv += i
    Order = TimeDiv + AddSub
    return Order

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
    result = testinputtype(calcule)
    if result == False:
        return ""
    

calculator(input("Entrer le calcul"))