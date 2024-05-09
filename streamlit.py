import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title('Movie Recommender System')
option = st.selectbox(
    'Choose a movie...',
    movies['title'].values
)

def recommend(movie):
    idx = movies[movies['title'] == movie].index[0]
    movie_list = list(sorted(enumerate(similarity[idx]), reverse=True, key = lambda x: x[1]))[1:6]

    rm = []
    for i in movie_list:
        rm.append(movies.iloc[i[0]].title)
    return rm

if st.button('Recommend'):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)
