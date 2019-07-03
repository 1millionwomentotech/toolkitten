
# coding: utf-8

# In[201]:


import nltk
from nltk.book import *


# In[202]:


#### Day 1 ####


# In[203]:


## Exercise #5 in http://www.nltk.org/book/ch01.html 
# Compare the lexical diversity scores for humor and romance fiction in 1.1. Which genre is more lexically diverse?


# In[302]:


lexical_diversity_humor = 0.231 # the number of distinct words is 23% of the total number of words.
lexical_diversity_fiction_romance = 0.121 # the number of distinct words is 12% of the total number of words.

'So the genre humor is more lexically diverse.'


# In[ ]:


## Exercise #6 in http://www.nltk.org/book/ch01.htmland 
# Produce a dispersion plot of the four main protagonists in Sense and Sensibility: Elinor, Marianne, Edward, and Willoughby. What can you observe about the different roles played by the males and females in this novel? Can you identify the couples?


# In[ ]:


print(text2.dispersion_plot(["Elinor", "Marianne", "Edward", "Willoughby"]))

'It can be seen that the female characters Elinor and Marianne appear much more frequently than the male characters. The dispersion of their apparation is quite spread out over the book.'
'Looking at the distribution, it looks like the couples are 1- Elinor and Edward, 2- Marianne and Willoughby.'


# In[ ]:


#### Day 2 ####


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('pprint', '')
import nltk
# nltk.download()
from nltk.book import *
import matplotlib.pyplot as plt

from nltk.corpus import gutenberg
from nltk.corpus import webtext
from nltk.corpus import brown
from nltk.corpus import nps_chat
from nltk.corpus import reuters
from nltk.corpus import inaugural


# In[ ]:


## Exercise: Type up the whole Chapter 2 of http://www.nltk.org/book/ch02.html


# In[ ]:


# 1.1 Gutenberg Corpus

print(gutenberg.fileids())
emma = gutenberg.words('austen-emma.txt')
len(emma)


# In[ ]:


for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print (round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)


# In[ ]:


macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
macbeth_sentences
macbeth_sentences[1116]
longest_len = max(len(s) for s in macbeth_sentences)
[s for s in macbeth_sentences if len(s) == longest_len]


# In[ ]:


# 1.2 Web and Chat Text


# In[ ]:


for fileid in webtext.fileids():
    print(fileid, webtext.raw(fileid)[:65])


# In[ ]:


chatroom = nps_chat.posts('10-19-20s_706posts.xml')
chatroom[45]


# In[ ]:


# 1.3 Brown Corpus


# In[ ]:


brown.categories()
brown.words(categories = 'news')
brown.words(fileids = ['cr06'])
brown.sents(categories = ['news', 'humor'])


# In[ ]:


news_text = brown.words(categories='news')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can','could','may','must']
for m in modals:
    print (m + " : ", fdist[m], end=' ')
# print(fdist)


# In[ ]:


cfd = nltk.ConditionalFreqDist((genre, word)
                              for genre in brown.categories()
                              for word in brown.words(categories=genre))
genres = ['humor', 'news', 'hobbies']
pronouns = ['she', 'her', 'hers', 'he', 'him', 'his', 'it', 'its', 'they', 'them', 'theirs']

cfd.tabulate(conditions=genres, samples=pronouns)


# In[ ]:


# 1.4 Reuters Corpus


# In[ ]:


reuters.fileids()
reuters.categories()
reuters.categories('training/9865')
reuters.categories(['training/9865', 'training/9880'])
reuters.fileids('barley')
reuters.fileids(['barley', 'corn'])
reuters.words('training/9865')[:14]
reuters.words(['training/9865', 'training/9880'])
reuters.words(categories='barley')
reuters.words(categories=['barley', 'corn'])


# In[ ]:


# 1.5 Inaugural Adress Corpus


# In[ ]:


inaugural.fileids()
[fileid[:4] for fileid in inaugural.fileids()]

cfd = nltk.ConditionalFreqDist(
            (target, fileid[:4])
            for fileid in inaugural.fileids()
            for w in inaugural.words(fileid)
            for target in ['america', 'citizen']
            if w.lower().startswith(target))
