import nltk # Import NLTK package for natural language processing
from nltk.corpus import stopwords # Import stopwords module, which manages words that carry little semantic meaning 
from nltk.tokenize import word_tokenize, sent_tokenize # Import word and sentence tokenizing libraries

text = """""" # Placeholder for the input text

# Create a set of Croatian stopwords
stopwords = set([
    'a', 'ako', 'ali', 'bih', 'bi', 'bismo', 'biste', 'bio', 'bila', 
    'bile', 'bili', 'bilo', 'ću', 'ćeš', 'će', 'ćemo', 'ćete', 
    'da', 'i', 'ili', 'iako', 'jer', 'ni', 'niti', 'pa', 'te'
]) 
words = word_tokenize(text) # Tokenize the input text into words

freqTable = dict() # Initialize an empty dictionary to store word frequencies 
for word in words: # Iterate over each word in the tokenized words
    word = word.lower() # Convert word to lowercase
    if word in stopwords: 
        continue # If the word is a stopword, skip it
    if word in freqTable: 
        freqTable[word] += 1 # If the word is already in the frequency table, increment its count by 1
    else:
        freqTable[word] = 1 # Otherwise, add the word to the frequency table with a count of 1

sentences = sent_tokenize(text) # Tokenize the input text into sentences
sentenceValue = dict() # Initialize an empty dictionary to store sentence scores

for sentence in sentences: # Iterate over each sentence
    for word, freq in freqTable.items(): # Iterate over each word and its frequency in the frequency table
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq # If the sentence is already in the sentenceValue dictionary, increment the sentence's score by the word frequency
            else:
                sentenceValue[sentence] = freq # Otherwise, add the sentence to the dictionary with the word's frequency

sumValues = 0 
for sentence in sentenceValue: # Iterate over each sentence in the sentenceValue dictionary
    sumValues += sentenceValue[sentence] # Add the sentence's score to sumValues

average = int(sumValues / len(sentenceValue)) # Calculate the average sentence score

summary = '' # Initialize an empty string for the summary
for sentence in sentences: # Iterate over each sentence
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 
        summary += " " + sentence # If the sentence's score is above a threshold, add the sentence to the summary
print(summary) # Print the summary



