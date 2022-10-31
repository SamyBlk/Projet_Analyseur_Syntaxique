Word = input("Donnez le mot: ")
ver = True
i=0
j=0
while i < len(Word) and ver:
    if(Word[i] != "a" and Word[i] != "b"):
        ver = False
    i += 1
i = 0
lastB = 0
firstB = 0
LB = True
FB = True
leng = len(Word)-1
while i < leng and LB:
    s = leng - i
    if Word[i] == "b":
        lastB = s
        LB = False
    i += 1
i = 0
while i < leng and FB:
    if Word[i] == "b":
        firstB = i
        FB = False
    i +=1
i = firstB-1
cptB = 0
while i<leng:
    if Word[i] == "b":
        cptB += 1
    i += 1
i=0
cptA = 0
while i <firstB:
    if Word[i] == "a":
        cptA += 1
    i += 1
        
if cptA < (cptB*2):
    ver = False      

if (ver):
    if(Word == ""):
        print("Le mot vide appartient au langage")
    elif(Word == "a" or Word =="aab" or Word=="aaab"):
        print ("Le mot ", Word, " appartient au langage")
    else:
        print("Le mot appartient au langage")
else:
    print("Le mot n'appartient pas au langage")