import requests

url = ""
if url == "":
    print("Url vide. Modifier le script est ajouté une url à scraper")
    exit(1)
    
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0"
response = requests.get(
    url, headers={"User-Agent": user_agent, "Content-type": "text/html; charset=utf-8"}
)


# with open("raw.html", "wb") as f:
#     f.write(response.content)

# html_content = ""
# with open("raw.html", 'r', encoding="utf-8") as file:
#     html_content = file.read()

html_content = response.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

categories = soup.select('.newsPost .content > div')

changes_by_category = {}

for category in categories:
    if "id" not in category.attrs:
        continue
    
    category_name = category.attrs["id"]
    changes = []
    for li in category.select("li"):
        changes.append(li.get_text().strip("\n"))

    changes_by_category[category_name] = list(changes)


for change_category, change_list in changes_by_category.items():
    print(change_category)
    for change in change_list:
        print(change)
