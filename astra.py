def remplir():
    dist=open("distance.txt","w")
    i=65
    d=0
    while i<74:
        for c in range(9-d):
            a=(chr(i)+","+chr(i+c+1))+"= "
            dis=input(a)
            dis=a+dis
            dist.write(dis)
        i=i+1
        d=d+1
    dist.close()

def remplirc():
    N=input("combien de chemin")
    L=[str()*N]
    vd=input("enrer le vie de depart")
    va=input("enrer le vie de arrive")
    dd=open("chemin.dat","wb")
    for i in range(N-1):
        
        chem=input("enrer le chemin")
        while(chem[1]!=vd)and(chem[-1]!=va):
            chem=input("enrer le chemin correcte!!!")
        
        distt=dist(chem)
        Dict = {"Chemin": chem, "Distance": distt}
        pickle.dump(Dict,dd)
    dd.close()

def dist(ch):
    dist=open("distance.txt","r")
    L=dist.read()
    s=0
    for i in range(len(ch)-1):
        ch1=ch[i:i+1]
        for j in range(len(L)):
            if (ch1[0] in L[i]) and (ch1[1] in L[i]):
                s=s+L[i][-1]
    dist.close()
    return s

def tri(t): 
    for i in range(1, len(tab)): 
        k=tab[i] 
        j=i-1
        while j>=0 and k<tab[j] : 
                tab[j+1]=tab[j] 
                j=j-1
        tab[j+1]=k


def affichage():
    dd=open("chemin.dat","rb")
    L=pickle.load(dd)
    tri(L)
    print("Les meilleur chemins sont:")
    for i in range(1,3):
        print(L[-i])

    
            
        
        
        
        
    

