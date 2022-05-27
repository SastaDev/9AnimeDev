const animedev = require('./animedev')

const AnimeDevClient = new animedev.client()

try {
    // Searching anime.
    const anime = AnimeDevClient.search('Doraemon') // enter your anime name instead of Doraemon.
    console.log(anime)
} catch (err) {
    console.log(err)
}

// Printing version of animedev.
console.log(animedev.version)