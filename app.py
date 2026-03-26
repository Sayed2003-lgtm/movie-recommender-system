import streamlit as st
import pickle
import pandas as pd
import os

# Poster dictionary (manual)
poster_dict = {
    "Avatar": "https://image.tmdb.org/t/p/w500/6EiRUJpuoeQPghrs3YNktfnqOVh.jpg",
    "Spider-Man": os.path.join("img", "spider_man", "spiderman.png"),
    "Spider-Man 2": os.path.join("img", "spider_man", "Screenshot (188).png"),
    "The Amazing Spider-Man": os.path.join("img", "spider_man", "theAmazingSpiderMan.png"),
    "The Amazing Spider-Man 2": os.path.join("img", "spider_man", "theAmazingSpiderMan2.png"),
    "The Dark Knight": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
    "Batman Begins": "https://image.tmdb.org/t/p/w500/4MpN4kIEqUjW8OPtOQJXlTdHiJV.jpg",
    "The Dark Knight Rises": "https://image.tmdb.org/t/p/w500/hr0L2aueqlP2BYUblTTjmtn0hw4.jpg",
    "Arachnophobia": os.path.join("img", "spider_man", "Aracnophobia.png")
}

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))

# Compute similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()
similarity = cosine_similarity(vectors)

# Fetch poster
def fetch_poster(movie_name):
    return poster_dict.get(movie_name, "https://dummyimage.com/300x450/000/fff&text=No+Poster")

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    names = []
    posters = []

    for i in movies_list:
        movie_name = movies.iloc[i[0]].title
        names.append(movie_name)   # 🔥 YOU MISSED THIS
        posters.append(fetch_poster(movie_name))

    return names, posters


# ---------------- UI ---------------- #

st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values,
    key="movie_select"
)

if st.button("Recommend", key="recommend_btn"):
    names, posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]

    for i in range(len(names)):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
