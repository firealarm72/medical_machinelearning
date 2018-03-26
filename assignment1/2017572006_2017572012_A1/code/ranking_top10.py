import csv
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from collections import Counter
import nltk
nltk.download('stopwords')
"""
Read output files and print all results
1. Top 10 journals
2. Top 10 authors
3. Histogram of number of paper published with 5-year intervals
4. Top 10 words (title)
5. Top 10 words (abstract)
"""
#TOP 10 journals
print("==============TOP 10 JOURNALS=================")
#File read
f1 = open("pubmed_journal_title.txt",'r', encoding='utf-8')
title_dict = dict()
for line in f1.readlines():
    if line in title_dict:
        # count
        title_dict[line] +=1
    else:
        # If there is no key, initialize
        title_dict[line] = 1
#Sorting dictionary
sort_list=sorted(title_dict, key=title_dict.get, reverse=True)

#After Sorting, print only top 10
rank=0
for title in sort_list:
    rank+=1
    print("RANK %d : %s(%d)"  %(rank, title.rstrip('\n'), title_dict[title]))
    if rank==10:
        # After 10 loop stop
        break
f1.close()

#TOP 10 authors
print("==============TOP 10 AUTHORS=================")
#File read
f2 = open("pubmed_authors.csv",'r', encoding='utf-8')
rd = csv.reader(f2)
author_dict = dict()

for line in rd:
    for author in line:
        if author in author_dict:
            # count
            author_dict[author] +=1
        else:
            # If there is no key, initialize
            author_dict[author] = 1
# sorting
sort_list=sorted(author_dict, key=author_dict.get, reverse=True)

#print top 10
rank=0
for author in sort_list:
    rank+=1
    print("RANK %d : %s(%d)"  %(rank, author,author_dict[author]))
    if rank==10:
        break
f2.close()

#Draw HISTOGRAM (using matplot library)

f3 = open("pubmed_pubyear.txt",'r')
#File read
pubyear_list=f3.readlines()
print(pubyear_list)
list=[]
for pubyear in pubyear_list:
    year=pubyear.split('\n')[0]
    year=year[0:4] #get only year. (first 4 texts)
    list.append(int(year)-int(year)%5) #to get per 5-year interval, substract 5 mod
plt.xlabel('year') #x-axis name
plt.ylabel('frequency') # y-axis name
# graph name
plt.title('Histogram of number of paper published with 5-year intervals')
plt.hist(list)
plt.show()

f3.close()

#TOP 10 TERMS IN TITLE (using nltk library)
print("==============TOP 10 TERMS(TITLE)=================")
f4 = open("test2/pubmed_title.txt",'r',encoding="utf-8")
# Make tokenizer
tokenizer = RegexpTokenizer(r'\w+')
title_str=f4.read() # Load titles
# Put title string into tokenizer
no_punc = tokenizer.tokenize(title_str)
set(w.title() for w in no_punc if w.lower() not in stopwords.words())
word_count_dict = Counter(w.title() for w in no_punc if w.lower() not in stopwords.words())
most_common_term=word_count_dict.most_common(10)
# Print top 10 most common term
print(most_common_term)
f4.close()


#TOP 10 TERMS IN ABSTRACT (using nltk library)
print("==============TOP 10 TERMS(ABSTRACT)=================")
f5 = open("test2/pubmed_abstract.txt",'r',encoding="utf-8")
tokenizer = RegexpTokenizer(r'\w+')
abs_str=f5.read() # Load abstracts
# Put abstract string into tokenizer
no_punc = tokenizer.tokenize(abs_str)
set(w.title() for w in no_punc if w.lower() not in stopwords.words())
word_count_dict = Counter(w.title() for w in no_punc if w.lower() not in stopwords.words())
most_common_term=word_count_dict.most_common(10)
f5.close()
# Print top 10 most common term
print(most_common_term)