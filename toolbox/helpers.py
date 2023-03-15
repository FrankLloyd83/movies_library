from toolbox.Film import Film, DvdFilm, VhfFilm
from toolbox.Friend import Friend
    
def get_name_date(movies):
    my_films = []
    for film in movies:
        raw_title = film[0]
        type = film[1].lower()
        if type == 'dvd':
            my_film = DvdFilm(raw_title[:-7], raw_title[-5:-1], type)
        elif type == 'vhf':
            my_film = VhfFilm(raw_title[:-7], raw_title[-5:-1], type)
        else:
            my_film = Film(raw_title[:-7], raw_title[-5:-1])
        my_films.append(my_film)
    return my_films

def set_locations(library, friends):
    for friend in friends:
        if len(friend)>1:
            my_friend = Friend(friend[0], [friend[1]])
            film_title = my_friend.movies
            film_lent = list(filter(lambda x :x.name in film_title, library.films))
            for film in film_lent:
                film.lent(my_friend)
    return library