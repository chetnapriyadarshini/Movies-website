import webbrowser

class Movie():

	def __init__(self, movieTitle, movieStoryLine, movieLink, movieTrailer, moviePoster):
		self.title = movieTitle;
		self.story = movieStoryLine;
		self.link = movieLink;
		self.trailer = movieTrailer;
		self.poster = moviePoster;

	def showTrailer(self):
		webbrowser.open(self.trailer)