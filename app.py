import streamlit as st
import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader as pdfr
from groq import Groq
import os

st.title("Summariser")

st.write("Please refrain from using texts that have over 10000 chars, as any texts will be cut down to the first 10000 chars\nAlso to ensure that no error occurr please only click summerise with either url or pdf not both")
#get user iport from the app and return it as idk impout url smth like that, make it so the user can eith upload a pdf fil or a url
st.write(" ")
st.write(" ")

user_url = st.text_input("Paste your url here: ")

user_file = st.file_uploader("Upload a pdf file: ", type = ["pdf"])

def url_text_extract(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    raw_html = requests.get(url, headers = headers)
    status = raw_html.status_code
    if status == 200:
        soup = BeautifulSoup(raw_html.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.extract()
        text = soup.get_text(separator = " ", strip = True)
        text = text[:10000]
        #return the pretty text
        
        return text
    else:
        st.write(f"Error: {status}")
        return None


def pdf_text_extract(pdf):
    reader = pdfr(pdf)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() or ""
    #return the pretty text
    full_text = full_text[:10000]
    return full_text

#AI API
AI = os.environ["GROQ_API_KEY"]
api = Groq(api_key =AI)

#summarise the text
def ai_summarise(text):
    ai_summariser = api.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "summarise this text"
            },
            {
                "role": "user",
                "content": text
            }
        ] 
    ) 
    return ai_summariser.choices[0].message.content

if st.button("Summarise"):

    if user_url:
        url_text = url_text_extract(user_url)
        if url_text:
            summary = ai_summarise(url_text)
            st.markdown("Summary")
            st.write(summary)
        elif url_text == None:
            url_error_message = "Error: invalid URL"
    elif user_file:
        pdf_text = pdf_text_extract(user_file)
        summary = ai_summarise(pdf_text)
        st.markdown("Summary")
        st.write(summary)
    else:
        st.write("Error with summary")


#if input url disable the put here your pdf file 
#elif inout is a pdf file disable the url function

#print the summarisation 

#have a run again button so that it restets the whole thing and the user can run ts again(or will that take to much time?)