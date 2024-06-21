class Movie:
    def __init__(self, id, title, director, year, genre, synopsis):
        self.id = id
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.synopsis = synopsis


movies = [
    {
        "id": 1,
        "title": "The Shawshank Redemption",
        "director": "Frank Darabont",
        "year": 1994,
        "genre": ["Drama"],
        "synopsis": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
    },
    {
        "id": 2,
        "title": "The Godfather",
        "director": "Francis Ford Coppola",
        "year": 1972,
        "genre": ["Crime", "Drama"],
        "synopsis": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
    },
    {
        "id": 3,
        "title": "The Dark Knight",
        "director": "Christopher Nolan",
        "year": 2008,
        "genre": ["Action", "Crime", "Drama"],
        "synopsis": "When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.",
    },
    {
        "id": 4,
        "title": "Pulp Fiction",
        "director": "Quentin Tarantino",
        "year": 1994,
        "genre": ["Crime", "Drama"],
        "synopsis": "The lives of two mob hitmen, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
    },
    {
        "id": 5,
        "title": "Forrest Gump",
        "director": "Robert Zemeckis",
        "year": 1994,
        "genre": ["Drama", "Romance"],
        "synopsis": "The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal, and other historical events unfold from the perspective of an Alabama man with an IQ of 75.",
    },
    {
        "id": 6,
        "title": "Inception",
        "director": "Christopher Nolan",
        "year": 2010,
        "genre": ["Action", "Adventure", "Sci-Fi"],
        "synopsis": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
    },
    {
        "id": 7,
        "title": "Fight Club",
        "director": "David Fincher",
        "year": 1999,
        "genre": ["Drama"],
        "synopsis": "An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into much more.",
    },
    {
        "id": 8,
        "title": "The Matrix",
        "director": "Lana Wachowski, Lilly Wachowski",
        "year": 1999,
        "genre": ["Action", "Sci-Fi"],
        "synopsis": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
    },
    {
        "id": 9,
        "title": "The Lord of the Rings: The Return of the King",
        "director": "Peter Jackson",
        "year": 2003,
        "genre": ["Action", "Adventure", "Drama"],
        "synopsis": "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",
    },
    {
        "id": 10,
        "title": "The Silence of the Lambs",
        "director": "Jonathan Demme",
        "year": 1991,
        "genre": ["Crime", "Drama", "Thriller"],
        "synopsis": "A young F.B.I. cadet must receive the help of an incarcerated and manipulative cannibal killer to help catch another serial killer, a madman who skins his victims.",
    },
]
