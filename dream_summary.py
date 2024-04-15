# Hashable object that is great for keeping track of the frequency of different items in a collection.
from collections import Counter # keep track of sentence scoring
import re # regular expressions module
import requests # used to download files and webpages
import bs4 # used to parse HTML
import nltk
from nltk.corpus import stopwords

# Project performs the following steps:
# 1. Opens a web page containing the "I Have a Dream" speech
# 2. Loads the text as a string
# 3. Tokenizes the text into words and sentences
# 4. Removes stop words with no contextual content
# 5. Counts the remaining words
# 6. Uses the counts to rank the sentences
# 7. Displays the highest-ranking sentences

# Notes: 
# Elements are stored as dictionary keys, and their counts are stored as dictionary values.

def main():
    # url to webscrape and extract html from
    url = 'http://www.analytictech.com/mb021/mlk.htm'
    page = requests.get(url) # storing extracted html
    page.raise_for_status() # Returns an HTTPError (response) object if an error has occured during the process
    soup = bs4.BeautifulSoup(page.text, 'html.parser') # Parse html using html.parser
    p_elems = [element.text for element in soup.find_all('p')] # Store all p elements text in an array
    speech = ''.join(p_elems) # Combine elements into text

    # Prep speech to fix typos, remove punctuation, special characters, and spaces:
    # eliminate extra white spaces, replace all non-alphabtic characters with a space
    # eliminate white spaces again because of replacement of non-alphabtic characters
    speech = speech.replace(')mowing', 'knowing') # Replace typo mowing with knowing
    speech = re.sub('\s+', ' ', speech) # replace one or more whitespace characters matched by the pattern should be replaced with a single space
    speech_edit = re_sub('[^a-zA-Z]', ' ', speech) # replace all non-alphabetic characters with a space
    speech_edit = re.sub('\s+',' ', speech_edit) # replace sequence of whitespace characters with a single whitespace character

    # User enters whole numbers for max-words and number-of-sentences
    #  and validate that user has entered in only numbers
    while True:
        max_words = input("Enter max words per sentence for summary: ")
        num_sents = input("Enter number of sentences for summary: ")
        if max_words.isdigit() and num_sets.isdigit():
            break
        else:
            print("\nInput must be in whole numbers.\n")
    
    speech_edit_no_stop = remove_stop_words(speach_edit)
    word_freq = get_word_freq(speech_edit_no_stop)
    sent_scores = score_sentences(speech, word_freq, max_words)

    counts = Counter(sent_scores)
    summary = counts.most_common(int(num_sents))
    print("\nSUMMARY:")
    for i in summary:
        print(i[0])

# functions to be defined:

main()