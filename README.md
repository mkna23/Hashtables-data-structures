# Project: Hashtables-data-structures for calculating frequency of pair of anagrams in raw text

## Overview: In this project, I was given a raw text file to find the pairs of anagrams an then to calculate the frequency of ech pair in text.

## Steps used for completion of this project

1. Read the text file and then this text preprocessed it by a preprocess function

2. In preprocess function, it takes the text and first of all remove all pnctuations and
tokenized the text and created a list of tokenized words, from this list i just kept the words
that have no numeric values and are not stopwords

3. Using list of words a list of unique words is created because further while finding
anagrams this list of unique words  help in not giving repition of words in pairs of anagrams.

4. Hashing function takes the word as input and creates  indexe for word,
here prime numbers were assigned to different alphabets using a dic and 
then multiplication of prime numbers associated the alphabets in word is the index of the word
this creates collisions for anagrams, bcz anagrams have same alphabets in their string.

5. Hashing return the list of indexes of words by using hashing function previously described
list was used over here as ouput because they are ordered, so the word in words list is at same position 
as index of word in index list

6. Using for loop, a dic is being created named anagrams whose key is index and value is list of anagrams.
as angrams have same indexes

7. Next part was to calculate freq for  anagrams list in anarams dic
using for loop over values of anagrams dictionary, and  nested for loop over list of anagrams
the freq of word is calculated by built in count function.

8. The  tuple of list of angrams and their frequency is appended to the anagramfrq list

9. In search function i calculated the index of word and through its index i got the 
list of anagrams and then from list of anagrams i found the frequency.
