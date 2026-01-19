<<<<<<< HEAD
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
=======
Symbols = ["+","-","*","/","//","%","²","√"]
History=[]
try:
    with open("historique.txt", "r", encoding="utf-8") as f:
        History = f.read().splitlines()
except FileNotFoundError:
    pass


# Delete History
def clearhistory():
    History.clear()
    with open("historique.txt", "w", encoding="utf-8"):
        pass
    print("History deleted")


# All supported calculations
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

# Call calculations in priority order
def prioritycalculation(Intlist,Symblist):
    i = 0
    while not i == len(Symblist):
        if Symblist[i] == "²":
            Intlist[i] = currentsquare(Intlist[i])
            Symblist.pop(i)
        elif Symblist[i] == "√":
            Intlist[i] = currentsquareroot(Intlist[i])
            Symblist.pop(i)
        else:
            i += 1
    i = 0

    while not i == len(Symblist):
        if Symblist[i] == "*":
            Intlist[i] = currenttime(Intlist[i],Intlist[i+1])
            Intlist.pop(i+1)
            Symblist.pop(i)
        elif Symblist[i] == "/":
            Intlist[i] = currentdiv(Intlist[i],Intlist[i+1])
            Intlist.pop(i+1)
            Symblist.pop(i)
        elif Symblist[i] == "//":
            Intlist[i] = currentwholediv(Intlist[i],Intlist[i+1])
            Intlist.pop(i+1)
            Symblist.pop(i)
        elif Symblist[i] == "%":
            Intlist[i] = currentremainder(Intlist[i],Intlist[i+1])
            Intlist.pop(i+1)
            Symblist.pop(i)
        else:
            i += 1
    i = 0

    while not i == len(Symblist):
        if Symblist[i] == "+":
            Intlist[i] = currentadd(Intlist[i],Intlist[i+1])
            Intlist.pop(i+1)
            Symblist.pop(i)
        elif Symblist[i] == "-":
            Intlist[i] = currentsub(Intlist[i],Intlist[i+1])
            Intlist.pop(i+1)
            Symblist.pop(i)
        else:
            i += 1
    return Intlist[0]


# Declare error and type
def errormessage(Cause):
    print("Error")
    if Cause == "Char":
        print("Put a valid value")
    elif Cause == "Cal":
        print("Put a valid calculation")


# Check the nature of each character
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


# Check for forbidden calculations
def testvalidcalculation(Character,NextCharacter):
    if Character == "/":
        if NextCharacter == "0":
            errormessage("Cal")
            return False
    else:
        return True


# Sort all characters into lists and layer of calculations
def sortinginput(Calculation):
    Calculation += ")"
    CurrentInput = "0"
    Intlist = []
    Symblist = []
    i = 0

    while not i == len(Calculation)-1:
        Inputtype = testinputtype(Calculation[i])
        if Inputtype == False:
            break
        elif testvalidcalculation(Calculation[i],Calculation[i+1]) == False:
            Inputtype = False
            break
        elif Inputtype == "Integer":
            CurrentInput = CurrentInput + Calculation[i]
            if not testinputtype(Calculation[i+1]) == "Integer":
                Intlist = Intlist + [int(CurrentInput)]
                CurrentInput = ""
        elif Inputtype == "Symbol":
            CurrentInput = CurrentInput + Calculation[i]
            if not testinputtype(Calculation[i+1]) == "Symbol":
                Symblist = Symblist + [Calculation[i]]
                CurrentInput = ""
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
        return [Intlist,Symblist,i]


# Main calculator branch
def calculator(Calculation):
    Calculationdata = sortinginput(Calculation)
    if Calculationdata == False:
        return False
    else:
        Result = [prioritycalculation(Calculationdata[0],Calculationdata[1]),Calculationdata[2]]
        return Result


# History Menu
def historymenu():
    print(History)    
    print("Delete History : 1")
    print("Go back to Menu : 2")
    Choice = input("Choose between the 2 choices : ")
        
    if Choice == "1":
        clearhistory()
        historymenu()

    if Choice == "2":
        calculatormenu()


# Calculator menu
def calculatormenu(): 
    print("Make your calculation : 1")
    print("Show history : 2")
    Choice = input("Choose between the 2 choices : ")
    
    if Choice == "1":
        Calculation = input("Enter your calculation : ")
        Result = calculator(Calculation)
        if Result == False:
            Result = "Error"
        else:
            Result = Result[0]
        FullCalculation = f"{Calculation} = {Result}"
        print(FullCalculation)
        History.append(FullCalculation)
        with open("historique.txt", "a", encoding="utf-8") as f:
            f.write(f"{Calculation} = {Result}\n")
            calculatormenu()
                
    elif Choice == "2":
        historymenu()
        

    


calculatormenu()
>>>>>>> Test
