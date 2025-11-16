base=int(input("Veillez indiquer le nombre dont vous voulez la table de multiplication :"))
debut=int(input("Par quel nombre doit commencer la table de multiplication ? :"))
fin=int(input("Par quel nombre doit terminer la table de multiplication ? :"))
inc=int(input("Vous voulez par bond de combien ? :"))
def table (base,debut,fin,inc):
    i=debut
    for i in range(debut,fin,inc):
        print(base,"*",i,"=",base*i)
        i+=1

table(base,debut,fin,inc)
