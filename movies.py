import media
import webbrowser
import fresh_tomatoes

#declaration of movie objects
ltr1 = media.Movie("The Lord of the Rings: Fellowship of the Rings","Quest to destroy the one ring","https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg","https://www.youtube.com/watch?v=V75dMMIW2B4")
ltr2 = media.Movie("The Lord of The Rings: The Twin Towers","Battle of Helms Deep","https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg","https://www.youtube.com/watch?v=cvCktPUwkW0")
ltr3 = media.Movie("The Lord of The Rings: Fellowship of the Ring","Quest to destroy the one ring","https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg","https://www.youtube.com/watch?v=r5X-hFf6Bwo")
hb1 = media.Movie("The Hobbit: An Unexpected Journey","Set to reclaim Erebor","https://upload.wikimedia.org/wikipedia/en/b/b3/The_Hobbit-_An_Unexpected_Journey.jpeg","https://www.youtube.com/watch?v=SDnYMbYB-nU")
hb2 = media.Movie("The Hobbit: The Desolation of Smaug","The awakening of the dragon","https://upload.wikimedia.org/wikipedia/en/4/4f/The_Hobbit_-_The_Desolation_of_Smaug_theatrical_poster.jpg","https://www.youtube.com/watch?v=OPVWy1tFXuc")
hb3 = media.Movie("The Hobbit:  The Battle of the Five Armies","The battle for the mountain","https://upload.wikimedia.org/wikipedia/en/0/0e/The_Hobbit_-_The_Battle_of_the_Five_Armies.jpg","https://www.youtube.com/watch?v=iVAgTiBrrDA")


movieList=[];
movieList=[ltr1,ltr2,ltr3,hb1,hb2,hb3];

#generating the movie page
fresh_tomatoes.open_movies_page(movieList)
