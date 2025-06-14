#!/usr/local/bin/python
from comu import *

reseau = {
        "Alice" : ["Bob", "Dan"],
        "Bob" : ["Alice", "Carl", "Dan"],
        "Carl" : ["Bob"],
        "Dan" : ["Alice", "Bob"]
       } 

reseau2 = {
        "Alice" : ["Bob"],
        "Bob" : ["Alice", "Carl"],
        "Carl" : ["Bob"],
       } 

reseau3 = {} 

amis = ["Alice", "Bob", "Alice", "Dan", "Bob", "Carl", "Bob", "Dan"]

#test de la fonction cree_reseau

def test_cree_reseau():

    assert cree_reseau(amis)["Alice"] == ["Bob", "Dan"]
    assert cree_reseau(amis)["Bob"] == ["Alice", "Carl", "Dan"]
    assert cree_reseau(amis)["Carl"] == ["Bob"]
    assert cree_reseau(amis)["Dan"] == ["Alice", "Bob"]
    assert not cree_reseau(amis)["Alice"] == ["Carl", "Dan"]
    assert not cree_reseau(amis)["Carl"] == ["Dan"]
    print("Les test de la fonction cree_reseau  : OK")


test_cree_reseau()


#test de la fonction liste_personnes

def test_liste_personnes():
    
    assert liste_personnes(reseau) == ['Alice', 'Bob', 'Carl', 'Dan']
    assert liste_personnes(reseau2) == ['Alice', 'Bob', 'Carl']
    assert liste_personnes(reseau3) == []
    assert not liste_personnes(reseau) == ['Alice', 'Bob', 'Carl', 'Dan', 'Bryan']
    print("Les tests de la fonction liste_personnes : OK")

test_liste_personnes()


#test de la fonction sont_amis

def test_sont_amis():
    
    assert sont_amis(reseau, "Alice", "Bob") == True
    assert sont_amis(reseau, "Bob", "Dan") == True 
    assert sont_amis(reseau2, "Carl","Bob") == True
    assert sont_amis(reseau3, "", "" ) == False
    assert not sont_amis(reseau, "Alice", "Carl") == True
    print("Les tests de la fonction sont_amis : OK")

test_sont_amis()

#test de la fonction sont_amis_de

def test_sont_amis_de():
    assert sont_amis_de("Alice", ["Bob", "Carl"], reseau) == False
    assert sont_amis_de("Alice", ["Bob", "Dan"], reseau) == True 
    assert sont_amis_de("", ["", ""], reseau3) == False
    assert not sont_amis_de("Alice", ["Bob", "Carl"], reseau) == True
    print("Les tests de la fonction sont_amis_de : OK")

test_sont_amis_de()

#test de la fonction est_comu

def test_est_comu():
    assert est_comu(reseau, ["Alice", "Bob", "Dan"]) == True
    assert est_comu(reseau, ["Bob", "Dan", "Carl"]) == False
    assert est_comu(reseau3, [""]) == True
    assert not est_comu(reseau, ["Alice", "Bob", "Dan"]) == False
    print("Les tests de la fonction est_comu : OK")

test_est_comu()

#test de la fonction comu

def test_comu():
    assert comu(reseau, ["Alice", "Bob", "Carl", "Dan"]) == ['Alice', 'Bob', 'Dan']
    assert comu(reseau, ["Carl", "Alice", "Bob", "Dan"]) == ['Carl', 'Bob']
    assert comu(reseau, ["Carl", "Alice", "Dan"]) == ["Carl"]
    assert comu(reseau3, [""]) == [""]
    assert not comu(reseau, ["Alice", "Bob", "Carl", "Dan"]) == ['Bob', 'Alice', 'Dan']
    print("Les tests de la focntion comu : OK")

test_comu()

#test de la fonction tri_popu

def test_tri_popu():
    assert tri_popu(reseau, ["Alice", "Bob", "Carl"]) == ['Bob', 'Alice', 'Carl']
    assert tri_popu(reseau, ["Alice", "Bob", "Carl", "Dan"]) == ['Bob', 'Alice', 'Dan', 'Carl']
    assert tri_popu(reseau3, [""]) == ['']
    assert not tri_popu(reseau, ["Alice", "Bob", "Carl", "Dan"]) == ['Carl', 'Alice', 'Bob']
    print("Les tests de la fonction tri_popu : OK")

test_tri_popu()

#test de la fonction comu_dans_reseau

def test_comu_dans_reseau():
    assert comu_dans_reseau(reseau) == ['Bob', 'Alice', 'Dan']
    assert comu_dans_reseau(reseau2) == ['Bob', 'Alice']
    assert comu_dans_reseau(reseau3) == []
    assert not comu_dans_reseau(reseau) == ['Bob', 'Alice', 'Dan', 'Carl']
    print("Les tests de la fonction comu_dans_reseau : OK")

test_comu_dans_reseau()

#test de la fonction comu_dans_amis

def test_comu_dans_amis():
    assert comu_dans_amis(reseau, "Alice") == ['Alice', 'Bob', 'Dan']
    assert comu_dans_amis(reseau2, "Alice") == ['Alice', 'Bob']
    assert comu_dans_amis(reseau3, "") == []
    assert not comu_dans_amis(reseau, "Alice") == ['Bob', 'Alice', 'Dan']
    print("Les tests de la fonction comu_dans_amis : OK")

test_comu_dans_amis()

#test de la fonction comu_max

def test_comu_max():
    assert comu_max(reseau) == ['Alice', 'Bob', 'Dan']
    assert comu_max(reseau2) == ['Alice', 'Bob']
    assert comu_max(reseau3) == []
    assert not comu_max(reseau) == ['Alice', 'Bob', 'Dan', 'Carl']
    print("Les tests de la fonction comu_max : OK")

test_comu_max()