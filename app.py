from sys import exit
from typing import Callable, NoReturn
from xmlrpc.server import SimpleXMLRPCDispatcher
f: Callable[..., NoReturn] = exit
import pickle
Similarity=pickle.load (open('similarity.pkl','rb'))
books_list = pickle.load(open('books.pkl','rb'))
books_gen = books_list['Genre'].values
import streamlit as st



def recommend(book):
    book_inx=books_list[books_list['Genre'] == book].index[0]
    distance = Similarity[book_inx]
    book_shell=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[0:5]
    
    
    recommended_books=[]
    for i in book_shell:
        recommended_books.append(books_list.iloc[i[0]].Title)
    return recommended_books   





st.title('Book Recommendor System')

selected_genre = st.selectbox('How would you like to be contacted?',books_gen)


if st.button('recommend'):
   ##st.write(selected_genre)
   recommendations = recommend(selected_genre)
   for i in recommendations:
         st.write(i)
        