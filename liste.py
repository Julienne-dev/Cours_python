import easygui
nombre = [1,2,3,4,5]
nbr= easygui.integerbox("Entrer un nombre svp", title="Saisie l'age")
for i in nombre:
    if i==nbr:
       easygui.msgbox(f"Le nombre {nbr} est dans la liste") 
       break
else:
    easygui.msgbox(f"Le nombre {nbr} n'est pas dans la liste", title="Fin de la boucle")

nb = easygui.integerbox("Entrez un entier positif :", lowerbound=1)
i=2
while i*i <= nb:
    if (nb%i) == 0:
        easygui.msgbox(f"Le nombre {nb} n'est pas premier et son premier diviseur est {i}", title="Fin de la boucle")
        break
    i+=1
else:
    easygui.msgbox(f"Le nombre {nb} est premier", title="Fin de la boucle")   