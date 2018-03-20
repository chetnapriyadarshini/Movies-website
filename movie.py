import webbrowser

class Movie():

	def __init__(self, movieTitle, movieStoryLine, movieLink, movieTrailer, moviePoster):
		"""This is a example showing docstrings
    
    Attributes:
        title (str): Title of the movie
        story (str): Story of the movie
        link (str): Link containing more details about the movie
        trailer(str) : You tube trailer ID
    	poster(str) : Link to the poster of the movie
    """
		self.title = movieTitle;
		self.story = movieStoryLine;
		self.link = movieLink;
		self.trailer = movieTrailer;
		self.poster = moviePoster;

	def showTrailer(self):
		webbrowser.open(self.trailer)