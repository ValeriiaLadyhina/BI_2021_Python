import sqlite3
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


url = 'https://www.slu.se/en/education/programmes-courses/'      # webpage of SLU with programmes
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
article = soup.find_all('article')
pattern = re.compile(r'<span class="content">.*</span>')
content = pattern.findall(str(article))
pattern = re.compile(r'<span class="headline">.*</span>')
headlines = pattern.findall(str(article))
pattern = re.compile(r'<a href=".*>')
ahref = pattern.findall(str(article))
pattern2 = re.compile(r'>.*<')
pattern_ahref = re.compile(r'/.*/')
SLU_programmes = []
for i in range(23):
    programme = pattern2.findall(headlines[i])
    content_i = pattern2.findall(content[i])
    ahref_i = pattern_ahref.findall(ahref[i])[0]
    ahref_i = ahref_i[1:-1].split('/')
    if ahref_i[3] == 'bachelors-programmes':
        type_programme = 'Bachelor'
    else:
        type_programme = 'Master'

    SLU_programmes.append([programme[0][1:-1], ahref_i[0], type_programme, 120, content_i[0][1:-1]])

connection = sqlite3.connect('SLU_english_programmes.db')
query = '''CREATE TABLE SLU_programmes(
                            id INTREGER PRIMARY KEY,
                            name TEXT,
                            language TEXT,
                            level TEXT,
                            length INTREGER,
                            question TEXT)
                            '''
connection.execute(query)
insertion_query = '''INSERT INTO 
                     SLU_programmes (name,language, level, length, question)
                     VALUES (?, ?, ?, ?, ?)
                     '''
connection.executemany(insertion_query, SLU_programmes)
connection.commit()
connection.close()
