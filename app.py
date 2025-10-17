import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=82ae0b6471c494012fa04b09d955baf8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index= movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    recommendation_list = sorted(list(enumerate(distances)),key = lambda x:x[1] , reverse=True)[1:6]

    recommend_list=[]
    recommend_posters=[]
    for i in recommendation_list:
        movie_id = movies.iloc[i[0]].id
        
        recommend_list.append(movies.iloc[i[0]].title)
        recommend_posters.append(fetch_poster(movie_id))
    return recommend_list,recommend_posters

movies= pickle.load(open('movies.pkl','rb'))
movie_list = movies['title'].values
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender system')

movie = st.selectbox(
    'Type or select a Movie',
    movie_list
)

if st.button('recommend'):
    recommended_movie_names,recommended_movie_posters = recommend(movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
