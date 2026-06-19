class Song:
    _count = 0  
    genre_count = {}
    artist_count = {}
    
    _genres = set()
    _artists = set()
    
    def __init__(self, name, artist, genre):
        if Song._count == 0:
            Song.genre_count.clear()
            Song.artist_count.clear()
            Song._genres.clear()
            Song._artists.clear()
        
        self.name = name
        self.artist = artist
        self.genre = genre
        
        Song._count += 1
        
        Song._genres.add(genre)
        Song._artists.add(artist)
        
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
            
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
        
        
    @classmethod
    def count(cls):
        return cls._count
    
    @classmethod
    def genres(cls):
        return list(cls._genres)
    
    @classmethod
    def artists(cls):
        return list(cls._artists)
        
                

song1 = Song("99 Problems", "Jay Z", "Rap")
song2 = Song("Halo", "Beyonce", "Pop")
song3 = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
song4 = Song("Out of Touch", "Hall and Oates", "Pop")
song5 = Song("Drunk In Love", "Beyonce", "Pop")
song6 = Song("Show You Off", "Justin Bieber", "RnB")


    
print(Song.count())
print(Song.genres())
print(Song.artists())
print(Song.genre_count)
print(Song.artist_count)