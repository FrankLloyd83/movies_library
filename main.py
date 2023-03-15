""" Import des fonctions et classes nécessaires au script principal """
from toolbox.helpers import set_locations, get_name_date
from toolbox.Library import Library, LentLibrary

""" Données brutes """
raw_films = [
    ("Blade Runner (1982)", "vhf"),
    ("Alien : Le 8ème Passager (1979)", "vhf"),
    ("2001 : L'Odyssée de l'espace (1968)", "VhF"),
    ("Matrix (1999)", "DVD"),
    ("Interstellar (2014)", "dvD"),
    ("L'Empire contre-attaque (1980)", "vhf"),
    ("Retour vers le futur (1985)", "vhf"),
    ("La Guerre des Étoiles (1977)", "vhf"),
    ("L'Armée des 12 singes (1995)", "dVd"),
    ("Terminator 2 : Le Jugement dernier (1991)", "DVD"),
]

friends = [
    ("Paul", "Blade Runner"),
    ("Lucie",),
    ("Zoé", "Terminator 2 : Le Jugement dernier"),
]

""" Programme principal """
def main():
    my_films = get_name_date(raw_films)
    my_library = Library(my_films)
    my_library = set_locations(my_library, friends)
    my_lent_library = LentLibrary(my_films)
    print('Programme terminé')

if __name__ == '__main__':
    main()