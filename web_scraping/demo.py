import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com/videos/python-web-scraping-tutorial-in-hindi"

r = requests.get(url)

# htmlContent = r.content
# print(htmlContent)

# htmlText = r.text
# print(htmlText)

soup = BeautifulSoup(r.content , 'html.parser')
# print(soup.prettify())


title = soup.title
#find title
# print(title)   

#find paragraphs
# print(soup.find('p'))
# print(soup.find_all('p'))

#find paragraphs using class name
# print(soup.find('p')['class'])
# print(soup.find_all('p', class_='lead'))
# print(soup.find_all(class_='code-toolbar'))

#find using id
# print(soup.find(id='search-toggle'))

#find all links/anchor tags

# print(soup.find_all('a'))


# paras = soup.find_all('p')
# for i in paras:
#     print(i.get('href'))

html = '''
<body>
    <ul>
        <li>This1</li>
        <li><a>This2</a>This3</li>
        <li>This4</li>
        <li>This5</li>
        <li id="li">This6</li>
        <li>    This7    </li>
    </ul>
</body>
'''

soup = BeautifulSoup(html, 'html.parser')
# ul = soup.find('ul')
# print(ul.contents)

#to fetch children

# for i in ul.children:
#     print(i)

#to fetch parent

# print(ul.parent)    

#to fetch parents's parent
# print(ul.parent.parent) 

ul = soup.find(id = "li")
# print(ul.next_sibling.next_sibling)

# for j in ul.next_sibling:
#     print(j)

# for i in ul.previous_sibling:
#     print(i)    

# print(ul.previous_sibling.previous_sibling)    

ul = soup.find(id="li")
elem = ul.next_sibling.next_sibling
print(elem)
for i in elem.stripped_strings:
    print(i)