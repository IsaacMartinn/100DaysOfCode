from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents,"html.parser")
# print(soup.title) #Gives the whole contents
# print(soup.title.name) # Gives the name of the tag
# print(soup.title.string) # Gives the contents within the tag

# print(soup.prettify()) #Indented contents

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)


for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass

heading = soup.find(name="h1",id="name")
# print(heading)

section_heading = soup.find(name="h3",class_="heading")
# print(section_heading.getText())

company_url = soup.select_one(selector="p a")
print(company_url)