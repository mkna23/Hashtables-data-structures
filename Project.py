#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

docstring

1. Read the text file and then this text preprocessed it by a preprocess function

2.in preprocess function, it takes the text and first of all remove all pnctuations and
tokenized the text and created a list of tokenized words, from this list i just kept the words
that have no numeric values and are not stopwords

3.using list of words a list of unique words is created because further while finding
anagrams this list of unique words  help in not giving repition of words in pairs of anagrams.

4. hashing function takes the word as input and creates  indexe for word,
here prime numbers were assigned to different alphabets using a dic and 
then multiplication of prime numbers associated the alphabets in word is the index of the word
this creates collisions for anagrams, bcz anagrams have same alphabets in their string.

5.hashing return the list of indexes of words by using hashing function previously described
list was used over here as ouput because they are ordered, so the word in words list is at same position 
as index of word in index list

6.using for loop, a dic is being created named anagrams whose key is index and value is list of anagrams.
as angrams have same indexes

7.Next part was to calculate freq for  anagrams list in anarams dic
using for loop over values of anagrams dictionary, and  nested for loop over list of anagrams
the freq of word is calculated by built in count function.

the  tuple of list of angrams and their frequency is appended to the anagramfrq list

in search function i calculated the index of word and through its index i got the 
list of anagrams and then from list of anagrams i found the frequency.
"""

import pandas as pd
from functools import reduce

def preprocess(text):
    Text=[]
    newtext = " "
    #remove puntuations by importing punctuations list from string lib
    #after removing punc add the words to newtText string
    tokenize_Text =[]
    from nltk.tokenize import word_tokenize
    import string
    for word in text:
        if word not in string.punctuation:
           newtext = newtext + word
    #creating a list of tokenized text (tokenize_Text)
    tokenize_Text = word_tokenize(newtext)
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    for word in tokenize_Text:
        if word.isalpha() is True and word not in stop_words:
            Text.append(word)
    return Text#returning list of clean text words




def Hashingfunction(word):
    """
    this hashing function takes word as inpt and calculte index for that word
    using multiplication of prime numbers."""
    
    a = 'abcdefghijklmnopqrstuvwxyz'
    p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
     71, 73, 79, 83, 89, 97, 101]
    d = dict(zip(a, p))
    return reduce((lambda i,j: i*j), [d[ch] for ch in word])



def Hashing(words,hash1):
    #this function returns the list of index keys for the list of words passed
    return list(map(lambda word : hash1(word), words))

def search(word, anagrams, anagramfreq):
    """ this function takes input as search word, anagrams dic have words with anagrams and without anagrams along with their
    indexes.
    the list anagramfreq which has tuples whose 1st value is list of anagrams and 2nd value is their frequency"""
    index = Hashingfunction(word)
    if index in anagrams.keys():
        print('word:' , word)
        print('anagrams of word in text:',anagrams[index])
        s = 1
    else:
        print('word or its anagram not in text')
    
    if s==1:
        for i in anagramfreq:
            if anagrams[index] == i[0]:
               print('frequency:',i[1])
        
               
        
                    
    

def main():
    
    text = open("jane_eyre.txt",'r')
    text = " ".join(map(str,text))
    word_list =[]
    words = preprocess(text.lower())

    #list of unique words
    for i in words:
        if i not in word_list:
            word_list.append(i)
            
     # finding   anagrams
    anagrams = {}
    index=[]
    index = Hashing(word_list,Hashingfunction)
    for i in range(len(index)):
        if index[i] not in anagrams:
           anagrams[index[i]] = [word_list[i]]
        else:
            anagrams[index[i]].append(word_list[i])


    #calculating frequency of  anagrams
    anagramfrq=[]
    for i in anagrams.values():
           sum1 = 0
           for j in i:
               sum1+= words.count(j)
           anagramfrq.append((i,sum1))
           
    #finding pairs of anagrams       
    ana =[]      
    for i in anagramfrq:
        if len(i[0])>1:
           ana.append(i) 
 
    #i prefer dataframe because it is easy to go through them.
    df = pd.DataFrame(data = ana , columns = ['Anagrams','Frequency'])
    print(df)
    #print('------Anagrams-------Frequency-----')
    #this is another way of printing anagrams
    """for i in anagramfrq:
        print(i[0],''**9,i[1])"""
   
    searchstring= str(input('input the word to search :'))
    search(searchstring, anagrams, anagramfrq)
      

main()
         
                   
                    