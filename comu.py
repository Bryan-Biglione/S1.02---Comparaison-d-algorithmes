reseau = {
        "Alice" : ["Bob", "Dan"],
        "Bob" : ["Alice", "Carl", "Dan"],
        "Carl" : ["Bob"],
        "Dan" : ["Alice", "Bob"]
       } 

amis = ["Alice", "Bob", "Alice", "Dan", "Bob", "Carl", "Bob", "Dan"]

#Question 1 

#Définition de la fonction     
def cree_reseau(amis):                 
    '''
    Génère un dictionnaire représentant un réseau d'amis à partir d'une liste donnée.

    Chaque élément de la liste représente une paire d'amis. La fonction retourne un 
    dictionnaire où chaque clé est le prénom d'une personne, et la valeur associée 
    est une liste des prénoms de ses amis.

    Paramètres :
    amis (list) : Liste contenant des paires d'amis sous forme [prenom1, ami1, prenom2, ami2, ...].

    Retourne :
    dict : Un dictionnaire où les clés sont des prénoms et les valeurs sont des listes des amis.
    '''
    i = 0                                   
    #dictionnaire vide qu'on va remplir
    dico_amis = {}                          
    
    while i < len(amis):                    
        #deux variable qui on pour but de fonctionner par paire
        prenom = amis[i]                      
        ami = amis [i + 1]

        if prenom not in dico_amis:
            dico_amis[prenom] = []           
        dico_amis[prenom].append(ami) 

        if ami not in dico_amis: 
            dico_amis[ami]= [] 
        dico_amis[ami].append(prenom)
        
        #On incrémente de 2 car notre tableau "amis" prit en paramètre fonctionne par paire
        i += 2                              
    
    return dico_amis                         


#Question 3

def liste_personnes(dico):
    '''
    Renvoie la liste des personnes présentes dans un réseau d'amis.

    Cette fonction extrait les clés du dictionnaire représentant le réseau d'amis,
    où chaque clé correspond à une personne.

    Paramètres :
    dico (dict) : Dictionnaire où les clés sont des prénoms et les valeurs sont des listes d'amis.

    Retourne :
    list : Liste des prénoms des personnes dans le réseau.
    '''
    #liste_amis contient toutes les personnes du reseau 
    liste_amis = list(dico.keys())

    return liste_amis


#Question 4

def sont_amis(reseau, personne1, personne2):
    '''
    Vérifie si deux personnes sont amies dans un réseau.

    La fonction détermine si 'personne1' et 'personne2' figurent dans les listes 
    d'amis l'une de l'autre dans le dictionnaire du réseau.

    Paramètres :
    reseau (dict) : Dictionnaire où les clés sont des prénoms et les valeurs sont des listes d'amis.
    personne1 (str) : Le prénom de la première personne.
    personne2 (str) : Le prénom de la deuxième personne.

    Retourne :
    bool : True si les deux personnes sont amies, False sinon.
    '''
    #vérification pour savoir si les deux personnes sont dans le reseau et amis l'un avec l'autre
    if personne1 in reseau and personne2 in reseau[personne1]:
        return True
    if personne2 in reseau and personne1 in reseau[personne2]:
        return True
    else:
        return False


#Question 5

def sont_amis_de(personne1, groupe, reseau):
    '''
    Vérifie si une personne est amie avec tous les membres d'un groupe.

    La fonction parcourt la liste des membres du groupe et utilise la fonction 'sont_amis'
    pour vérifier si 'personne1' est amie avec chaque membre.

    Paramètres :
    personne1 (str) : Le prénom de la personne à vérifier.
    groupe (list) : Liste des prénoms des personnes dans le groupe.

    Retourne :
    bool : True si 'personne1' est amie avec tous les membres du groupe, False sinon.
    '''
    i = 0 
    #parcourir le tableau 
    while i < len(groupe):
        #variable qui va nous permettre de voir si toutes les personnes du groupe sont amis 
        personne2 = groupe[i]
        #si la condition est remplie alors 'personne1' n'est pas ami avec tout le monde 
        if not sont_amis(reseau, personne1, personne2):
            return False
        i += 1

    return True


#Question 6

def est_comu (reseau, groupe):
    '''
    Vérifie si tous les membres d'un groupe sont amis entre eux.

    La fonction parcourt toutes les paires possibles de membres dans le groupe
    et utilise la fonction 'sont_amis' pour vérifier si chaque paire est amie.

    Paramètres :
    reseau (dict) : Dictionnaire où les clés sont des prénoms et les valeurs sont des listes d'amis.
    groupe (list) : Liste des prénoms des personnes dans le groupe.

    Retourne :
    bool : True si tous les membres du groupe sont amis entre eux, False sinon.
    '''
    i = 0 
    #boucle qui va parcourir le groupe
    while i < len(groupe):
        j = i + 1
        #boucle qui parcoure le groupe et vérifie si 'i+1' est ami avec 'i' grâce à la fontions 'sont_amis'
        while j < len(groupe):
            #si la condition est remplie alors 'i' et 'i+1' ne sont pas amis
            if not sont_amis(reseau, groupe[i], groupe[j]):
                return False
            j += 1
        i += 1

    return True


#Question 7

