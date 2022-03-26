class PhotoAlbum:
    photos_per_page = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[]*self.photos_per_page for i in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count//cls.photos_per_page)

    def add_photo(self, label:str):
        for i in range(0, self.pages):
            if len(self.photos[i]) < self.photos_per_page:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i+1} slot {self.photos_per_page - (self.photos_per_page - len(self.photos[i]))}"
        return "No more free slots"

    def display(self):
        string_repr = "-----------\n"
        for n in range(0, self.pages):
            frames = []
            for photo in self.photos[n]:
                frames.append("[]")
            frames_str = " ".join(frames)
            string_repr += frames_str
            string_repr += "\n-----------\n"
        return string_repr

album = PhotoAlbum(3)
for _ in range(8):
    album.add_photo("asdf")
print(album.display().strip())