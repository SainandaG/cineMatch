// Add Movie Form Submission
document.getElementById('add-movie-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const title = document.getElementById('title').value;
    const genre = document.getElementById('genre').value;

    fetch('/add_movie', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title, genre }),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        document.getElementById('add-movie-form').reset();
    })
    .catch(error => console.error('Error:', error));
});

// Search Movies Function
function searchMovies() {
    const query = document.getElementById('search-query').value;
    const type = document.getElementById('search-type').value;

    fetch(`/search_movie?query=${query}&type=${type}`)
    .then(response => response.json())
    .then(data => {
        const resultsDiv = document.getElementById('search-results');
        resultsDiv.innerHTML = '';
        if (data.length) {
            data.forEach(movie => {
                resultsDiv.innerHTML += `<p>Title: ${movie.title}, Genre: ${movie.genre}, Rating: ${movie.rating}</p>`;
            });
        } else {
            resultsDiv.innerHTML = '<p>No movies found.</p>';
        }
    })
    .catch(error => console.error('Error:', error));
}

// Recommend Movies Function
function recommendMovies() {
    const n = document.getElementById('top-n').value;

    fetch(`/recommend_movies?n=${n}`)
    .then(response => response.json())
    .then(data => {
        const recommendationsDiv = document.getElementById('recommendations');
        recommendationsDiv.innerHTML = '';
        if (data.length) {
            data.forEach(movie => {
                recommendationsDiv.innerHTML += `<p>Title: ${movie.title}, Genre: ${movie.genre}, Rating: ${movie.rating}</p>`;
            });
        } else {
            recommendationsDiv.innerHTML = '<p>No movies available for recommendation.</p>';
        }
    })
    .catch(error => console.error('Error:', error));
}

// Delete Movie Function
function deleteMovie() {
    const title = document.getElementById('delete-title').value;

    fetch('/delete_movie', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title }),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        document.getElementById('delete-title').value = '';
    })
    .catch(error => console.error('Error:', error));
}
