import csv
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from collections import Counter
import nltk
nltk.download('stopwords')

#TOP 10 journals
print("==============TOP 10 JOURNALS=================")
f1 = open("test2/pubmed_journal_title.txt",'r', encoding='utf-8')
title_dict = dict()
for line in f1.readlines():
    if line in title_dict:
        title_dict[line] +=1
    else:
        title_dict[line] = 1

sort_list=sorted(title_dict, key=title_dict.get, reverse=True)

rank=0
for title in sort_list:
    rank+=1
    print("RANK %d : %s(%d)"  %(rank, title.rstrip('\n'), title_dict[title]))
    if rank==10:
        break
f1.close()

#TOP 10 authors
print("==============TOP 10 AUTHORS=================")
f2 = open("test2/pubmed_authors.csv",'r', encoding='utf-8')
rd = csv.reader(f2)
author_dict = dict()

for line in rd:
    for author in line:
        if author in author_dict:
            author_dict[author] +=1
        else:
            author_dict[author] = 1

sort_list=sorted(author_dict, key=author_dict.get, reverse=True)

rank=0
for author in sort_list:
    rank+=1
    print("RANK %d : %s(%d)"  %(rank, author,author_dict[author]))
    if rank==10:
        break
f2.close()

#HISTOGRAM

f3 = open("test2/pubmed_pubyear.txt",'r')
pubyear_list=f3.readlines()
print(pubyear_list)
list=[]
for pubyear in pubyear_list:
    year=pubyear.split('\n')[0]
    year=year[0:4]
    list.append(int(year)-int(year)%5)
plt.xlabel('year')
plt.ylabel('frequency')
plt.title('Histogram of number of paper published with 5-year intervals')
plt.hist(list)
plt.show()

f3.close()

#TOP 10 TERMS IN TITLE
print("==============TOP 10 TERMS(TITLE)=================")
f4 = open("test2/pubmed_title.txt",'r',encoding="utf-8")
tokenizer = RegexpTokenizer(r'\w+')
title_str=f4.read()
no_punc = tokenizer.tokenize(title_str)
set(w.title() for w in no_punc if w.lower() not in stopwords.words())

word_count_dict = Counter(w.title() for w in no_punc if w.lower() not in stopwords.words())
most_common_term=word_count_dict.most_common(10)
print(most_common_term)


f4.close()
#TOP 10 TERMS IN ABSTRACT
print("==============TOP 10 TERMS(ABSTRACT)=================")
f5 = open("test2/pubmed_abstract.txt",'r',encoding="utf-8")
tokenizer = RegexpTokenizer(r'\w+')
abs_str=f5.read()
no_punc = tokenizer.tokenize(abs_str)
set(w.title() for w in no_punc if w.lower() not in stopwords.words())

word_count_dict = Counter(w.title() for w in no_punc if w.lower() not in stopwords.words())
most_common_term=word_count_dict.most_common(10)
f5.close()
print(most_common_term)