def comu (reseau, groupe):
    '''
    Détermine une communauté d'amis compatibles dans un groupe.

    La fonction construit une communauté à partir des membres du groupe, en ajoutant
    les membres compatibles (c'est-à-dire ceux qui sont amis avec tous les membres
    déjà dans la communauté).

    Paramètres :
    reseau (dict) : Dictionnaire où les clés sont des prénoms et les valeurs sont des listes d'amis.
    groupe (list) : Liste des prénoms des personnes dans le groupe.

    Retourne :
    list : Une liste des membres formant une communauté d'amis compatibles.
    '''
    #tableau vide qui va stocker les membres qui sont tous amis
    communaute = []
    i = 0 
    #boucle qui va vérifié si la personne à l'indice 'i' est ami avec tout le groupe
    while i < len(groupe):
        membre = groupe[i]
        j = 0
        compatible = True
        #boucle qui parcoure tout le groupe a partir du début pour savoir si 'i' est ami avec tout le groupe
        while j < len(communaute):
            #si cette condition est remplie alors la personne à l'indice 'i' n'est pas ami avec tout le groupe 
            if not sont_amis(reseau, membre, communaute[j]):
                compatible = False
            j += 1
            #si True alors on ajoute la personne de l'indice 'i' à la communauté
        if compatible: 
            communaute.append(membre)
        i += 1

    return communaute 


#Question 8

def swap_tab(tab, i, j):                #fonction qui va nous permettre d'utilisé le tri à bulle 
    tab[i], tab[j] = tab[j], tab[i]     #permet d'écganger les positions de deux valeurs 

def tri_popu (reseau, groupe):
    '''
    Trie un groupe de personnes par popularité décroissante.

    La fonction utilise le tri à bulles pour organiser les membres d'un groupe
    en fonction du nombre d'amis qu'ils ont dans le réseau, du plus populaire au moins populaire.

    Paramètres :
    reseau (dict) : Dictionnaire où les clés sont des prénoms et les valeurs sont des listes d'amis.
    groupe (list) : Liste des prénoms des personnes à trier.

    Retourne :
    list : La liste triée des prénoms par popularité décroissante.
    '''     
    n = len(groupe)                     #utilisation du tri à bulle 
    while 1 < n:
        i = 0
        while i < n-1 :
            #compare la taille des deux listes d'ami si la liste de 'i' est plus grande que la liste de 'i+1' 
            #alors on échange l'indice grâce à la fonction 'swap_tab'
            if len(reseau[groupe[i]]) < len(reseau[groupe[i+1]]):
                swap_tab(groupe, i, i+1)
            i += 1
        n-=1
    return groupe


#Question 9

def comu_dans_reseau(reseau):
    '''
    Détermine une communauté d'amis compatibles la plus populaire dans un réseau.

    Cette fonction identifie une communauté à partir de toutes les personnes du réseau,
    trie les membres de cette communauté par popularité décroissante (nombre d'amis),
    puis retourne cette communauté triée.

    Paramètres :
    reseau (dict) : Dictionnaire où les clés sont des prénoms et les valeurs sont des listes d'amis.

    Retourne :
    list : Une liste triée des membres de la communauté compatible, par ordre de popularité décroissante.
    '''
    #variable qui contient tous les membres du réseau 
    personne = list(reseau.keys())
    #on tri par ordre décroissant les membres du réseau
    tri_popu(reseau, personne)
    #on définit une communauté 
    communaute = comu(reseau, personne)
    
    return communaute 


#Question 10

def comu_dans_amis(reseau, personne):
    '''
    Construit et retourne une communauté d'amis compatibles à partir d'une personne donnée.

    La fonction commence avec la personne spécifiée, puis parcourt les autres personnes dans le réseau,
    et ajoute celles qui sont amies avec tous les membres déjà présents dans la communauté.

    Paramètres :
    reseau (dict) : Dictionnaire où les clés sont des prénoms et les valeurs sont des listes d'amis.
    personne (str) : Le prénom de la personne à partir de laquelle construire la communauté.

    Retourne :
    list : Liste des membres de la communauté compatible.
    '''
    #si c'est vide 
    if len(personne) <= 0:
        return []
    #variable qui va contenir les membres d'une communauté 
    communaute = []
    #la communauté commence par la personne en paramètre (obligé de faire parti de la communauté) 
    communaute.append(personne)
    #variable qui contient les membres du réseau
    reste = reseau[personne]
    reste = tri_popu(reseau, reste)
    #parcourir les membres de la communauté
    i = 0 
    while i < len(reste):
        ajout = reste[i]
        #si 'i' est amis avec toute la communaute alors on l'ajoute à la communauté 
        if sont_amis_de (ajout, communaute, reseau):
            communaute.append(ajout)
        i += 1

    return communaute


#Question 12

def comu_max(reseau):
    '''
    Trouve la plus grande communauté d'amis compatibles dans un réseau.

    Cette fonction parcourt chaque personne dans le réseau et construit une communauté 
    compatible en partant de cette personne. Elle conserve la plus grande communauté 
    trouvée parmi toutes les personnes.

    Paramètres :
    reseau (dict) : Dictionnaire où les clés sont des prénoms et les valeurs sont des listes d'amis.

    Retourne :
    list : La plus grande communauté compatible trouvée dans le réseau.
    '''
    #Variable qui stockera la communaute maximale
    comu_maxi = []
    #variable qui contient les membres du réseau
    membre = list(reseau.keys())
    #boule qui parcoure tous les memebres du réseau 
    i = 0
    while i < len(membre):
        personne = membre[i]
        #définir la communauté de la personne de l'indice 'i' dans le réseau en paramètre
        communaute = comu_dans_amis(reseau, personne)
        #si le nombre de personne dans la communauté est suppérieur à celle de la communauté maximale alors elle l'a remplace
        if len(communaute) > len(comu_maxi):
            comu_maxi = communaute
        i += 1

    return comu_maxi