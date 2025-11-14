def Addition(a,b):
    return a+b

def Soustraction(a,b):
    return a-b

def Multiplication(a,b):
    return a*b

def Division(a,b):
    return a/b

def Reste(a,b):
    return a%b

nbr1=int(input("Entrer un premier nombre : "))
nbr2=int(input("Entrer un deuxième nombre : "))
print ("  Menu")
print ("1-Addition")
print ("2-Soustraction")
print ("3-Multiplication")
print ("4-Division")
print ("5-Reste")
choix=int(input("Faite un choix svp :"))
while choix<1 or choix>5:
    print("Choix invalide!")
    choix=int(input("Faite un choix valide svp :"))
match choix :
    case 1:
        print("L'addition des deux nombres est :"+str(Addition(nbr1,nbr2)))
    case 2:
        print("La soustraction des deux nombres est :"+str(Soustraction(nbr1,nbr2)))
    case 3:
        print ("La multiplication des deux nombres est :"+str(Multiplication(nbr1,nbr2)))
    case 4:
        print ("La division des deux nombres est :"+str(Division(nbr1,nbr2)))
    case 5:
        print ("Le reste des deux nombres est :"+str(Reste(nbr1,nbr2)))
    
