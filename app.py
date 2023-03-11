import pandas as pd
import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image

st.set_page_config(
    page_title='Akku-Dashboard',
    layout='wide'
)
tab1,tab2=st.tabs(['MOVIES-RECOMMENDER','BOOKS-RECOMMENDER'])
                  
with tab1:
    image=Image.open('movi.jpg')
    edited=image.resize((3060,500))
    st.image(edited,use_column_width=True)
    
    def fetch_poster(movie_id):
       response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
       data = response.json()
       return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

    def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:16]
        recommend_movies=[]
        recommend_movies_posters = []
        for i in movies_list:
            recommend_movies.append(movies.iloc[i[0]].title)
            movie_id = movies.iloc[i[0]].movie_id
            recommend_movies_posters.append(fetch_poster(movie_id))
        return recommend_movies,recommend_movies_posters
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    st.title("Movie Recommender System")

    selected_movie_name = st.selectbox('would you like to watch movie related to ', movies['title'].values)

    if st.button('Recommend'):
        names, posters = recommend(selected_movie_name)

        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.header(names[0])
            st.image(posters[0])
        with col2:
            st.header(names[1])
            st.image(posters[1])
        with col3:
            st.header(names[2])
            st.image(posters[2])
        with col4:
            st.header(names[3])
            st.image(posters[3])
        with col5:
            st.header(names[4])
            st.image(posters[4])

        c1,c2,c3,c4,c5 = st.columns(5)
        with c1:
            st.header(names[5])
            st.image(posters[5])
        with c2:
            st.header(names[6])
            st.image(posters[6])
        with c3:
            st.header(names[7])
            st.image(posters[7])
        with c4:
            st.header(names[8])
            st.image(posters[8])
        with c5:
            st.header(names[9])
            st.image(posters[9])   

        cc1,cc2,cc3,cc4,cc5 = st.columns(5)
        with cc1:
            st.header(names[10])
            st.image(posters[10])
        with cc2:
            st.header(names[11])
            st.image(posters[11])
        with cc3:
            st.header(names[12])
            st.image(posters[12])
        with cc4:
            st.header(names[13])
            st.image(posters[13])
        with cc5:
            st.header(names[14])
            st.image(posters[14])
with tab2:
    image=Image.open('bokk.jpg')
    edited=image.resize((3060,500))
    st.image(edited,use_column_width=True)
