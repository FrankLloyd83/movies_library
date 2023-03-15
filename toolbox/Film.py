"""
Classe des objets film, qui permet de stocker les informations sur un film et de 
    - l'afficher : display_film()
    - le prêter à un ami : lent(friend)
"""

class Film:
    """
    Initialisation de la classe film : 'name' est son titre, 'date' est sa date de création, 
    et 'location' est le lieu où se situe le film ('home' si stocké par le propriétaire, 'nom_ami' 
    si stocké chez un ami).
    """

    def __init__(self, name, date, location='home'):
        self.name = name
        self.date = date
        self.location = location
    
    """
    Méthode d'affichage des informations du film sous forme de tableau.
    """

    def display_film(self):
        print('_' * 60)
        print('{:<35} {:<10} {:<10}'.format('Title', 'Year', 'Location'))
        print('-' * 60)
        print("{:<35} {:<10} {:<10}".format(
            self.name, self.date, self.location))
        print('_'*60)

    """
    Méthode qui permet de changer la propriété 'location' du film, et également d'ajouter ce film à la 
    liste des films possédés par l'ami 'friend'.
    """

    def lent(self, friend):
        self.location = friend.name
        friend.movies.append(self.name)
        print(f"{self.name} has been lent to {friend.name}.")

"""
Classe spécifique aux films sur VHF. Possède les mêmes méthodes que la classe Film, avec seulement un attribut
en plus : player
"""

class VhfFilm(Film):
    def __init__(self, name, date, player = 'vhf', location = 'home'):
        super().__init__(name, date, location)
        self.player = player

    def display_film(self):
        print('_' * 68)
        print('{:<35} {:<10} {:<10} {:<12}'.format(
            'Title', 'Year', 'Location', 'Player'))
        print('-' * 68)
        print('{:<35} {:<10} {:<10} {:<12}'.format(
            self.name, self.date, self.location, self.player))
        print('_' * 68)

    def lent(self, friend):
        super().lent(friend)

"""
Idem, mais pour les film de type DVD
"""

class DvdFilm(Film):
    def __init__(self, name, date, player = 'dvd', location = 'home'):
        super().__init__(name, date, location)
        self.player = player

    def display_film(self):
        print('_' * 68)
        print('{:<35} {:<10} {:<10} {:<12}'.format(
            'Title', 'Year', 'Location', 'Player'))
        print('-' * 68)
        print('{:<35} {:<10} {:<10} {:<12}'.format(
            self.name, self.date, self.location, self.player))
        print('_' * 68)

    def lent(self, friend):
        super().lent(friend)
