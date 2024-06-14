from flask import Flask, request, jsonify, render_template
from movies_data import CineMatch

app = Flask(__name__)
cinematch = CineMatch()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_movie_page')
def add_movie_page():
    return render_template('add_movie.html')

@app.route('/add_movie', methods=['POST'])
def add_movie():
    data = request.json
    title = data['title']
    genre = data['genre']
    cinematch.add_movie(title, genre)
    return jsonify({"message": "Movie added successfully!"})

@app.route('/search_movie_page')
def search_movie_page():
    return render_template('search_movie.html')

@app.route('/search_movie', methods=['GET'])
def search_movie():
    query = request.args.get('query')
    search_type = request.args.get('type')
    if search_type == 'title':
        results = cinematch.search_by_title(query)
    elif search_type == 'genre':
        results = cinematch.search_by_genre(query)
    else:
        return jsonify({"error": "Invalid search type."}), 400
    return jsonify(results)

@app.route('/recommend_movies_page')
def recommend_movies_page():
    return render_template('recommend_movies.html')

@app.route('/recommend_movies', methods=['GET'])
def recommend_movies():
    n = int(request.args.get('n'))
    recommendations = cinematch.recommend_top_n(n)
    return jsonify(recommendations)

@app.route('/delete_movie_page')
def delete_movie_page():
    return render_template('delete_movie.html')

@app.route('/delete_movie', methods=['POST'])
def delete_movie():
    data = request.json
    title = data['title']
    cinematch.delete_movie(title)
    return jsonify({"message": "Movie deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
