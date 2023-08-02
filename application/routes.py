from application import app, db
from flask import request, jsonify, render_template, redirect
from application.models import FavouriteMovie
from application.forms import AddMovieForm

def format_movie(movie):
    return {
        "title": movie.title,
        "duration_minutes": movie.duration_minutes,
        "genre": movie.genre,
        "short_description": movie.short_description
    }

@app.route("/")
def greeting():
    return render_template('home.html')

# POST / GET
@app.route("/movies", methods=["POST", "GET"])
def movies():
    form = AddMovieForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            movie = FavouriteMovie(form.title.data, form.duration_minutes.data, form.genre.data, form.short_description.data)
            db.session.add(movie)
            db.session.commit()
            return redirect('/')
        else:
            movies = FavouriteMovie.query.all()
            movie_list = [format_movie(movie) for movie in movies]
            return render_template('movies.html', movies=movie_list, title="Movies", form=form)
            
    elif request.method == "GET":
        movies = FavouriteMovie.query.all()
        movie_list = [format_movie(movie) for movie in movies]
        return render_template('movies.html', movies=movie_list, title="Movies", form=form)

# GET /:id
@app.route('/movie/<id>')
def get_movie(id):
    movie = FavouriteMovie.query.filter_by(id=id).first()
    return render_template("movie.html", movie=movie)


# DELETE /:id
@app.route("/movies/<id>", methods=['DELETE'])
def delete_movie(id):
    movie = FavouriteMovie.query.filter_by(id=id).first()
    db.session.delete(movie)
    db.session.commit()
    return f"Movie {id} deleted successfully"

# PATCH /:id
@app.route("/movies/<id>", methods=["PATCH"])
def update_movie(id):
    movie = FavouriteMovie.query.filter_by(id=id)
    data = request.json
    movie.update(dict(title=data["title"], duration_minutes=data["duration_minutes"], genre=data["genre"], short_description=data["short_description"]))
    db.session.commit()
    updatedMovie = movie.first()
    return jsonify(id=updatedMovie.id, title=updatedMovie.title, duration_minutes=updatedMovie.duration_minutes, genre=updatedMovie.genre, short_description=updatedMovie.short_description)

