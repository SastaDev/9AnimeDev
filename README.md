# 9AnimeDev
A <a href='https://9anime.dev'>9anime.dev</a> scrapper module for python.

# Installation

Installing through pip.

```bash
pip install animedev
```

Cloning using git.

```bash
git clone https://github.com/SastaDev/9AnimeDev/src
```

# How To Use?
Check out examples.py inside src folder.

<b>Examples.py:</b>
```py
from animedev import client, exceptions

def search_anime(anime_name):
    try:
        anime = client.search(anime_name)
        text = f'''
Anime Title: {anime['AnimeTitle']}

Anime Link: {anime['AnimeLink']}

Anime Image: {anime['AnimeImg']}

Search Query: {anime['Search_Query']}
'''

        print(text)
    except exceptions.NotFound as e:
        print(e)
        return

# Searching anime.
search_anime('Doraemon') # Add your anime name instead of Doraemon.
```

To check version of animedev.

```py
# Printing version of animedev.
import animedev
print(animedev.__version__)
```

# Thanks
Thanks to <a href='https://github.com/itspro-dev'>@itspro-dev</a> for <a href='https://9anime.dev'>9anime.dev</a>.
Thanks to <a href='https://github.com/SastaDev'>@SastaDev</a> for <a href='https://github.com/SastaDev/9AnimeDev'>this scrapper</a>.

© <a href='https://telegram.dog/SastaNetwork'>Sasta Network</a> 2022.