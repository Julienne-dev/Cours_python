def table (base,debut,fin,inc):
    i=debut
    for i in range(debut,fin,inc):
        print(base,"*",i,"=",base*i)
        i+=1

table(2,1,11,1)
table(5,1,11,1)
table(3,1,11,1)
table(4,1,11,1)