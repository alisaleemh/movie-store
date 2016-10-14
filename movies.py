import media
import webbrowser
import fresh_tomatoes

#declaration of movie objects
ltr1 = media.Movie("The Lord of the Rings: Fellowship of the Rings","Quest to destroy the one ring","https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg","https://www.youtube.com/watch?v=V75dMMIW2B4")
ltr2 = media.Movie("The Lord of The Rings: The Twin Towers","Battle of Helms Deep","https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg","https://www.youtube.com/watch?v=cvCktPUwkW0")
ltr3 = media.Movie("The Lord of The Rings: Fellowship of the Ring","Quest to destroy the one ring","https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg","https://www.youtube.com/watch?v=r5X-hFf6Bwo")
hb1 = media.Movie("The Lord of The Rings: Fellowship of the Ring","Quest to destroy the one ring","","")
hb2 = media.Movie("The Lord of The Rings: Fellowship of the Ring","Quest to destroy the one ring","","")
hb3 = media.Movie("The Lord of The Rings: Fellowship of the Ring","Quest to destroy the one ring","","")



movieList=[];

movieList=[ltr1,ltr2,ltr3]

fresh_tomatoes.open_movies_page(movieList)
