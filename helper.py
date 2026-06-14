import os
import gdown
from joblib import load

# Create model folder
os.makedirs("model", exist_ok=True)

# Download movies.joblib
if not os.path.exists("model/movies.joblib"):
    gdown.download(
        "https://drive.google.com/file/d/115kMWMDIhHJ1lKdVbgaCyvICYQblVIhi/view?usp=sharing",
        "model/movies.joblib",
        fuzzy=True,
        quiet=False
    )

# Download similarity_final.joblib
if not os.path.exists("model/similarity_final.joblib"):
    gdown.download(
        "https://drive.google.com/file/d/1fPgBdhl_Uxiek9lGVEh5xIU6sVaZKapj/view?usp=sharing",
        "model/similarity_final.joblib",
        fuzzy=True,
        quiet=False
    )

movies = load("model/movies.joblib")
similarity = load("model/similarity_final.joblib")


def recommend(movie):

    movie_index = movies[
        movies['title'].str.lower() == movie.lower()
    ].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:8]

    recommendations = []

    for i in movies_list:
        recommendations.append(
            movies.iloc[i[0]].title
        )

    return recommendations