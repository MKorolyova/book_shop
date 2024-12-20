class Genre:

    def __init__(self):
        self.genre_id = None
        self.genre = None
        self.description = None
     
    def to_dict(self):
        return {
            'genre_id': self.genre_id,
            'genre': self.genre,
            'description': self.description
        }
    
    def from_dict(self, data):
        self.genre_id = data["genre_id"]
        self.genre = data["genre"]
        self.description = data["description"]
        return self
    
