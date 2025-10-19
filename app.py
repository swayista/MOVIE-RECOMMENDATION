import streamlit as st
import pickle
import pandas as pd

# Load your data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Define recommendation function
def recommend(movie):
    movie_index = movies[movies['original_title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].original_title)
    return recommended_movies

# Streamlit UI
st.title('🎥 Movie Recommendation System')
print(movies.columns)
selected_movie = st.selectbox(
    'Type or select a movie from the dropdown:',
    movies['original_title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    st.write("**You might also like:**")
    for rec in recommendations:
        st.write(f"👉 {rec}")





