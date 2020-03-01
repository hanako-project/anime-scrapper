from requests import Response
from bs4 import BeautifulSoup as bs


def parse_content(content: Response.content, source: str):
    print("Parsing data from {0}".format(source))
    content = bs(content, "html.parser")
    if source == "MAL":
        score = content.find("div", class_="score").get_text(strip=True)
        synopsis = content.find("span", itemprop="description").get_text(strip=True)
        return {
            "score": score,
            "synopsis": synopsis
        }
