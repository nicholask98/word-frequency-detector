words_used = {}

punctuation = ('.', ',', '!', '?', ';', ':', '[', ']', '{', '}', '(', ')', '"')
common_words = ('THE', 'A', 'AN', 'AND', 'BE', 'TO', 'HAVE', 'DO', "DON'T", 'SAY', 
'OR', 'BUT', 'OF', 'FOR', 'IN', 'WITH', 'ON', 'FROM', 'AT', 'BY', 'IT', 'IS', 'IF', 
'I', 'YOU', 'HE', 'SHE', 'THEY', 'WE', 'HIS', 'HERS', 'THAT', 'THIS', 'NOT', 'TO')


def add_word(word):
    if word in words_used: # For existing words
        words_used[word] += 1
    else: # For new words
        words_used[word] = 1

user_doc = input('Paste your document here: \n')
current_word = ''
for character in range(len(user_doc)): # Create new string for each new word based on spaces
     
    if user_doc[character] in punctuation: # checks for punctuation and ignores it
        continue

    if user_doc[character] != ' ': # Compiles all characters before the next space into one string: current_word
        current_word += user_doc[character]
        continue

    current_word = current_word.upper()
    
    if (user_doc[character] == ' '):
        if current_word in common_words: # Skips common words
            current_word = ''
            continue
        else:
            add_word(current_word)
            current_word = ''

add_word(current_word.upper()) # Last word

print(words_used)

#FIXME: If an enter/return is used in the document pasted, the program currently
# treats it as the user pressing enter. Therefore everything after the first return
# in the document is not counted. ****

# ****  
# upon some further research, it seems that I need to read in a user document from a
# file, and not from the terminal. The return key is reserved for finalizing the user
# input, and cannot be used in any other way. 



# FIXME: Print a specific number of the top most used words 10, 20 etc.



# FIXME: Let the user input how many of the top words they want to see


# FIXME: Look into split() function for strings. May be able to replace your
# work involving detecting spaces in the user input.

# --- My current understanding is that it removes specified sequences of 
# characters from a string, and puts each resulting section into a list with
# its own index.