cfd.plot()


# In[ ]:


# 1.7 Corpora in Other Languages


# In[ ]:


nltk.corpus.cess_esp.words()
nltk.corpus.floresta.words()
nltk.corpus.indian.words('hindi.pos')
nltk.corpus.udhr.fileids()
nltk.corpus.udhr.words('Javanese-Latin1')[11:]


# In[ ]:


from nltk.corpus import udhr
languages = ['Chickasaw', 'English', 'German_Deutsch','Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
            (lang, len(word))
            for lang in languages
            for word in udhr.words(lang + '-Latin1'))
cfd.plot()


# In[ ]:


# 1.8 Text Corpus Structure

raw = gutenberg.raw("burgess-busterbrown.txt")
raw[1:20]
words = gutenberg.words("burgess-busterbrown.txt")
words[1:20]
sents = gutenberg.sents("burgess-busterbrown.txt")
sents[1:20]


# In[ ]:


# 2. Conditional Frequency Distributions
# 2.2   Counting Words by Genre


# In[ ]:


cfd = nltk.ConditionalFreqDist(
            (genre, word)
            for genre in brown.categories()
            for word in brown.words(categories=genre)
            )
genre_word = [(genre,word) for genre in ['news', 'romance'] for word in brown.words(categories=genre)]
len(genre_word)
genre_word[:4]
genre_word[-4:]

cfd = nltk.ConditionalFreqDist(genre_word)
cfd
cfd.conditions()

print(cfd['news'])
cfd['news']['expected']


# In[ ]:


# 2.3   Plotting and Tabulating Distributions


# In[ ]:


cfd = nltk.ConditionalFreqDist(
            (target, fileid[:4])
            for fileid in inaugural.fileids()
            for w in inaugural.words(fileid)
            for target in ['america', 'citizen'] 
            if w.lower().startswith(target)
            )


# In[ ]:


from nltk.corpus import udhr
languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
            (lang, len(word)) 
            for lang in languages
            for word in udhr.words(lang + '-Latin1'))

cfd.tabulate(conditions=['English', 'German_Deutsch'],samples=range(10), cumulative=True)


# In[ ]:


# 2.4   Generating Random Text with Bigrams


# In[ ]:


sent = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven','and', 'the', 'earth', '.']
list(nltk.bigrams(sent))


# In[ ]:


def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()

text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams) 
cfd['living']
generate_model(cfd, 'living')


# In[ ]:


# 3   More Python: Reusing Code


# In[ ]:


from __future__ import division
def lexical_diversity(my_text_data):
    word_count = len(my_text_data)
    vocab_size = len(set(my_text_data))
    diversity_score = vocab_size / word_count
    return diversity_score

from nltk.corpus import genesis
kjv = genesis.words('english-kjv.txt')
lexical_diversity(kjv)


# In[ ]:


def plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'

plural('fairy')
plural('woman')


# In[ ]:


from text_proc import plural
# frunctions saved another file called text_proc.py
plural('wish')
plural('fan')


# In[ ]:


# 4   Lexical Resources
# 4.1   Wordlist Corpora


# In[ ]:


def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)

unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt'))
unusual_words(nltk.corpus.nps_chat.words())


# In[ ]:


from nltk.corpus import stopwords
stopwords.words('english')

def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content) / len(text)

content_fraction(nltk.corpus.reuters.words())


# In[ ]:


puzzle_letters = nltk.FreqDist('egivrvonl')
obligatory = 'r'
puzzle_letters
wordlist = nltk.corpus.words.words()
[w for w in wordlist if len(w) >= 6 
         and obligatory in w 
         and nltk.FreqDist(w) <= puzzle_letters]


# In[ ]:


names = nltk.corpus.names
names.fileids()
male_names = names.words('male.txt')
female_names = names.words('female.txt')
[w for w in male_names if w in female_names]


# In[ ]:


cfd = nltk.ConditionalFreqDist(
    (fileid, name[-1])
    for fileid in names.fileids()
    for name in names.words(fileid))
cfd.plot()


