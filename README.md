# movies_library

## Fonctionnalités

Il y aura deux parties dans ce projet : le nettoyage des données puis le stockage des films.

### Nettoyage des données

Voici les données à traiter :

```python
films = [
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
```

Il y a quelques imperfections dans les données : la date est comprise dans le film, et les types sont écrits avec des casses aléatoires. Néanmoins, la date est écrite de manière homogène : il suffit de sélectionner les 7 derniers caractères, les retirer du titre du film, puis parmi ces 7 récupérer les 4 de l’année de création. Il faut aussi indiquer le lieu où le film est stocké actuellement Il nous faut donc trois fonctionnalités :

- Extraction de la date
- Homogénéisation de la casse du type
- Ecriture du lieu de stockage

### Stockage des films

- Un **Film** possède un **nom**, une **date de création**, et un **lieu de stockage.**
- Il y a 2 Types de films : les **films VHF** et les **films DVD**
- Chaque film est listé dans la **Bibliothèque**, qui les **trie par date**, **par nom** ou **par type**
- Nous pouvons **sélectionner un film au hasard**
- Des **amis** qui possèdent un **nom** peuvent avoir l’un de mes **Films** en prêt
- On peut **afficher la liste** des **Films prêtés**
- On peut **afficher** quel ami a notre **Film prêté**
