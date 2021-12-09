import re
import urllib
import matplotlib.pyplot as plt
link = 'https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/2430AD'

def read_url(link):
    with urllib.request.urlopen(link) as file:
        text = (str(file.read()).strip()).strip()


def find_numbers(text):
    pattern_numbers = re.compile('\d')
    numbers = pattern_numbers.findall(text)
    print('In the text', len(numbres), 'numbers were found:', *numbers)
    print(*numbers)

read_url(link)
find_numbers(text)









