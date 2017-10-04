import webbrowser#used to import the webbrowser class to my page

class Movie():#here class movie is used to make a site
    def __init__(self,movie_title,movie_storyline,poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        #it take self as input and display the trailer of movie on which we click
    
