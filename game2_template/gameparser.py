import string

# List of "unimportant" words (feel free to add more)
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']

def filter_words(words, skip_words): #Skips all input words that are deemed unimportant 
    for skip_word in skip_words:
        for word in words:
            if word == skip_word: #If the word is in the skip_words set then it is removed from the input
                words.remove(word)
    return words

def remove_punct(text): #Removes punctuation from the users input
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char

    return no_punct

def normalise_input(user_input): #Normalises the users input 
    normalised_input = remove_punct(user_input).lower() #Removes punctuation and lowers the text
    normalised_input = normalised_input.split() #Splits the text
    normalised_input = filter_words(normalised_input, skip_words) #Removes any unimportant words 
    return normalised_input #Returns the normailsed input


