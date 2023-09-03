import nltk
from nltk.corpus import reuters

nltk.download('reuters')
nltk.download('punkt')

# 1. How many documents are there in the Reuters Corpus?
print("1. How many documents are there in the Reuters Corpus?")
print(len(reuters.fileids()))

# 2. How many words are there in the entire corpus?
print("2. How many words are there in the entire corpus?")
print(len(reuters.words()))

# 3. How many sentences are there in the entire corpus?
print("3. How many sentences are there in the entire corpus?")
print(len(reuters.sents()))

# 4. Find the text with fileID 'training/9920' in the corpus. Determine the number of words.
print("4. Find the text with fileID 'training/9920' in the corpus. Determine the number of words.")
print(len(reuters.words('training/9920')))

# 5. Determine the number of single word prepositions (e.g. 'in', 'on', 'at') in the entire corpus. 
print("5. Determine the number of single word prepositions (e.g. 'in', 'on', 'at') in the entire corpus.")

# most common prepositions in English
prepositions = ['of', 'in', 'to', 'for', 'with', 'on', 'at', 'from', 'by', 'about', 'as', 'into', 'like', 'through', 'after', 'over', 'between', 'out', 'against', 'during', 'without', 'before', 'under', 'around', 'among']
prepositions_count = 0
for word in reuters.words():
    if word in prepositions:
        prepositions_count += 1


def word_freq(word, fileId):
    count = 0
    for w in reuters.words(fileId):
        if w == word:
            count += 1
    return count


# 6. Use Regex to replace > with '' in the text with fileID 'training/9920'. Output the text after preprocessing.
print("6. Use Regex to replace > with '' in the text with fileID 'training/9920'. Output the text after preprocessing.")
text = reuters.raw('training/9920')
text = text.replace('>', '')
print(text)
