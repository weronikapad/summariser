import streamlit as st

st.title("Summariser")

#get user iport from the app and return it as idk impout url smth like that, make it so the user can eith upload a pdf fil or a url

user_input = st.text_input("Paste your url here: ")

user_file = st.file_uploader("Upload a pdf file: ", type = ["pdf"])

print(user_input)
#if input url disable the put here your pdf file 
#elif inout is a pdf file disable the url function

#print the summarisation 

#have a run again button so that it restets the whole thing and the user can run ts again(or will that take to much time?)