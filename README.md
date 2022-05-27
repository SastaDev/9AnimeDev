# 9AnimeDev
A <a href='https://9anime.dev'>9anime.dev</a> scrapper module for python.

# Available in programming languages
```py
1. Python
```
```node
2. Node.JS
```

# Installation

Installing through pip for python.

```bash
pip install animedev
```

Cloning using git.

for python:
```sh
git clone https://github.com/SastaDev/9AnimeDev/for_python
```

for node.js:
```sh
git clone https://github.com/SastaDev/9AnimeDev/for_node
```

# How To Use?

The python way:
Check out examples.py inside for_python folder.

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

The node.js way:

Check out examples.js inside for_node folder.

<b>Examples.js</b>
```node
const animedev = require('animedev')

const AnimeDevClient = new animedev.client()

try {
    // Searching anime.
    const anime = AnimeDevClient.search('Doraemon') // enter your anime name instead of Doraemon.
    console.log(anime)
} catch (err) {
    console.log(err)
}
```
To check version of animedev.

```node
// Printing version of animedev.
const animedev = require('animedev')
console.log(animedev.version)
```

# Thanks
Thanks to <a href='https://github.com/itspro-dev'>@itspro-dev</a> for <a href='https://9anime.dev'>9anime.dev</a>.
Thanks to <a href='https://github.com/SastaDev'>@SastaDev</a> for <a href='https://github.com/SastaDev/9AnimeDev'>this scrapper</a>.

© <a href='https://telegram.dog/SastaNetwork'>Sasta Network</a> 2022.
