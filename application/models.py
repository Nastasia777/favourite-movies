from application import db, app

app.app_context().push()

class FavouriteMovie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    short_description = db.Column(db.String(500), nullable=False)
    
    def __init__(self, title, duration_minutes, genre, short_description):
        self.title = title
        self.duration_minutes = duration_minutes
        self.genre = genre
        self.short_description = short_description
    
    def __repr__(self):
        return f"This movies title is {self.title}, it longs {self.duration_minutes}, genre is {self.genre} and short description is {self.short_description}"
