var sync_request = require('sync-request')

class client {
    constructor() {
        this.base_url = 'https://9anime.dev'
    }
    search(anime_name) {
        const r = sync_request('GET', this.base_url + '/anime?search=' + anime_name)
        if (r.statusCode === 404) {
            throw new Error('Not Found.')
        }
        if (r.statusCode  !== 200) {
            throw new Error(`ERROR: ${r.body}`)
        }
        const j = JSON.parse(r.body)
        j['Search_Query'].replace(/ /g, '+')
        return j
    }
}

const version = '1.0.0'

module.exports = {
    client: client,
    version: version
}