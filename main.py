user_doc = input('Paste your document here: \n')

words_used = {'test': 1}

# Create new string for each new word based on spaces

'''for character in range(len(user_doc)):
    current_word = ''
    if user_doc[character] != ' ':
        current_word = current_word + user_doc[character]
        print(current_word)
    elif user_doc[character] == ' ':
        print('this is a space')
'''
current_word = ''
for character in range(len(user_doc)):
    # FIXME: check if existing word already and add one to total for word
    
    # For new words
    if user_doc[character] != ' ':
        current_word += user_doc[character]

        # FIXME: check last word in document if it doesn't have a space
    elif (user_doc[character] == ' '): # or character == len(user_doc):
        if current_word in words_used:
            words_used[current_word] += 1
        else:
            words_used[current_word] = 1
        current_word = ''

print(words_used)

    

# FIXME: ignore punctuation . , ! ? : ; " / ( ) % - 



# FIXME: ignore common words: and or the for etc. (look up a list of these words for reference)