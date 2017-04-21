import fresh_tomatoes
import media

forest_gump = media.Movie("Forest Gump",
                        "Forrest Gump, while not intelligent, has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him. ",
                        "https://upload.wikimedia.org/wikipedia/pt/c/c0/ForrestGumpPoster.jpg",
                        "https://www.youtube.com/watch?v=bLvqoHBptjg")

enemy_at_the_gates = media.Movie("Enemy at the Gates",
                        "A Russian and a German sniper play a game of cat-and-mouse during the Battle of Stalingrad", "http://3.bp.blogspot.com/_g3nSNR9hosY/SkaWj5yHpSI/AAAAAAAAB44/zqFOb42UOVI/s400/venemyatthegates.jpg",
                        "https://www.youtube.com/watch?v=4O-sMh_DO6I")

the_dark_knight = media.Movie("Batman - The Dark Knight",
                        " In the film, Bruce Wayne/Batman (Bale), James Gordon (Oldman) and Harvey Dent (Eckhart) form an alliance to dismantle organised crime in Gotham City, but are menaced by a criminal mastermind known as the Joker (Ledger) who seeks to undermine Batman's influence and create chaos. ","https://upload.wikimedia.org/wikipedia/pt/thumb/d/d1/The_Dark_Knight.jpg/250px-The_Dark_Knight.jpg",
                        "https://www.youtube.com/watch?v=EXeTwQWrcwY")

three_hundred  = media.Movie("300",
                        " King Leonidas of Sparta and a force of 300 men fight the Persians at Thermopylae in 480 B.C.", "http://static.rogerebert.com/uploads/movie/movie_poster/300-2006/large_4AmPMxTs1zSdCK0eCacj0kBgOMV.jpg",
                        "https://www.youtube.com/watch?v=wDiUG52ZyHQ")

fight_club = media.Movie("Fight Club",
                        " An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more.", "http://br.web.img3.acsta.net/medias/nmedia/18/90/95/96/20122166.jpg",
                        "https://www.youtube.com/watch?v=SUXWAEX2jlg")

the_matrix = media.Movie("Fight Club",
                        " A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.", "https://upload.wikimedia.org/wikipedia/pt/c/c1/The_Matrix_Poster.jpg",
                        "https://www.youtube.com/watch?v=m8e-FF8MsqU")

movies = [forest_gump, enemy_at_the_gates, the_dark_knight, three_hundred, fight_club, the_matrix]

fresh_tomatoes.open_movies_page(movies)
#forest_gump.show_trailer()

#print (forest_gump.title + " " + forest_gump.storyline+" "+ forest_gump.poster_image_url+ ' '+ forest_gump.trailer_youtube_url)

