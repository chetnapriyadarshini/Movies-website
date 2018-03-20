import movie
import fresh_tomatoes

# story variable stores the storyline of the movies
story = "In 1985 Dallas, electrician and hustler Ron Woodroof works around"\
	"the system to help AIDS patients get the medication they need after he is diagnosed with the disease."

#initialize movie object
dallasBuyerClub = movie.Movie("Dallas Buyers Club", story, "https://en.wikipedia.org/wiki/Dallas_Buyers_Club",
	"https://www.youtube.com/watch?v=fvMPU0WaPcc", "https://upload.wikimedia.org/wikipedia/en/a/a8/Dallas_Buyers_Club_poster.jpg")


#print(dallasBuyerClub.story)

story = "Aspiring musician Miguel, confronted with his family's ancestral ban on music,"\
" enters the Land of the Dead to find his great-great-grandfather, a legendary singer"


coco = movie.Movie("Coco", story, "https://en.wikipedia.org/wiki/Coco_(2017_film)", "https://www.youtube.com/watch?v=Rvr68u6k5sI",
	"https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg")

#print(coco.story)

story = "Four teenagers are sucked into a magical video game, and the only way they can escape is to work together to finish the game."

jumanji = movie.Movie("Jumanji", story, "https://en.wikipedia.org/wiki/Jumanji", "https://www.youtube.com/watch?v=2QKg5SZ_35I",
 "https://upload.wikimedia.org/wikipedia/en/d/dc/Jumanji_Welcome_to_the_Jungle.png")

story = "During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts."

spiritedAway = movie.Movie("Spirited Away", story, "https://en.wikipedia.org/wiki/Spirited_Away", "https://www.youtube.com/watch?v=ByXuk9QqQkk",
 "https://upload.wikimedia.org/wikipedia/en/d/db/Spirited_Away_Japanese_poster.png")

story = "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant"

ratatouille = movie.Movie("Ratatouille", story, "https://en.wikipedia.org/wiki/Ratatouille_(film)", "https://www.youtube.com/watch?v=uVeNEbh3A4U", 
	"https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg")

story = "A clumsy panda bear becomes an unlikely kung fu hero when a treacherous enemy spreads chaos throughout the countryside in this animated martial arts adventure "

kungFuPanda = movie.Movie("Kung Fu Panda", story, "https://en.wikipedia.org/wiki/Kung_Fu_Panda","https://www.youtube.com/watch?v=PXi3Mv6KMzY"
 , "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg")

#spiritedAway.showTrailer()

#create a list of the movie instances created
movieList = {dallasBuyerClub, coco, jumanji, spiritedAway, ratatouille, kungFuPanda}

#pass them to the movies page to be loaded
fresh_tomatoes.open_movies_page(movieList)