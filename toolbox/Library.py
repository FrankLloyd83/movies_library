from numpy import random
from operator import attrgetter
from toolbox.Film import Film

class Library:
    def __init__(self, films):
        self.films = films

    def display_lib(self):
        print('_' * 68)
        print('{:<35} {:<10} {:<10} {:<8}'.format('Title', 'Year', 'Location', 'Player'))
        print('-' * 68)

        for film in self.films:
            print('{:<35} {:<10} {:<10} {:<8}'.format(film.name, film.date, film.location, film.player))

        print('_'*68)

    def random_display(self):
        random.choice(self.films).display_film()

    def sort(self, criterion):
        if all(hasattr(film, criterion) for film in self.films):
            sorted_films = Library(sorted(self.films, key=attrgetter(criterion)))
            sorted_films.display_lib()
        else:
            print(f'{criterion} n\'est pas un critère de tri. Essayez avec "date", "name", "player" ou "location".')

    def add_film(self, new_film):
        self.films.append(new_film)
        return self.films
    
    def delete_film(self, film_to_delete):
        self.films.remove(film_to_delete)
        return self.films
    
    def finder(self, title):
        films = list(filter(lambda x: x.name == title, self.films))
        if not films :
            print(f'Le film {title} n\'est pas enregistré dans la bibliothèque.')
        else :
            for film in films:
                film.display_film()
    
class LentLibrary(Library):
    def __init__(self, films):
        super().__init__(films)
    
    def display_lib(self):
        print('_' * 68)
        print('{:<35} {:<10} {:<10} {:<8}'.format('Title', 'Year', 'Location', 'Player'))
        print('-' * 68)

        for film in self.films:
            if film.location != 'home':
                print('{:<35} {:<10} {:<10} {:<8}'.format(film.name, film.date, film.location, film.player))

        print('_'*68)
