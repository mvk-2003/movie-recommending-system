import re
from thefuzz import fuzz
from collections import Counter
import os

file_path = os.path.abspath(r"recommendation/site/Telugu.csv")
file = open(file_path, encoding='utf8')
info = file.read()
info = info.replace('\n','\t')
info = info.split('\t')
titles,years,directors,synopsis,cast,studios,countries,origins,languages,genres,themes = [],[],[],[],[],[],[],[],[],[],[]

for i in range(int(len(info)/11)):
    text = re.sub(r'[^a-zA-Z0-9\s]', '', info[i*11])       # removing all special characters from title including comma
    titles.append(text.lower())
    years.append(info[i*11+1])
    text = re.sub(r'[^a-zA-Z0-9\s]', '', info[i*11+2])
    directors.append(text.lower())
    text = info[i*11+3]
    synopsis.append(text.lower())
    text = re.sub(r'[^a-zA-Z0-9,\s]', '', info[i*11+4])         # excluding comma
    cast.append(text.lower())
    text = re.sub(r'[^a-zA-Z0-9\s]', '', info[i*11+5])
    studios.append(text.lower())
    text = re.sub(r'[^a-zA-Z0-9\s]', '', info[i*11+6])
    countries.append(text.lower())
    text = re.sub(r'[^a-zA-Z0-9\s]', '', info[i*11+7])
    origins.append(text.lower())
    text = re.sub(r'[^a-zA-Z0-9\s]', '', info[i*11+8])
    languages.append(text.lower())
    text = re.sub(r'[^a-zA-Z0-9\s]', '', info[i*11+9])
    genres.append(text.lower())
    text = re.sub(r'[^a-zA-Z0-9\s]', '', info[i*11+10])
    themes.append(text.lower())

def Input(prompt):
    prompt = re.sub(r'[^a-zA-Z0-9\s]', '', prompt)
    prompt = prompt.lower()
    prompt = prompt.split(' ')
    return prompt

def genre_out(prompt):
    index = []
    if(prompt!=[]): 
        for i in range(len(genres)):
            genre = genres[i].split(' ')
            for p in prompt:
                for g in genre:
                    if(p==g):
                        index.append(i)
    return index

def title_out(prompt):
    index = []
    if(prompt != ''):
        filtered_prompt = Input(prompt)
        for i in range(len(titles)):   
            names = titles[i].split(' ')                                # splitting every word in title 
            for p in filtered_prompt:
                for n in names:
                    if(fuzz.ratio(p,n)>=85):
                        index.append(i)                   # adding every index for every word in prompt
    return index

def year_out(prompt):
    index = []
    if(prompt != ''):
        for i in range(len(years)):
            if(prompt==years[i]):
                index.append(i)
    return index

def direc_out(prompt):
    index = []
    if(prompt!=''):
        filtered_prompt = Input(prompt)
        for i in range(len(directors)):
            direc = directors[i].split(' ')
            for p in filtered_prompt:
                for d in direc:
                    if(fuzz.ratio(p,d)>=90):
                        index.append(i)
    return index
    
def cast_out(prompt):
    index = []
    if(prompt!=''):
        filtered_prompt = Input(prompt)
        for i in range(len(cast)):
            actor = cast[i].split(' ')
            for p in filtered_prompt:
                for a in actor:
                    if(fuzz.ratio(p,a)>=90):
                        index.append(i)
    return index
    
def theme_out(prompt):
    index = []
    if(prompt!=''):
        filtered_prompt = Input(prompt)
        for i in range(len(themes)):
            theme = themes[i].split(' ')
            for p in filtered_prompt:
                for t in theme:
                    if(fuzz.ratio(p,t)>=95):
                        index.append(i)
    return index
    
def studio_out(prompt):
    index = []
    if(prompt!=''):
        filtered_prompt = Input(prompt)
        for i in range(len(studios)):
            studio = studios[i].split(' ')
            for p in filtered_prompt:
                for s in studio:
                    if(fuzz.ratio(p,s)>=90):
                        index.append(i)
    return index
    
def index(g,d,a,y,s,t):
    i1 = genre_out(g)
    i2 = direc_out(d)
    i3 = cast_out(a)
    i4 = year_out(y)
    i5 = studio_out(s)
    i6 = theme_out(t)
    index = i1+i2+i3+i4+i5+i6
    return index

def out(g,d,a,y,s,t):
    output = []
    ind = index(g,d,a,y,s,t)
    f = dict(Counter(ind))                 # checking frequency
    sorted_index = sorted(f.items(), key = lambda x:x[1], reverse = True)      # sorting in decreasing order of frequency
    f.clear()
    for key, value in sorted_index:                                      # updating dict to sorted one because sorted_index returns tuple
        f[key] = value
    sorted_index = list(f.keys())
    if(len(sorted_index)==0):
        return output
    else:
        for i in sorted_index:
            l = []
            for j in range(i*11,i*11+11):
                l.append(info[j])
            output.append(l)
        return output
