import pandas as pd
import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image
import numpy as np

st.set_page_config(
    page_title='Akku-Recommender',
    layout='wide'
)
tab1,tab2=st.tabs(['MOVIES-RECOMMENDER','BOOKS-RECOMMENDER'])
                  
with tab1:
    image=Image.open('movi.png')
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
    
    similarity = pd.read_pickle('similarity.pkl')
    movies_dict = pd.read_pickle('movie_dict.pkl')
    # with open('similarity.pkl', 'rb') as file1:
    #     similarity = pickle.load(file1)
    # with open('movie_dict.pkl', 'rb') as file2:
    #     movies_dict = pickle.load(file2)
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
    image=Image.open('bokk.png')
    edited=image.resize((3060,500))
    st.image(edited,use_column_width=True)

    st.title('Book Recommender System')
    popular_df = pd.read_pickle('popular.pkl')
    pt = pd.read_pickle('pt.pkl')
    books = pd.read_pickle('books.pkl')
    similarity_scores = pd.read_pickle('similarity_scores.pkl')
    
    book_name = list(popular_df['Book-Title'].values)
    author=list(popular_df['Book-Author'].values)
    image=list(popular_df['Image-URL-M'].values)
    votes=list(popular_df['num_ratings'].values)
    rating=list(popular_df['avg_rating'].values)
    
    selected_book_name = st.selectbox('Select your favorite book 👇', popular_df['Book-Title'].values)
    
    def recommend(book_name):
        index = np.where(pt.index==book_name)[0][0]
        similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:11]
    
        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
    
            data.append(item)
        
        return data
        
    if st.button('Recommend'):
        data = recommend(selected_book_name)
        for i in data:
            col1, col2 = st.columns([1,6])
            with col1:
                st.image(i[2])
                
            with col2:
                st.subheader(i[0])
                st.write('Author',i[1])






    # # popular_df =pickle.load(open("popular.pkl","rb"))
    # # pt =pickle.load(open("pt.pkl","rb"))
    # # books =pickle.load(open("books.pkl","rb"))
    # # similarity_scores =pickle.load(open("similarity_scores.pkl","rb"))

    # popular_df = pd.read_pickle('popular.pkl')
    # pt = pd.read_pickle('pt.pkl')
    # books = pd.read_pickle('books.pkl')
    # similarity_scores = pd.read_pickle('similarity_scores.pkl')
    
    # # with open('popular.pkl', 'rb') as file:
    # #      popular_df = pickle.load(file)
    # # with open('pt.pkl', 'rb') as filee:
    # #     pt = pickle.load(filee)
    # # with open('books.pkl', 'rb') as fileee:
    # #     books = pickle.load(fileee)
    # # with open('similarity_scores.pkl', 'rb') as fileeee:
    # #     similarity_scores = pickle.load(fileeee)

    # book_name = list(popular_df['Book-Title'].values)
    # author=list(popular_df['Book-Author'].values)
    # image=list(popular_df['Image-URL-M'].values)
    # votes=list(popular_df['num_ratings'].values)
    # rating=list(popular_df['avg_rating'].values)

    # selected_book_name = st.selectbox('Select your favorite book 👇', popular_df['Book-Title'].values)

    # def recommend(book_name):
    #     index = np.where(pt.index==book_name)[0][0]
    #     similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:11]

    #     data = []
    #     for i in similar_items:
    #         item = []
    #         temp_df = books[books['Book-Title'] == pt.index[i[0]]]
    #         item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
    #         item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
    #         item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

    #         data.append(item)

    #     return data

    # if st.button('Recommend1'):
    #     data = recommend(selected_book_name)
    #     for i in data:
    #         col1, col2 = st.columns([1,6])
    #         with col1:
    #             st.image(i[2])

    #         with col2:
    #             st.subheader(i[0])
    #             st.write('Author',i[1])
