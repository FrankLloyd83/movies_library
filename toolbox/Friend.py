"""
Classe Friend qui a une méthode :
    - display() : affiche la liste de films en possession de l'ami
"""

class Friend:
    def __init__(self, name, movies=[]):
        self.name = name
        self.movies = movies
    
    def display(self):
        print(f'Your friend {self.name} currently holds your movie(s) {[movie.name for movie in self.movies]}')