# In[ ]:


#4.2   A Pronouncing Dictionary


# In[ ]:


entries = nltk.corpus.cmudict.entries()
len(entries)
for entry in entries[42371:42379]:
    print(entry)
    


# In[ ]:


for word, pron in entries:
    if len(pron) == 3:
        ph1, ph2, ph3 = pron
        if ph1 == 'P' and ph3 == 'T':
            print(word, ph2, end=' ')
...


# In[ ]:


syllable = ['N', 'IH0', 'K', 'S']
[word for word, pron in entries if pron[-4:] == syllable]


# In[ ]:


[w for w, pron in entries if pron[-1] == 'M' and w[-1] == 'n']
sorted(set(w[:2] for w, pron in entries if pron[0] == 'N' and w[0] != 'n'))


# In[ ]:


def stress(pron):
    return [char for phone in pron for char in phone if char.isdigit()]
[w for w, pron in entries if stress(pron) == ['0', '1', '0', '2', '0']]
[w for w, pron in entries if stress(pron) == ['0', '2', '0', '1', '0']]


# In[ ]:


p3 = [(pron[0]+'-'+pron[2], word)
      for (word, pron) in entries
      if pron[0] == 'P' and len(pron) == 3] 
cfd = nltk.ConditionalFreqDist(p3)
for template in sorted(cfd.conditions()):
    if len(cfd[template]) > 10:
        words = sorted(cfd[template])
        wordstring = ' '.join(words)
        print(template, wordstring[:70] + "...")


# In[ ]:


prondict = nltk.corpus.cmudict.dict()
prondict['fire']
# prondict['blog'] 
prondict['blog'] = [['B', 'L', 'AA1', 'G']] 
prondict['blog']


# In[ ]:


text = ['natural', 'language', 'processing']
[ph for w in text for ph in prondict[w][0]]


# In[ ]:


# 4.3   Comparative Wordlists


# In[ ]:


from nltk.corpus import swadesh
swadesh.fileids()
swadesh.words('en')


# In[ ]:


fr2en = swadesh.entries(['fr', 'en'])
fr2en
translate = dict(fr2en)
translate['chien']
translate['jeter']


# In[ ]:


de2en = swadesh.entries(['de', 'en'])    
es2en = swadesh.entries(['es', 'en']) 
translate.update(dict(de2en))
translate.update(dict(es2en))
translate['Hund']
translate['perro']


# In[ ]:


languages = ['en', 'de', 'nl', 'es', 'fr', 'pt', 'la']
for i in [139, 140, 141, 142]:
    print(swadesh.entries(languages)[i])


# In[ ]:


# 4.4   Shoebox and Toolbox Lexicons


# In[ ]:


from nltk.corpus import toolbox
toolbox.entries('rotokas.dic')


# In[ ]:


# 5   WordNet


# In[ ]:


from nltk.corpus import wordnet as wn

wn.synsets('motorcar')

wn.synset('car.n.01').lemma_names()

wn.synset('car.n.01').definition()
wn.synset('car.n.01').examples()

wn.synset('car.n.01').lemmas() 
wn.lemma('car.n.01.automobile') 
wn.lemma('car.n.01.automobile').synset() 
wn.lemma('car.n.01.automobile').name()

wn.synsets('car')
for synset in wn.synsets('car'):
    print(synset.lemma_names())

wn.lemmas('car')


# In[ ]:


# 5.2   The WordNet Hierarchy


# In[ ]:


motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
types_of_motorcar[0]
sorted(lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas())


# In[ ]:


motorcar.hypernyms()
paths = motorcar.hypernym_paths()
len(paths)
[synset.name() for synset in paths[0]]
[synset.name() for synset in paths[1]]


# In[ ]:


motorcar.root_hypernyms()


# In[ ]:


# 5.3   More Lexical Relations


# In[ ]:


wn.synset('tree.n.01').part_meronyms()
wn.synset('tree.n.01').substance_meronyms()
wn.synset('tree.n.01').member_holonyms()

for synset in wn.synsets('mint', wn.NOUN):
    print(synset.name() + ':', synset.definition())
