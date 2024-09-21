class Song:
    count = 0
    genres = []
    artists = [] 
    genre_count = {}
    artist_count = {} 

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()

        self.genres.append(genre)
        self.artists.append(artist)

        self.add_to_artist_count(artist)
        self.add_to_genre_count(genre)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genre_count(cls, genre):
        """Updates the genre_count dictionary to keep track of how many songs belong to each genre."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Updates the artist_count dictionary to keep track of how many songs each artist has."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    @classmethod
    def get_genre_histogram(cls):
        """Returns a dictionary showing the count of songs for each genre (histogram)."""
        return cls.genre_count

    @classmethod
    def get_artist_histogram(cls):
        """Returns a dictionary showing the count of songs for each artist (histogram)."""
        return cls.artist_count
