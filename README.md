 Movie Recommender System
 Live Demo

 https://movie-recommender-system-fyjhaghwkcnw3uprppwri.streamlit.app

 Overview

This project is a content-based movie recommendation system that suggests similar movies based on user selection.
It analyzes movie metadata and uses cosine similarity to recommend the most relevant movies.

 Features

 Select any movie from the dropdown
 Get top 5 similar movie recommendations
 Fast and responsive UI
 Fully deployed web application
 Tech Stack

Python
Pandas & NumPy
Scikit-learn
Streamlit

 How It Works

Movie data is preprocessed and combined into a tags column
Text data is converted into numerical vectors using CountVectorizer
Similarity between movies is calculated using cosine similarity
Top similar movies are recommended based on similarity scores
