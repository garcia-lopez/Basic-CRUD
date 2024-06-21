from fastapi import Body, Form, FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from movie_data import movies
from typing import List


# Instantiate the FastAPI class and assign it to a variable app
app = FastAPI()

# agregamos un título y versión
app.title = "Movies API"
app.version = "0.0.1"

# Mount the static folder to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Function to create cards
def create_card(movie):
    return f"""
            <div class="element">
                <strong>{movie['title']}</strong> 
                <p>({movie['year']})</p>
                <p>Directed by {movie['director']}</p> 
                <p><strong>Genre:</strong> {", ".join(movie['genre'])}</p>
                <div class="container_buttons">
                  <a href="/movies/updateMovie/{movie["id"]}" ><img src="/static/circle.png" alt="editar" ></a>
                  <a href="/movies/deleteMovie/{movie["id"]}"><img src="/static/delete.png" alt="eliminar"></a>
                </div>
            </div>
        """


def cabeza(titulo):
    return f"""
      <!DOCTYPE html>
      <html>
      <head>
         <link rel="stylesheet" type="text/css" href="/static/style.css">
         <link rel="icon" type="image/x-icon" href="/static/icon.ico">
         <link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;700&display=swap" rel="stylesheet">
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>{titulo}</title>
      </head>"""


# Tags allow us to group the application's routes
@app.get("/", tags=["home"])
# Definimos una funcion que retorna un mensaje
def read_root():
    return HTMLResponse(
        f"""
        {cabeza("Home")}
        <body class="main">
            <h1>Movie List</h1>
            <p> Just for practice <p>
             <a href="/movies">
                <button class="button_class">Let's see the movies</button>
            </a>
        </body>
        </html>
            
        """
    )


# Route to get all movies
@app.get("/movies", tags=["movies"])
def obtener_peliculas():
    html_content = f"""
        {cabeza("Movie List")}
        <body>
            <h1 class="title">Movie List</h1>
            <div class="categories">
               <a href="/movies/filter/Action"><button class="button_class_categories">Action</button></a>
               <a href="/movies/filter/Adventure"><button class="button_class_categories">Adventure</button></a>
               <a href="/movies/filter/Crime=Crime"><button class="button_class_categories">Crime</button></a>
               <a href="/movies/filter/Drama"><button class="button_class_categories">Drama</button></a>
               <a href="/movies/filter/Romance"><button class="button_class_categories">Romance</button></a>
               <a href="/movies/filter/Sci-Fi"><button class="button_class_categories">Sci-Fi</button></a>
               <a href="/movies/filter/Thriller"><button class="button_class_categories">Thriller</button></a>
               <a href="/movies/addMovie"><button class="button_class_categories">New Movie</button></a>
            </div>
            <div class="container">
    """
    for movie in movies:
        html_content += create_card(movie)
    html_content += """
            </div>
        </body>
        </html>
    """
    return HTMLResponse(content=html_content)


# Route to filter movies by genre
@app.get("/movies/filter/{categorie}", tags=["movies"], response_class=HTMLResponse)
def get_movie_categories(categorie: str):
    _movies = [movie for movie in movies if categorie in movie["genre"]]
    html_content = f"""
        {cabeza("Filtered Movie List")}
        <body>
            <a href="/movies" ><img class="back_arrow" src="/static/respuesta.png" alt="Back Arrow"></a>
            <h1>Filtered Movie List <span class="filtered">{ categorie }</span></h1>
            <div class="container">
    """
    for movie in _movies:
        html_content += create_card(movie)
    html_content += """
            </div>
        </body>
        </html>
    """
    return HTMLResponse(content=html_content)


# Route to go to the form to add a new movie
@app.get("/movies/addMovie", tags=["movies"], response_class=HTMLResponse)
def get_formulario():
    form = f"""
       {cabeza("Add a New Movie")}
<body class="body_form">
    <a href="/movies" ><img class="back_arrow" src="/static/respuesta.png" alt="Back Arrow"></a>
    <h1>Add a New Movie</h1>
    <form class="formulario" action="/movies/add" method="post">       
        <label class="label-form" for="title">Title:</label>
        <input class="input-form" type="text" id="title" name="title" required>
        
        <label  class="label-form" for="director">Director:</label>
        <input  class="input-form" type="text" id="director" name="director" required>
        
        <label class="label-form" for="year">Year:</label>
        <input class="input-form" type="number" id="year" name="year" min=1888 required>
        
        <label class="label-form" for="genre">Genre</label>
        <fieldset class="genre_options">
          <input type="checkbox" name="genre" value="Action"> Action
          <input type="checkbox" name="genre" value="Adventure"> Adventure
          <input type="checkbox" name="genre" value="Crime"> Crime
          <input type="checkbox" name="genre" value="Drama"> Drama
          <input type="checkbox" name="genre" value="Romance"> Romance
          <input type="checkbox" name="genre" value="Sci-Fi"> Sci-Fi          
          <input type="checkbox" name="genre" value="Thriller"> Thriller
        </fieldset>
        
        <label  class="label-form" for="synopsis">Synopsis:</label>
        <textarea class="textarea-form" id="synopsis" name="synopsis" rows="4" required></textarea>
        
        <button class="button_form" type="submit">Add Movie</button>
    </form>
</body>
</html>
    """
    return HTMLResponse(content=form)