wn.synset('mint.n.04').part_holonyms()
wn.synset('mint.n.04').substance_holonyms()

wn.synset('walk.v.01').entailments()
wn.synset('eat.v.01').entailments()
wn.synset('tease.v.03').entailments()

wn.lemma('supply.n.02.supply').antonyms()
wn.lemma('rush.v.01.rush').antonyms()
wn.lemma('horizontal.a.01.horizontal').antonyms()
wn.lemma('staccato.r.01.staccato').antonyms()


# In[ ]:


# 5.4   Semantic Similarity


# In[ ]:


right = wn.synset('right_whale.n.01')
orca = wn.synset('orca.n.01')
minke = wn.synset('minke_whale.n.01')
tortoise = wn.synset('tortoise.n.01')
novel = wn.synset('novel.n.01')
right.lowest_common_hypernyms(minke)
right.lowest_common_hypernyms(orca)
right.lowest_common_hypernyms(tortoise)
right.lowest_common_hypernyms(novel)


# In[ ]:


wn.synset('baleen_whale.n.01').min_depth()
wn.synset('whale.n.02').min_depth()
wn.synset('vertebrate.n.01').min_depth()
wn.synset('entity.n.01').min_depth()


# In[ ]:


right.path_similarity(minke)
right.path_similarity(orca)
right.path_similarity(tortoise)
right.path_similarity(novel)


# In[ ]:


## Exercise 8 of http://www.nltk.org/book/ch02.html: Define a conditional frequency distribution over the Names corpus that allows you to see which initial letters are more frequent for males vs. females (cf. 4.4).


# In[ ]:


names = nltk.corpus.names
male_names = names.words('male.txt')
female_names = names.words('female.txt')
cfd = nltk.ConditionalFreqDist(
            (fileid, name[0])
            for fileid in names.fileids()
            for name in names.words(fileid)
    )
cfd.plot()


# In[ ]:


## Exercise 10 of http://www.nltk.org/book/ch02.html: How many word types account for a third of all word tokens, for a variety of text sources? What do you conclude about this statistic?


# In[ ]:


from __future__ import division

def third_of_tokens(text):
    words_in_text = [w for w in text if any(c.isalpha() for c in w)]

    fd = nltk.FreqDist(words_in_text)
    most = fd.most_common(1000)
    
    count = 0
    third_words = []

    for word, num in most:
        if ((count < (len(words_in_text) / 3)) and any(c.isalpha() for c in word)):
            count = count + num
            third_words.append(word)
    print (third_words)        
    print (len(third_words))

def third_of_tokens_corpus(corpus):
    for fileid in corpus.fileids():
        print (fileid, third_of_tokens(corpus.words(fileid)))

third_of_tokens_corpus(gutenberg)


# In[205]:


third_of_tokens_corpus(webtext)


# In[206]:


third_of_tokens_corpus(nps_chat)


# In[ ]:


"Statistics roughly accurate!"


# In[ ]:


# Reminders to myself:
# distinct words = "word types"
# A word "token" is a particular appearance of a given word in a text; a word "type" is the unique form of the word as a particular sequence of letters. We count word tokens using len(text) and word types using len(set(text)).
# We obtain the vocabulary of a text t using sorted(set(t)).
# We operate on each item of a text using [f(x) for x in text].
# To derive the vocabulary, collapsing case distinctions and ignoring punctuation, we can write set(w.lower() for w in text if w.isalpha())


# In[ ]:


#### Day 3 ####


# In[ ]:


## Exercise: Do research to see what Python libraries are already in existence that you could start using in your day-job, or daily life.


# In[113]:


"I'm currently working on Virtual Reality projects and it looks like PyGame would be very useful: "
"It is a set of Python modules designed for writing games, written on top of SDL library" 
"It allows to create fully featured games and multimedia programs in the python language."
"It is the most popular, and portable game library for python, with over 1000 free and open source projects that use pygame to look at."


# In[ ]:


## Exercise 5 ☼ Investigate the holonym-meronym relations for some nouns. Remember that there are three kinds of holonym-meronym relation, so you need to use: member_meronyms(), part_meronyms(), substance_meronyms(), member_holonyms(), part_holonyms(), and substance_holonyms().


