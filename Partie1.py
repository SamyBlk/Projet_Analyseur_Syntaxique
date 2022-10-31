ver = True
mot_vide = False
mot = input("Donnez le mot: ")
if (mot ==""):
    mot_vide = True         #Cas du mot vide

n = input("Donnez n: ")
n = int(n)      #On converte que le nombre donnée est un entier

#Verification
length = int(len(mot))      #on recupère la taille du mot
i = 0
while (i < length) and (ver):
    if mot[i] == 'a' or mot[i] == 'b' or mot[i] == 'c':     #Le mot doit etre composé de a ou b ou c
        ver = True
    else:
        ver = False
    i += 1

if(ver or mot_vide or mot =="ɛ"):       #Words that belong to the language
    if (mot_vide):
        print("Le mot vide appartient")
    else:    
        print("Le mot ", mot," appartient")
else:
    print("Le mot ", mot, " n'appartient pas à l'alphabet T")

motMirror = ""      #initialise le mot miroir
i = length-1        #initialise i par la taille du mot pour debuter au dernier charactere
motPui = ""         #initialise le mot puissance

while i >= 0 :
    motMirror = motMirror + mot[i]      #Fonction miroir, debuter du fin et reecrie le mot
    i -= 1
if (mot ==""):
    print("Le mot miroir du mot vide est : ɛ")
else:    
    print("Le mot miroir de ", mot, "est : ",motMirror)

#Puissance
if (ver):
    s = 0
    while s < n:
        motPui = motPui + mot
        s += 1
    if (mot_vide):
        print("Le mot puissance du mot vide est: ɛ")            #cas du mot vide
    else:
        print("Le mot puissance de ", mot," est: ",motPui)      #afficher la puissance du mot