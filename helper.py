from joblib import load

movies = load("model/movies_small.joblib")
similarity = load("model/similarity_small.joblib")


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