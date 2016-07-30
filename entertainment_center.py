# Importing media.py and fresh_tomatoes.py
import media
import fresh_tomatoes

# Creating Toy Story movie instance
toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Creating Suicide Squad movie instance
suicide_squad = media.Movie("Suicide Squad",
                        "Intelligence officer Amanda Waller (Viola Davis) decides to assemble a team of dangerous, incarcerated supervillains for a top-secret mission. ",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/5/50/Suicide_Squad_%28film%29_Poster.png/220px-Suicide_Squad_%28film%29_Poster.png",
                        "https://www.youtube.com/watch?v=CmRih_VtVAs")

# Creating Ghostbusters movie instance
ghostbusters = media.Movie("Ghostbusters",
                        "Paranormal researcher Abby Yates (Melissa McCarthy) and physicist Erin Gilbert are trying to prove that ghosts exist in modern society",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/d/d0/Ghostbusters_2016_film_poster.jpg/220px-Ghostbusters_2016_film_poster.jpg",
                        "https://www.youtube.com/watch?v=w3ugHP-yZXw")

# Creating Nerve movie instance
nerve = media.Movie("Nerve",
                        "Industrious high school senior Vee Delmonico (Emma Roberts) is tired of living life on the sidelines. Pressured by her friends, Vee decides to join Nerve, a popular online game that challenges players to accept a series of dares.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/e/e2/Nerve_2016_poster.jpg/220px-Nerve_2016_poster.jpg",
                        "https://www.youtube.com/watch?v=AX1BTiHzq-I")

# Create movies list called movies
movies = [toy_story, suicide_squad, ghostbusters, nerve]

# Using open_movies_page function of fresh_tomatoes file to open movies page in a browser
fresh_tomatoes.open_movies_page(movies)