# Route to handle form submission for adding a new movie
@app.post("/movies/add", tags=["movies"])
def post_movie(
    title: str = Form(),
    director: str = Form(),
    year: int = Form(),
    genre: List[str] = Form(default=[]),
    synopsis: str = Form(),
):
    id = max(movie["id"] for movie in movies) + 1
    # Print the form data to the console
    print(
        f"New Movie Added - ID: {id}, Title: {title}, Director: {director}, Year: {year}, Genre: {genre}, Synopsis: {synopsis}"
    )

    # Normally you would append the data to your movies list here
    movies.append(
        {
            "id": id,
            "title": title,
            "director": director,
            "year": year,
            "genre": genre,
            "synopsis": synopsis,
        }
    )

    return RedirectResponse(url="/movies", status_code=303)


# Function to update a movie
@app.post("/movies/update/{id}", tags=["movies"])
def update_movie(
    id: int,
    title: str = Form(),
    director: str = Form(),
    year: int = Form(),
    genre: List[str] = Form(default=[]),  # The default value is an empty list
    synopsis: str = Form(),
):
    movie = next((movie for movie in movies if movie["id"] == id), None)
    if not movie:
        return {"error": "Movie not found"}

    movie["title"] = title
    movie["director"] = director
    movie["year"] = year
    movie["genre"] = genre  # Already a list of strings
    movie["synopsis"] = synopsis

    return RedirectResponse(url="/movies", status_code=303)


# Form to update an existing movie
@app.get("/movies/updateMovie/{id}", tags=["movies"], response_class=HTMLResponse)
#  Receives the movie id through the URL set in the <a> tag of the movie card with buttons: the path is /movies/updateMovie/{movie["id"]}
def update_form(id: int):
    # Find the movie by ID
    movie = next(
        (movie for movie in movies if movie["id"] == id), None
    )  # Creates an iterator that returns the first value that meets the condition, if none does it returns None
    if not movie:
        return HTMLResponse(
            content="<h1>Movie not found</h1>", status_code=404
        )  # If the movie is not found, it returns an error message and the 404 code
    #  When submitting the form, it references the path /movies/update/{id} with the POST method and sends the form data
    # With this expression, the genres that the movie contains are selected and the corresponding checkboxes are marked "checked" if "Crime" in movie["genre"] else ""
    form = f"""
         {cabeza("Edit Movie")}
<body class="body_form">
    <a href="/movies" ><img class="back_arrow" src="/static/respuesta.png" alt="Back Arrow"></a>
    <h1>Edit Movie</h1>
    <form class="formulario" action="/movies/update/{id}" method="post">  
        <label class="label-form" for="title">Title:</label>
        <input class="input-form" type="text" id="title" name="title" value="{movie['title']}" required>
        
        <label class="label-form" for="director">Director:</label>
        <input class="input-form" type="text" id="director" name="director" value="{movie['director']}" required>
        
        <label class="label-form" for="year">Year:</label>
        <input class="input-form" type="number" id="year" name="year" value="{movie['year']}" min=1888 required>
        
        <label class="label-form" for="genre">Genre</label>
        <fieldset class="genre_options">
          <input type="checkbox" name="genre" value="Action" {"checked" if "Action" in movie["genre"] else ""}> Action
          <input type="checkbox" name="genre" value="Adventure" {"checked" if "Adventure" in movie["genre"] else ""}> Adventure
          <input type="checkbox" name="genre" value="Crime" {"checked" if "Crime" in movie["genre"] else ""}> Crime
          <input type="checkbox" name="genre" value="Drama" {"checked" if "Drama" in movie["genre"] else ""}> Drama
          <input type="checkbox" name="genre" value="Romance" {"checked" if "Romance" in movie["genre"] else ""}> Romance
          <input type="checkbox" name="genre" value="Sci-Fi" {"checked" if "Sci-Fi" in movie["genre"] else ""}> Sci-Fi          
          <input type="checkbox" name="genre" value="Thriller" {"checked" if "Thriller" in movie["genre"] else ""}> Thriller
        </fieldset>
        
        <label class="label-form" for="synopsis">Synopsis:</label>
        <textarea class="textarea-form" id="synopsis" name="synopsis" rows="4" required>{movie['synopsis']}</textarea>
        
        <button class="button_form" type="submit">Update Movie</button>
    </form>
</body>
</html>
    """
    return HTMLResponse(content=form)


# Route to delete a movie
# For user interface reasons, a route is created to delete a movie using the GET method <<it's not a good practice, but it looks nice and I don't want to use js>>
def eliminar_pelicula(id: int):
    for movie in movies:
        if movie["id"] == int(id):
            movies.remove(movie)
            return RedirectResponse(url="/movies", status_code=303)


@app.get("/movies/deleteMovie/{id}", tags=["movies"])
# Form to delete an existing movie
def delete_form(id: int):
    # Find the movie by ID
    print(id)
    movie = next((movie for movie in movies if movie["id"] == id), None)
    if not movie:
        return HTMLResponse(content="<h1>Movie not found</h1>", status_code=404)
    form = f"""
         {cabeza("Delete Movie")}
 <body class="main">
            <h1 class="h1_delete">Are you sure you want to delete the movie: <span class="filtered">{movie["title"]}</span>?</h1>
            <div class="yes_no">
                <a href="/movies">
                <button class="button_class_categories" type="button">No</button>
                </a>
                <a href="/movies/delete/{id}">
                <button class="button_class_categories" type="submit">Yes</button>
                </a>
            </div>
 
            
        </body>
</html>
    """
    return HTMLResponse(content=form)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
