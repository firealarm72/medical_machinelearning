import urllib.request
import re
import xml.etree.ElementTree as ET
import csv

f1 = open("pubmed_journal_title.txt",'w', encoding='utf-8')
f2 = open("pubmed_authors.csv",'w',encoding="utf-8",newline='')
f3 = open("pubmed_pubyear.txt",'w')
f4 = open("pubmed_title.txt",'w',encoding="utf-8")
f5 = open("pubmed_abstract.txt",'w',encoding="utf-8")

#serach keyword for articles containing 'emotions' and 'skin conductance'
term ="(emotions)%20AND%20skin%20conductance"
url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=xml&retmax=100000&term=%s&mindate=1950&maxdate=2018'%(term)
handle = urllib.request.urlopen(url)
data = handle.read() #read xml files corresponds to the conditions above

#find id string in between id tags
id_string = re.findall(r'<Id>(\d*?)</Id>\\n\\t', str(data))
i = 0 #id index

for id in id_string:
    crawl_url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?&db=pubmed&retmode=xml&id=%s"%(id)
    crawl_handle = urllib.request.urlopen(crawl_url)
    crawl_data = crawl_handle.read() #xml file corresponding to the id
    root = ET.fromstring(crawl_data) #root of the element tree

    #journal where the article is published
    journal_title = root.find("PubmedArticle").find("MedlineCitation").find("Article").find("Journal").findtext("Title")+"\n"

    #date when the journal is published
    pubdate = root.find("PubmedArticle").find("MedlineCitation").find("Article").find("Journal").find("JournalIssue").find("PubDate")

    if pubdate.findtext("Year") is not None:
        date = pubdate.findtext("Year") + "\n"
    elif pubdate.findtext("MedlineDate") is not None:
        date = pubdate.findtext("MedlineDate").split(' ')[0]

    #authors of the articles
    author_list=root.find("PubmedArticle").find("MedlineCitation").find("Article").find("AuthorList")
    authors = []

    for author in root.iter("Author"):
        authors.append(author.findtext("LastName")+' ' + author.findtext("ForeName"))


    title=root.find("PubmedArticle").find("MedlineCitation").find("Article").findtext("ArticleTitle") + ' '

    abstract=""
    abs= root.find("PubmedArticle").find("MedlineCitation").find("Article").find("Abstract")
    if abs is not None:
        for abs in abs.iter("AbstractText"):
            if abs.text is not None:
                abstract += abs.text
                abstract +=' '

    f1.write(journal_title)

    wr2 = csv.writer(f2)
    wr2.writerow(authors)

    f3.write(date)

    f4.write(title)

    f5.write(abstract)


    i+=1
    if i % 50==0:
        print("%dth ID\n"%i)


f1.close()
f2.close()
f3.close()
f4.close()
f5.close()

