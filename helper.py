import os
import gdown
from joblib import load

os.makedirs("model", exist_ok=True)

MOVIES_URL = "https://drive.google.com/uc?id=115kMWMDIhHJ1lKdVbgaCyvICYQblVIhi"
SIMILARITY_URL = "https://drive.google.com/uc?id=1fPgBdhl_Uxiek9lGVEh5xIU6sVaZKapj"

if not os.path.exists("model/movies.joblib"):
    print("Downloading movies.joblib...")
    gdown.download(
        url=MOVIES_URL,
        output="model/movies.joblib",
        quiet=False
    )

if not os.path.exists("model/similarity_final.joblib"):
    print("Downloading similarity_final.joblib...")
    gdown.download(
        url=SIMILARITY_URL,
        output="model/similarity_final.joblib",
        quiet=False
    )

print("Loading movies...")
movies = load("model/movies.joblib")
print("Movies loaded successfully!")

print("Loading similarity...")
similarity = load("model/similarity_final.joblib")
print("Similarity loaded successfully!")

print("Movies Shape:", movies.shape)

try:
    print("Similarity Shape:", similarity.shape)
except Exception as e:
    print("Similarity Error:", e)

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