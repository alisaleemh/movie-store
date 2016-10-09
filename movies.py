import media
import webbrowser
import fresh_tomatoes

dch = media.Movie("Dil Chahta Hay","A funny story","https://en.wikipedia.org/wiki/Dil_Chahta_Hai","https://www.youtube.com/watch?v=0pzF-MbiiZ0")

pch = media.Movie("The Lord of The Rings: Fellowship of the Ring","Quest to destroy the one ring","https://en.wikipedia.org/wiki/Dil_Chahta_Hai","https://www.youtube.com/watch?v=0pzF-MbiiZ0")

movieList=[];

movieList=[dch,pch]

fresh_tomatoes.open_movies_page(movieList)
