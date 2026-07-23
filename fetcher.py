from app import user_file, user_input
import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader as pdfr


#fetch user input throm UI


#check if its a valid URL


#extract the text from URL
def url_text_extract(url):
    raw_html = requests.get(url)
    status = raw_html.status_code
    if status == 200:
        soup = BeautifulSoup(raw_html, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.extract()
        text = soup.get_text(space = " ", strip = True)
        return text
    else:
        print(f"Error: {status}")


def pdf_text_extract(pdf):
    reader = pdfr(pdf)
    for page in reader.pages:
        page_text = page.extract_text()

    return page_text #i want a big wall of text 



#return the pretty text

#AI API

#summarise the text

#return text