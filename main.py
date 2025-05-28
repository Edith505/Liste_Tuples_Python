# TODO 1: Créer une liste de 3 fruits et l'afficher
def creer_liste_fruits():
    """ () -> list
    Retourne une liste contenant trois fruits au choix.
    ['pomme', 'banane', 'orange']
    """
    liste = []
    for i in range(3):
        fruits = input("Ajouter un fruit: ")
        liste.append(fruits)
    return liste


# TODO 2: Retourner le premier et le dernier élément d'une liste
def premier_et_dernier(liste):
    """ (list) -> tuple
    Retourne le premier et le dernier élément d'une liste.
    Ex : premier_et_dernier([10, 20, 30, 40])
    (10, 40)
    """
    pass


# TODO 3: Ajouter "mangue" à la liste et supprimer "banane" si elle existe
def modifier_liste(liste):
    """ (list) -> list
    Ajoute "mangue" à la liste et supprime "banane" si elle est présente.
    Ex : modifier_liste(['pomme', 'banane', 'kiwi'])
    ['pomme', 'kiwi', 'mangue']
    """
    pass


# TODO 4: Supprimer les doublons dans une liste sans utiliser set
def supprimer_doublons(liste):
    """ (list) -> list
    Retourne une nouvelle liste sans doublons, en conservant l'ordre.
    Ex : supprimer_doublons([1, 2, 2, 3, 1, 4])
    [1, 2, 3, 4]
    """
    pass


# TODO 5: Associer deux listes sous forme de tuples
def associer_listes(noms, notes):
    """ (list, list) -> list of tuples
    Associe chaque nom avec la note correspondante.
     Ex : associer_listes(['Alice', 'Bob'], [15, 12])
    [('Alice', 15), ('Bob', 12)]
    """
    pass


# TODO 6: Retourner les notes supérieures ou égales à un seuil donné
def notes_reussies(notes, seuil):
    """ (list of float, float) -> list of float
    Retourne une liste de notes supérieures ou égales au seuil.
    Ex : notes_reussies([8.5, 12.0, 9.0, 14.5], 10)
    [12.0, 14.5]
    """
    pass


# TODO 7: Extraire les noms avec une note >= 10 à partir d'une liste de tuples
def noms_des_reussites(paires):
    """ (list of (str, float)) -> list of str
    Retourne les noms des personnes qui ont une note >= 10.
    Ex : noms_des_reussites([('Alice', 15), ('Bob', 9.5), ('Carla', 11)])
    ['Alice', 'Carla']
    """
    pass


# TODO 8: Trouver l'élément le plus fréquent dans une liste
def element_plus_frequent(liste):
    """ (list) -> any
    Retourne l'élément le plus fréquent dans la liste.
    Ex : element_plus_frequent(['a', 'b', 'a', 'c', 'a', 'b'])
    'a'
    """
    pass


# TODO 9: Inverser les éléments d'une liste
def inverser_liste(liste):
    """ (list) -> list
    Retourne la liste inversée.
    Ex : inverser_liste([1, 2, 3])
    [3, 2, 1]
    """


# TODO 10: Calculer la moyenne à partir d'une liste de notes
def moyenne(notes):
    """ (list of float) -> float
    Retourne la moyenne des notes.
    Ex : moyenne([10.0, 12.0, 14.0])
    12.0
    """
    pass


print("-----------/ application / -----------")
fruit = creer_liste_fruits()
print(fruit)