# In[ ]:


from nltk.corpus import wordnet as wn


# In[135]:


wn.synsets('airplane')
wn.synset('airplane.n.01').member_meronyms()
wn.synset('airplane.n.01').part_meronyms()
wn.synset('airplane.n.01').substance_meronyms()
wn.synset('airplane.n.01').member_holonyms() 
wn.synset('airplane.n.01').part_holonyms()
wn.synset('airplane.n.01').substance_holonyms()

wn.synsets('wood')
wn.synset('wood.n.01').member_meronyms()
wn.synset('wood.n.01').part_meronyms()
wn.synset('wood.n.01').substance_meronyms()
wn.synset('wood.n.01').member_holonyms() 
wn.synset('wood.n.01').part_holonyms()
wn.synset('wood.n.01').substance_holonyms()

def relations(noun):
    noun_synset = wn.synset(noun)
    print ('Member Meronyms: ', noun_synset.member_meronyms() , 
           '\nPart Meronyms: ', noun_synset.part_meronyms() ,
           '\nSubstance Meronyms: ' , noun_synset.substance_meronyms() , 
           '\nMember Holonyms: ' , noun_synset.member_holonyms() ,
           '\nPart Holonyms: ' , noun_synset.part_holonyms() , 
           '\nSubstance Holonyms: ' , noun_synset.substance_holonyms())

relations('wood.n.01')


# In[46]:


## Exercise 13 ◑ What percentage of noun synsets have no hyponyms? You can get all noun synsets using wn.all_synsets('n')


# In[77]:


nouns = list(wn.all_synsets('n'))
# print(nouns[:20])
no_hyp_noun = []
for noun in nouns:
    if noun.hyponyms() == []:
        no_hyp_noun.append(noun)
print(no_hyp_noun[:20])
print(len(no_hyp_noun))

percentage = (len(no_hyp_noun)/len(nouns))*100
print('The percentage of noun synsets with no hyponyms is ' + str(percentage) + ' %')


# In[79]:


wn.synset('cup.n.01').hyponyms()
# wn.synset('cakewalk.n.02').hyponyms()


# In[78]:


## Exercise 14 ◑ Define a function supergloss(s) that takes a synset s as its argument and returns a string consisting of the concatenation of the definition of s, and the definitions of all the hypernyms and hyponyms of s.


# In[110]:


def supergloss(s):
    synset = (s.name(),s.definition())
    hypernyms_list = list(s.hypernyms())
    hyponyms_list = list(s.hyponyms())
    
    hypernyms = [(word.name(), word.definition()) for word in hypernyms_list]
    hyponyms = [(word.name(), word.definition()) for word in hyponyms_list]

    definitions = "synset: " , synset , " hypernyms: "  , hypernyms , " hoponyms: " , hyponyms
                  
    return (definitions)

supergloss(wn.synset('cup.n.01'))


# In[ ]:


#### Day 4 ####


# In[ ]:


## Exercise 6-10 from http://www.nltk.org/book/ch03.html


# In[ ]:


## Exercise 6: Describe the class of strings matched by the following regular expressions.
# [a-zA-Z]+
# [A-Z][a-z]*
# p[aeiou]{,2}t
# \d+(\.\d+)?
# ([^aeiou][aeiou][^aeiou])*
# \w+|[^\w\s]+
# Test your answers using nltk.re_show().


# In[222]:


import nltk, re, pprint
from nltk import word_tokenize


# In[231]:


'[a-zA-Z]+ : strings containing one or more letters (capital or not)'
nltk.re_show(r'[a-zA-Z]+', 'Whole World')


# In[233]:


'[A-Z][a-z]* : one capital letter and zero or more lowercase letters' 
nltk.re_show(r'[A-Z][a-z]*', 'Whole world')


# In[234]:


'p[aeiou]{,2}t : starts with p, followed by 0 up to 2 vowels (aeiou), end with t '
nltk.re_show(r'p[aeiou]{,2}t', 'This is a pet which likes to party')


