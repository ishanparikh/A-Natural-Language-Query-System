# File: pos_tagging.py
# Template file for Informatics 2A Assignment 2:
# 'A Natural Language Query System in Python/NLTK'

# John Longley, November 2012
# Revised November 2013 and November 2014 with help from Nikolay Bogoychev
# Revised November 2015 by Toms Bergmanis


# PART B: POS tagging

from statements import *

# The list_of_tags we shall use is:
# P  A  Ns  Np  Is  Ip  Ts  Tp  BEs  BEp  DOs  DOp  AR  AND  WHO  WHICH  ?

# Tags for words playing a special role in the grammar:

function_words_tags = [('a','AR'), ('an','AR'), ('and','AND'),
     ('is','BEs'), ('are','BEp'), ('does','DOs'), ('do','DOp'),
     ('who','WHO'), ('which','WHICH'), ('Who','WHO'), ('Which','WHICH'), ('?','?')]
     # upper or lowercase tolerated at start of question.

function_words = [p[0] for p in function_words_tags]

def unchanging_plurals():
    single = []
    plural = []
    unchanged = []
    with open("sentences.txt", "r") as f:
        for line in f:
            for tag_phrase in line.split():        #Splits the sentence on whitespace
                word, tag = tag_phrase.split('|')  #Splits the tagged word on '|'
                if tag == 'NNS':
                    plural.append(word)
                elif tag == 'NN':
                    single.append(word)
    for i in single:
        if i in plural:      #If tagged as both and not in output
            if i not in unchanged:

                unchanged.append(i)
    return unchanged



unchanging_plurals_list = unchanging_plurals()

def noun_stem (s):
    """extracts the stem from a plural noun, or returns empty string"""
    # add code here


    stem=" "


    if re.match ("[a-z]*[aeiou]ys$", s):
            stem = s[:-1]

    elif re.match ("[a-z]+[^aeiou]ies$", s) and len(s) >= 3:
            stem = s[:-3] + "y"

    elif re.match ("[a-z]*men",s):
            stem = s[:-3] + "man"

    elif s== "sheep" or s== "buffalo":      #LOOK BACK HERE
        if s not in unchanging_plurals_list:
            unchanging_plurals_list.append(s)
        return s

    elif re.match ("[^aeiou]ies$", s):
            stem = s[:-1]

    elif re.match ("[a-z]*[ox]es$", s) or s[-4:] == "ches" or s[-4:] == "shes" or s[-4:] == "sses" or s[-4:] == "zzes":
            stem = s[:-2]

    elif (re.match ("[a-z]*ses$", s) or re.match("[a-z]*zes$", s)) and s[-3:] != "sses" and s[-3:] != "zzes":
            stem = s[:-1]

    elif re.match ("[a-z]*[^iosxz]es$", s) and s[-4:-2] != 'ch' and s[-4:-2] != 'sh':
            stem = s[:-1]
    else:
            stem = ""
    return stem





def tag_word (lx,wd):
    """returns a list of all possible tags for wd relative to lx"""
    # add code here

    list_of_tags = ["P", "A"]
    list_of_tag_verbs = ["I", "T"]
    tag_list=[]


    if wd in function_words:
        find_tag=function_words.index(wd)
        tag_list.append(function_words_tags[find_tag][1])

    for tag in list_of_tags:
        if wd in lx.getAll(tag):
                tag_list.append(tag)


    if wd in lx.getAll("N"):
        if wd in unchanging_plurals_list:
            tag_list += ["Ns", "Np"]
        elif noun_stem(wd) == '':
            tag_list.append("Ns")
        else:
            tag_list.append("Np")
    if noun_stem(wd) in lx.getAll("N"):
        tag_list.append("Np")
    for i in lx.getAll("N"):
        if noun_stem(i) == wd:
            tag_list.append("Ns")
            break

    for tag in list_of_tag_verbs:
        if wd in lx.getAll(tag):
            if verb_stem(wd) == '':
                tag_list.append(tag + "p")
            else:
                tag_list.append(tag + "s")
        if verb_stem(wd) in lx.getAll(tag):
            tag_list.append(tag + "s")
        for i in lx.getAll(tag):
            if verb_stem(i) == wd:
                tag_list.append(tag + "p")
                break


    tag_list = list(set(tag_list))
    return tag_list



def tag_words (lx, wds):
    """returns a list of all possible tag_list for a list of words"""
    if (wds == []):
        return [[]]
    else:
        tag_first = tag_word (lx, wds[0])
        tag_rest = tag_words (lx, wds[1:])
        return [[fst] + rst for fst in tag_first for rst in tag_rest]

# End of PART B.
'''lx=Lexicon()
#lx.add()
lx.add("John","P")
lx.add("Mary","P")
lx.add("like","T")
x=tag_word(lx,"John")
print(x)
'''