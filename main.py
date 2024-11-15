import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

client = OpenAI(api_key=api_key)

text = """
Sztuczna inteligencja: wpĹyw i wyzwania

Sztuczna inteligencja to dziedzina nauki i technologii zajmujÄca siÄ tworzeniem maszyn i programĂłw zdolnych do wykonywania zadaĹ wymagajÄcych ludzkiej inteligencji, takich jak uczenie siÄ, rozumienie jÄzyka naturalnego i podejmowanie decyzji. AI staĹa siÄ integralnÄ czÄĹciÄ naszego codziennego Ĺźycia, od asystentĂłw gĹosowych w smartfonach, jak Siri czy Google Assistant, po systemy rekomendacyjne na platformach streamingowych, takich jak Netflix czy Spotify. Wspiera nas w planowaniu tras, automatyzacji domowych urzÄdzeĹ oraz w komunikacji. Obecnie jest o niej bardzo gĹoĹno chociaĹźby za sprawÄ duĹźych modeli jÄzykowych, jak ChatGPT.

RozwĂłj uczenia maszynowego i gĹÄbokiego uczenia umoĹźliwiĹ tworzenie zaawansowanych modeli, ktĂłre potrafiÄ samodzielnie rozwiÄzywaÄ skomplikowane problemy. Sieci neuronowe analizujÄ ogromne iloĹci danych w obszarach takich jak rozpoznawanie obrazĂłw czy przetwarzanie jÄzyka naturalnego. DziÄki temu AI nie tylko przetwarza dane, ale takĹźe podejmuje decyzje, wczeĹniej zarezerwowane dla ludzi.

Wyzwania etyczne i spoĹeczne

Kluczowym wyzwaniem jest zapewnienie etycznego i odpowiedzialnego rozwoju AI. NaleĹźy zwracaÄ uwagÄ na uprzedzenia w danych treningowych, ktĂłre mogÄ prowadziÄ do dyskryminacji, oraz na wpĹyw AI na prywatnoĹÄ i nierĂłwnoĹci spoĹeczne. WaĹźne jest opracowanie ram etycznych i mechanizmĂłw nadzoru regulujÄcych rozwĂłj i wdraĹźanie AI, a takĹźe wĹÄczanie rĂłĹźnych grup spoĹecznych w ten proces. TransparentnoĹÄ dziaĹaĹ firm i instytucji moĹźe pomĂłc w budowaniu zaufania do technologii.

Badacze pracujÄ nad rozwiÄzaniami umoĹźliwiajÄcymi harmonijne wspĂłĹistnienie ludzi i AI, koncentrujÄc siÄ na tworzeniu systemĂłw wspierajÄcych czĹowieka, a nie go zastÄpujÄcych. Istotne jest opracowywanie mechanizmĂłw wspĂłĹpracy miÄdzy czĹowiekiem a maszynÄ, co sprzyja synergii i skutecznej komunikacji.

Automatyzacja i przyszĹoĹÄ rynku pracy

Automatyzacja procesĂłw dziÄki AI przynosi korzyĹci w postaci zwiÄkszonej efektywnoĹci i redukcji kosztĂłw. Jednak istniejÄ obawy dotyczÄce wpĹywu na rynek pracy i potencjalnego zastÄpienia ludzi przez maszyny. Kluczowe jest przemyĹlane podejĹcie do transformacji rynku pracy, inwestycja w edukacjÄ i przekwalifikowanie pracownikĂłw, aby mogli oni znaleĹşÄ nowe role w gospodarce przyszĹoĹci.

SpecjaliĹci powinni byÄ gotowi na ciÄgĹe doskonalenie swoich umiejÄtnoĹci, uczÄc siÄ m.in. zasad dziaĹania algorytmĂłw AI. PrzyszĹoĹÄ pracy bÄdzie wymagaÄ nie tylko umiejÄtnoĹci technicznych, ale takĹźe kompetencji miÄkkich, takich jak kreatywnoĹÄ i zdolnoĹÄ rozwiÄzywania problemĂłw.

Nasza zdolnoĹÄ do adaptacji i innowacji zdecyduje o tym, jak AI wpĹynie na przyszĹoĹÄ ludzkoĹci. WspĂłlnie moĹźemy ksztaĹtowaÄ tÄ przyszĹoĹÄ, wykorzystujÄc AI dla dobra wszystkich.

*Tekst opracowany przez AI. W Oxido nie mamy aĹź tak cukierkowego spojrzenia na sztucznÄ inteligencjÄ... ;)
"""

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": """
Prompt:
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
          "text": f"{text}"
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
print(response.choices[0].message.content)

article_html_name = "artykul.html"
article_html = response.choices[0].message.content

with open(article_html_name, "w") as plik:
    plik.write(article_html)
