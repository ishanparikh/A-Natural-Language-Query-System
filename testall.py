x1=[]
y1=[]
f=open("sentences.txt","r+")
for line in f:
    for i in line.split():
        x,y=i.split('|')
        x1.append(x)




function_words_tags = [('a','AR'), ('an','AR'), ('and','AND'),
     ('is','BEs'), ('are','BEp'), ('does','DOs'), ('do','DOp'),
     ('who','WHO'), ('which','WHICH'), ('Who','WHO'), ('Which','WHICH'), ('?','?')]
     # upper or lowercase tolerated at start of question.

function_words = [p[0] for p in function_words_tags]
print(function_words)
print(type(function_words))
x=function_words
y=(x.index('are'))
z=function_words_tags[y][1]
print(z)

'''
single=[]
plural=[]
with open("sentences.txt", "r") as f:
    for line in f:
        for tag_phrase in line.split():  # Splits the sentence on whitespace
            word, tag = tag_phrase.split('|')  # Splits the tagged word on '|'
            if tag == 'NN':
                single.append(word)
            elif tag == 'NNS':
                plural.append(word)
'''