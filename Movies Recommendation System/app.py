import pickle
import streamlit as st
import requests
import pandas as pd


def recommend(movie):
    movie_index = new_data[new_data["title"]==movie].index[0]
    distance=similarity[movie_index]
    movie_list=sorted( list (enumerate(distance)),reverse=True, key=lambda x: x[1])[1:6]
    for i in movie_list:
       print(new_data.iloc[i[0]].title)
    
    distance=similarity[movie_index]
    movie_list=sorted( list (enumerate(distance)),reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies_dict=[]
    for i in movie_list:
        recommend_movies_dict.append(new_data.iloc[i[0]].title)
        return recommend_movies_dict 


  
movie_list=pickle.load(open("movies_dict.pkl","rb"))
similarity=movie_list=pickle.load(open("similarity.pkl","rb"))
new_data=pd.DataFrame(movie_list)

st.title("Movie Recommender System")

selected_movies_names=st.selectbox(
    "Type or select a movie from the dropdown",
    new_data["title"].values
)

if st.button('Show Recommendation'):
    recommendations=recommend(new_data)
    for i in recommendations:
        st.write(i)




