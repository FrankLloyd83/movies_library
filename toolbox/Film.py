class Film:
    def __init__(self, name, date, location='home'):
        self.name = name
        self.date = date
        self.location = location
    
    def display_film(self):
        print('_' * 60)
        print('{:<35} {:<10} {:<10}'.format('Title', 'Year', 'Location'))
        print('-' * 60)
        print("{:<35} {:<10} {:<10}".format(self.name, self.date, self.location))
        print('_'*60)
    
    def lent(self, friend):
        self.location = friend.name
        friend.movies.append(self.name)
        print(f"{self.name} has been lent to {friend.name}.")

class VhfFilm(Film):
    def __init__(self, name, date, player):
        super().__init__(name, date)
        self.player = player
        self.location = 'home'
    
    def display_film(self):
        print('_' * 68)
        print('{:<35} {:<10} {:<10} {:<12}'.format('Title', 'Year', 'Location', 'Player'))
        print('-' * 68)
        print('{:<35} {:<10} {:<10} {:<12}'.format(self.name, self.date, self.location, self.player))
        print('_' * 68)
    
    def lent(self, friend):
        super().lent(friend)
        

class DvdFilm(Film):
    def __init__(self, name, date, player):
        super().__init__(name, date)
        self.player = player
        self.location = 'home'

    def display_film(self):
        print('_' * 68)
        print('{:<35} {:<10} {:<10} {:<12}'.format('Title', 'Year', 'Location', 'Player'))
        print('-' * 68)
        print('{:<35} {:<10} {:<10} {:<12}'.format(self.name, self.date, self.location, self.player))
        print('_' * 68)
    
    def lent(self, friend):
        super().lent(friend)