class Music:
    def __init__(self, title: str, artist: str, lyrics: str):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics

song1 = Music("Slim Shady", "Eminem", "Who's the real Slim Shady?")
print(song1.print_info())
print(song1.play())