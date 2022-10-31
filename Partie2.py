def funcRepFirst(nbr, cst):
 cst = nbr + cst
 cst = cst.replace("0", "a")
 cst = cst.replace("1", "b")     
 return cst

def funcRepLast(nbr, cst):
    cst = cst + nbr
    cst = cst.replace("0", "a")
    cst = cst.replace("1", "b")     
    return cst

def funcRepMi(nbr, cst):
 h=[]
 j = len(nbr)
 bst = cst
 for i in range (j):
    if i> 0:
        cst = nbr[:i] + cst + nbr[i:]
        cst = cst.replace("0", "a")
        cst = cst.replace("1", "b")
        h.append(cst)
        cst = bst
 return h

taille = input("Donnez la largeur: ")
taille  = int(taille)
abbConst = "abb"
TConst = 3
Wor = []
exp = taille - 3
power = pow(2, exp)
power = int(power)
powerBin = bin(power)
powerStr = str(powerBin)
powerStr = powerBin[2::]
lg = len(powerStr)
i = 0     

if taille < 4:
    if taille == 0:
        print("Le mot vide n'appartient pas")
    elif taille == 2 or taille == 1:
        print("Les mots des cette taille n'appartients pas")
    elif taille == TConst:
        print("['abb']")
else:
 while i <= power-1:
  b = bin(i)
  b = str(b)
  b = b[2::]
  j = 0
  while j < lg and len(b)< lg-1:
     b = "0"+b        
     j +=1
  i += 1
  Wor.append(funcRepFirst(b, abbConst))
  Wor.append(funcRepLast(b, abbConst))
  Arr = funcRepMi(b, abbConst)
  for x in Arr:
   Wor.append(x)

 Wor = list(dict.fromkeys(Wor))
 print(Wor)