# In[240]:


'\d+(\.\d+)? : an integer or decimal number'
nltk.re_show(r'\d+(\.\d+)?', 'the result is 0.24 or maybe 65')


# In[241]:


'([^aeiou][aeiou][^aeiou])* : '
'zero or more of the following sequence: non vowel, vowel, non-vowel'
nltk.re_show(r'([^aeiou][aeiou][^aeiou])*', 'My magic keyboard is writing things by itself')


# In[242]:


'\w+|[^\w\s]+ : '
'zero or one of any alphanumeric characters or zero or one of any characters that are neither alphanumeric nor whitespace'
nltk.re_show(r'\w+|[^\w\s]+', 'My magic keyboard is writing things by itself')


# In[ ]:


## Exercise 7: Write regular expressions to match the following classes of strings:
# a. A single determiner (assume that a, an, and the are the only determiners).
# b. An arithmetic expression using integers, addition, and multiplication, such as 2*3+8.


# In[ ]:


# a.
'^(a|an|the)$'


# In[ ]:


# b.
'\d+([\+\*]\d+)+'


# In[ ]:


## Exercise 8: Write a utility function that takes a URL as its argument, 
# and returns the contents of the URL, with all HTML markup removed. 
# Use from urllib import request and then  request.urlopen('http://nltk.org/').read().decode('utf8') 
# to access the contents of the URL.


# In[245]:


from urllib import request
from bs4 import BeautifulSoup


# In[249]:


def get_content(URL):
    html = request.urlopen(URL).read().decode('utf8')
    return BeautifulSoup(html).get_text()
    
print(get_content('http://nltk.org/'))


# In[ ]:


## Exercise 9: Save some text into a file corpus.txt. Define a function load(f) that reads from the file named 
# in its sole argument, and returns a string containing the text of the file.

# Use nltk.regexp_tokenize() to create a tokenizer that tokenizes the various kinds of punctuation in this text. Use one multi-line regular expression, with inline comments, using the verbose flag (?x).
# Use nltk.regexp_tokenize() to create a tokenizer that tokenizes the following kinds of expression: monetary amounts; dates; names of people and organizations.


# In[278]:


file = open('corpus.txt')

def load(f):
    return f.read()

text = load(file)

print (text)


# In[ ]:


# Use nltk.regexp_tokenize() to create a tokenizer that tokenizes the various kinds of punctuation in this text. 
# Use one multi-line regular expression, with inline comments, using the verbose flag (?x).


# In[277]:


pattern = r'''(?x)
    [\.,;"'?\(\):\-_`\[\]\{\}]+ # one or more punctuation symbols, brackets etc.
'''
print(nltk.regexp_tokenize(text, pattern))


# In[ ]:


# Use nltk.regexp_tokenize() to create a tokenizer that tokenizes the following kinds of expression: monetary amounts; 
# dates; names of people and organizations.


# In[300]:


pattern2 = r'''(?x)
    \£\s?(?:\d+\.)?\d+                  # Monetary ex. £5
    | \d{2}\-\d{2}\-\d{4}               # Date ex. 01-08-2018
    | \d{1,2}\s[A-Z][a-z]{2,8}\s\d{4}   # Date ex. 1 August 2018
    | ([A-Z][a-z]*\s[A-Z][a-z]*)        # Names
'''

# Test 
test = 'Monetary example is £10 or $2.20, date example is or 01-08-2018 or 1 August 2018 and name example is Laure or United Kingdom'
print (nltk.regexp_tokenize(test, pattern))


# In[301]:


print(nltk.regexp_tokenize(text, pattern2))


# In[ ]:


## Exercise 10: Rewrite the following loop as a list comprehension:

 	
# >>> sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
# >>> result = []
# >>> for word in sent:
# ...     word_len = (word, len(word))
# ...     result.append(word_len)
# >>> result
# [('The', 3), ('dog', 3), ('gave', 4), ('John', 4), ('the', 3), ('newspaper', 9)]


# In[261]:


print(list((w, str(len(w))) for w in ['The', 'dog', 'gave', 'John', 'the', 'newspaper']))

