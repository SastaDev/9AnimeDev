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
    except Exception as e:
        print(e)
        return

# Searching anime.
search_anime('Doraemon') # Add your anime name instead of Doraemon.

# Printing version of animedev.
import animedev
print(animedev.__version__)
