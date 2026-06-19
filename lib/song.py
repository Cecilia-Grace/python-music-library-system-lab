class Song:
    count = 0
    genre_count = {}
    artist_count = {}
    genres = []
    artists = []

    def __init__(self, name, artist, genre):
        if Song.count == 0:
            Song.genre_count.clear()
            Song.artist_count.clear()
            Song.genres.clear()
            Song.artists.clear()

        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1
        
        if genre not in Song.genres:
            Song.genres.append(genre)
            
        if artist not in Song.artists:
            Song.artists.append(artist)

        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1
