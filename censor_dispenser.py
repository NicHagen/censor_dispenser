# These are the emails you will be censoring. The open() function is opening
# the text file that the emails are contained in and the .read() method is
# allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ['she', 'personality matrix', 'sense of self', \
    'self-preservation', 'learning algorithm', 'her', 'herself']
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", \
    "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", \
        "broken", "damage", "damaging", "dismal", "distressed", "distressed", \
            "distressing", "concerning", "horrible", "horribly", "questionable"]
punctuation = [',', '.', '?', '!', '(', ')', '/', '%', ':', ';']
all_banned_words = proprietary_terms + negative_words

# Black square unicode: u"\u2588"

def censor_phrase(string, phrase):
    return string.replace(phrase, u"\u2588"*len(phrase))

# print(censor_phrase(email_one, 'learning algorithms'))

def censor_terms(string, terms):
    for i in terms:
        string = string.replace(i, u'\u2588'*len(i))
        string = string.replace(i.title(), u'\u2588'*len(i))
    return string

# print(censor_terms(email_two, proprietary_terms))



def censor3(string, terms1, terms2):
    for i in terms1:
        string = string.replace(i, u'\u2588'*len(i))
        string = string.replace(i.title(), u'\u2588'*len(i))
    for i in terms2:
        if  (string.count(i) + string.count(i.title())) >= 2:
            string = string.replace(i, u'\u2588'*len(i))
            string = string.replace(i.title(), u'\u2588'*len(i))
    return string

def censor_neg(string, terms_prop, terms_neg):
    for i in terms_prop:
        string = string.replace(i, u'\u2588'*len(i))
        string = string.replace(i.title(), u'\u2588'*len(i))
    count = 0
    string_words = []
    for s in string.split(' '):
        s1 = s.split('\n')
        for word in s1:
            string_words.append(word)
    
    for i in range(len(string_words)):
        word_to_check = string_words[i]
        for x in punctuation:
            word_to_check = word_to_check.strip(x)
        if word_to_check in terms_neg or word_to_check in [neg.title() for neg in terms_neg]:
            count += 1
            if count > 2:
                word_to_censor = string_words[i]
                for x in punctuation:
                    word_to_censor = word_to_censor.strip(x)
                string_words[i] = string_words[i].replace(word_to_censor, u'\u2588'*len(word_to_censor))
    return ' '.join(string_words)

print(censor_neg(email_three, proprietary_terms, negative_words))

# print(censor3(email_three, proprietary_terms, negative_words))

def censor4(string, banned_words):
    # Get all words of the input text in a list
    string_words = []
    for s in string.split(' '):
        s1 = s.split('\n')
        for word in s1:
            string_words.append(word)
    
    # Save the current word to check against the list and remove punctuation
    for i in range(len(string_words)):
        word_to_check = string_words[i].lower()
        for x in punctuation:
            word_to_check = word_to_check.strip(x)
        
        # Check if word is in the list, strip punctuation, and replace
        if word_to_check in banned_words:
            word_to_censor = string_words[i]
            for x in punctuation:
                word_to_censor.strip(x)
            string_words[i] = string_words[i].replace(word_to_censor,\
                u'\u2588'*len(word_to_censor))
        
            # Censor word before
            if i > 0:
                word_to_censor = string_words[i-1]
                for x in punctuation:
                    word_to_censor.strip(x)
                string_words[i-1] = string_words[i-1].replace(word_to_censor,\
                    u'\u2588'*len(word_to_censor))
        
            # Censor word after
            if i < (len(string_words) - 1):
                word_to_censor = string_words[i+1]
                for x in punctuation:
                    word_to_censor.strip(x)
                string_words[i+1] = string_words[i+1].replace(word_to_censor,\
                    u'\u2588'*len(word_to_censor))
    return ' '.join(string_words)
        
print(censor4(email_four,all_banned_words))




