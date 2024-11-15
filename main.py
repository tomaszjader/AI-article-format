import os
from openai import OpenAI
from dotenv import load_dotenv
import requests
load_dotenv()

api_key = os.getenv("API_KEY")
client = OpenAI(api_key=api_key)
    
def download_file(url):
    
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Error downloading the file. Status: {response.status_code}")
        return None



def generate_html_from_text(text):
    

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": """
                                    You will receive a text that you need to format into structured HTML. Follow these steps for formatting:

Extract the title from the text and wrap it in an <h1> tag at the top of the HTML.
Divide the remaining text into sections, where each paragraph group begins with a descriptive <h2> tag summarizing its content. The <h2> headers should be generated based on the topic of the following paragraph(s).
Wrap each paragraph in a <p> tag.
After each paragraph, insert an HTML <figure> element that contains:
An <img> tag with the following attributes:
src="image_placeholder.jpg".
alt attribute that describes how to generate the corresponding image based on the content of the paragraph (this should be a prompt for an image generation system, like DALL·E).
A <figcaption> tag that contains a brief description of what the image is depicting in the context of the paragraph.
Return only the formatted HTML code, with no additional comments or formatting like "```html". Ensure the HTML is valid and ready for use, including using the <figure> element for images, with the appropriate alt descriptions and captions.

                                """
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": text
                    }
                ]
            }
        ],
        temperature=1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        response_format={
            "type": "text"
        }
    )

    article_html = response.choices[0].message.content

    article_html_name = "artykul.html"
    with open(article_html_name, "w") as file:
        file.write(article_html)

    return article_html_name


url = "https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt"



file_content = download_file(url)

if file_content:
    print(file_content)
    generate_html_from_text(file_content)