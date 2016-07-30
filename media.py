# Creating Movie Class
class Movie():
    # Defining initiator function of movie class which has several arguements
    def __init__(self, movie_title, movie_storyline, poster_image, youtube_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
