user_doc = input('Paste your document here: \n')

words_used = {}

# Create new string for each new word based on spaces

current_word = ''
for character in range(len(user_doc)):
    # Compiles all characters before the next space into one string: current_word
    if user_doc[character] != ' ':
        current_word += user_doc[character]

        # FIXME: check last word in document if it doesn't have a space
    elif (user_doc[character] == ' '):

# ----------------------------
# (1)Make this if/else a function
        if current_word in words_used:
            words_used[current_word] += 1
        else: # For new words
            words_used[current_word] = 1
        current_word = ''
# ----------------------------
# ----------------------------
# (1)Make this if/else a function
if current_word in words_used:
    words_used[current_word] += 1
else: # For new words
    words_used[current_word] = 1
    current_word = ''
# ----------------------------

print(words_used)

    

# FIXME: ignore punctuation . , ! ? : ; " / ( ) % - 



# FIXME: ignore common words: and or the for etc. (look up a list of these words for reference)