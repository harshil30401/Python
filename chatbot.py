import random, string, warnings, nltk

from googlesearch import search
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# from nltk.stem import WordNetLemmatizer

warnings.filterwarnings('ignore')

# from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True)

# from google.colab import drive
# drive.mount('/content/drive')

file = r'C:\Users\DELL\Desktop\ChatBot\bot.txt'

f = open(file, 'r', errors='ignore')
raw = f.read()
raw = raw.lower()

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)
lemmatizer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmatizer.lemmatize(token) for token in tokens]

remove_punc_dict = dict((ord(punc), None) for punc in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punc_dict)))

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I'm glad you're talking to me"]

def greeting(sentence):
    for word in sentence.split():
        if (word.lower() in GREETING_INPUTS):
            return random.choice(GREETING_RESPONSES)

def search_online(user_response):
    query = str(user_response)

    for j in search(query, num_results=5):
        print(j)

def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfIdVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfIdVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf == 0):
        print("Sorry, i don't understand, do you want me to do a web search?")
        web_search = input("Type Yes/No: ")
        web_search.lower()
        if (web_search == 'yes'):
            print("KITT: Here are the top 5 resuts from google: \n")
            return search_online(user_response)                       

        elif (web_search == 'no'):
            robo_response = ("KITT: Okay")
            return robo_response

        else:
            robo_response = ("KITT: Not a valid response!")
            return robo_response

    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response

def chat(user_response):
    if(user_response != 'bye'):
        if(user_response == 'thanks' or user_response == 'thank you'):
            flag = False
            print(" KITT: You're most welcome :)")
            pass
        elif (('not tell' or 'not say' or 'not send') in user_response):
            print("KITT: Okay, i won't")
            pass

        elif (('your name' or 'who are you' or 'your identity') in user_response):
            print('KITT: My name is KITT, i\'m a ChatBot')
            pass        

        else:
            if(greeting(user_response) != None):
                print("KITT: "+greeting(user_response))
            else:
                print("KITT: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
            pass
    else:
        flag = False
        print("KITT: Have a great day!")

def main():
    flag = True

    print("Hello i'm KITT, how can i help you?")

    while(flag == True):
        user_response = input("You: ")
        user_response = user_response.lower()
        if(user_response != 'bye'):
            if(user_response == 'thanks' or user_response == 'thank you'):
                flag = False
                print(" KITT: You're most welcome :)")
                pass
            elif (('not' or 'not tell' or 'not say' or 'not send') in user_response):
                print("KITT: Okay, i won't")
                pass

            elif (('your name' or 'who are you' or 'your identity') in user_response):
                print('KITT: My name is KITT, I\'m an AI powered ChatBot')
                pass

            else:
                if(greeting(user_response) != None):
                    print("KITT: "+greeting(user_response))
                else:
                    print("KITT: ",end="")
                    print(response(user_response))
                    sent_tokens.remove(user_response)
                pass
        else:
            flag = False
            print("KITT: Have a great day!")

try:
    main()
except KeyboardInterrupt:
    print("Type bye to deactivate me")
    main()
