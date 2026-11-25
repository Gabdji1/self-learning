# Two Sum : existe-t-il deux nombres dans la liste
# dont la somme est égale à la cible ?


# Version 1 : lente, O(n²)
# On teste toutes les paires possibles avec deux boucles imbriquées.
def two_sum_lent(liste, cible): 
    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):
            if liste[i]+liste[j] == cible:
                return "yes"
    return "no" 


# Version 2 : rapide, O(n)
# On parcourt la liste une seule fois en gardant
# les nombres déjà vus dans un set.
def two_sum_rapide(liste, cible):
    vu = set()
    for i in liste:
        complement = cible-i
        if complement in vu:
            return("yes")
        else:
            vu.add(i)
    return "no"


# Tests
print("Version lente :")
print(two_sum_lent([3, 8, 1, 5, 12], 13))   # yes
print(two_sum_lent([3, 8, 1, 5, 12], 30))   # no
print(two_sum_lent([3, 8, 1, 5, 12], 16))   # no
print(two_sum_lent([3], 100))               # no

print("Version rapide :")
print(two_sum_rapide([3, 8, 1, 5, 12], 13))   # yes
print(two_sum_rapide([3, 8, 1, 5, 12], 30))   # no
print(two_sum_rapide([3, 8, 1, 5, 12], 16))   # no
print(two_sum_rapide([3], 100))               # no


def afficher_positions(liste):
    # pour chaque position i, afficher : "position", i, "valeur", liste[i]
    for i in range(len(liste)):
        print(f"position {i} valeur {liste[i]}")

afficher_positions([3, 8, 1, 5, 12])