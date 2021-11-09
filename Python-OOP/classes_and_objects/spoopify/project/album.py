from project.song import Song


class Album:
    def __init__(self, name, *args):
        self.name = name
        self.songs = [x for x in args]
        self.published = False

    def add_song(self, song: Song):
        if song in self.songs:
            return f"Song is already in the album."
        else:
            if song.single:
                return f"Cannot add {song.name}. It's a single"
            if self.published:
                return f"Cannot add songs. Album is published."
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return f"Cannot remove songs. Album is published."
        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."
        return f"Song is not in the album."

    def publish(self):
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        songs_details = []
        for song in self.songs:
            songs_details.append(f"== {song.get_info()}")
        song_details_str = "\n".join(songs_details)
        return f"Album {self.name}\n{song_details_str}"