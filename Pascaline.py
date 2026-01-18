Symbols = ["+","-","*","/","%","²","√"]

#Effectue les calculs individuellement
def currentadd(Value1,Value2):
    return Value1 + Value2
def currentsub(Value1,Value2):
    return Value1 - Value2
def currenttime(Value1,Value2):
    return Value1 * Value2
def currentsquare(Value):
    return Value * Value
def currentdiv(Value1,Value2):
    return Value1 / Value2
def currentwholediv(Value1,Value2):
    return Value1 // Value2
def currentremainder(Value1,Value2):
    return Value1 % Value2
def currentsquareroot(Value):
    return int(Value ** 0.5)

#Effectue les calculs dans l'ordre
def prioritycalculation(list,symb):
    print(list,symb)
    i = 0
    print(i)
    while not i == len(symb):
        if symb[i] == "²":
            list[i] = currentsquare(list[i])
            symb.pop(i)
        elif symb[i] == "√":
            list[i] = currentsquareroot(list[i])
            symb.pop(i)
        else:
            i += 1
        print(list,symb)
        print(i)
    i = 0
    while not i == len(symb):
        if symb[i] == "*":
            list[i] = currenttime(list[i],list[i+1])
            list.pop(i+1)
            symb.pop(i)
        elif symb[i] == "/":
            if symb[i+1] == "/":
                list[i] = currentwholediv(list[i],list[i+1])
                list.pop(i+1)
                symb.pop(i)
                symb.pop(i)
            else:
                list[i] = currentdiv(list[i],list[i+1])
                list.pop(i+1)
                symb.pop(i)
        elif symb[i] == "%":
            list[i] = currentremainder(list[i],list[i+1])
            list.pop(i+1)
            symb.pop(i)
        else:
            i += 1
        print(list,symb)
        print(i)
    i = 0
    while not i == len(symb):
        print(i)
        if symb[i] == "+":
            list[i] = currentadd(list[i],list[i+1])
            list.pop(i+1)
            symb.pop(i)
        elif symb[i] == "-":
            list[i] = currentsub(list[i],list[i+1])
            list.pop(i+1)
            symb.pop(i)
        else:
            i += 1
        print(list,symb)
        print(i)
    return list[0]

# Annonce le type d'erreur de la part de l'utilisateur
def errormessage(cause):
    if cause == "Char":
        print("Mettre une valeur valide")
    elif cause == "Cal":
        print("Mettre un calcule valide")


#Vérifie si le caractère est valide entre chiffres, symboles et parenthèses
def testinputtype(Character):
    Validinput = False
    if Character in Symbols:
        Validinput = "Symbol"
    elif Character == "(":
        Validinput = "OpenParenthesis"
    elif Character == ")":
        Validinput = "CloseParenthesis"
    elif Character.isdigit():
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
def sortinginput(Calculation):
    Calculation += ")"
    Currentnumber = "0"
    Intlist = []
    Symblist = []
    i = 0
    while not i == len(Calculation)-1:
        Inputtype = testinputtype(Calculation[i])
        if Inputtype == False or testvalidcalculation(Calculation[i],Calculation[i+1]) == False:
            Inputtype = False
            break
        elif Inputtype == "Integer":
            Currentnumber = Currentnumber + Calculation[i]
            if not testinputtype(Calculation[i+1]) == "Integer":
                Intlist = Intlist + [int(Currentnumber)]
                Currentnumber = ""
        elif Inputtype == "Symbol":
            Symblist = Symblist + [Calculation[i]]
        elif Inputtype == "OpenParenthesis":
            parentcal = calculator(Calculation[i+1:])
            Intlist = Intlist + [parentcal[0]]
            i += parentcal[1]
        i += 1
        if Inputtype == "CloseParenthesis":
            break
    if Inputtype == False:
        return False
    else:
        return [prioritycalculation(Intlist,Symblist),i]


#Vérifie la priorité actuelle
def testpriority(Symblist):
    AddSub = []
    TimeDiv = []
    for i in range(len(Symblist)):
        if Symblist[i] == "+" or Symblist[i] == "-":
            AddSub += [i]
        elif Symblist[i] == "*" or Symblist[i] == "/":
            TimeDiv += [i]
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
def calculator(Calculation):
    result = sortinginput(Calculation)
    if result == False:
        return ""
    else:
       return result

#Appelle la calculatrice pour ne rendre que le résultat
def callcalculator(Calculation):
    print(Calculation,'=',sortinginput(Calculation)[0])

callcalculator("(13+3²)*432%(351-√4)")