import nltk.sentiment.vader as senti
import pandas as pd
import emoji
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk
import sklearn
from nltk.tokenize import word_tokenize

raw_train = pd.read_csv('training.1600000.processed.noemoticon.csv', header=None,
                        names=['Score', 'A', 'B', 'C', 'D', 'Tweet'])

raw_train.drop(['A', 'B', 'C', 'D'], axis=1)

#analyzer = senti.SentimentIntensityAnalyzer()
raw_train = pd.Series(raw_train['Tweet'], dtype='str')

score_train = []

train = raw_train[:80000]
test = raw_train[80000:100000]

#for i in range(80000):
    #score_train.append(analyzer.polarity_scores(train[i])['compound'])
#score_train = score_train.round(2)
#pd.Series(score_train)
# train = {'Tweets' : train,'Score' : score_train }
# train = pd.DataFrame(train)

score_test = []

#for i in range(80000, 100000):
    #score_test.append(analyzer.polarity_scores(test[i])['compound'])

#pd.Series(score_test)
# test = {'Tweets' : test,'Score' : score_test }
# test = pd.DataFrame(test)


#raw_train = raw_train.str.replace('http\S+|www.\S+', '', case=False)
#raw_train = raw_train.str.replace('@\S+', '', case=False)
#raw_train = raw_train.str.replace("’|'\S+", '', case=False)
#raw_train = raw_train.str.replace("\\n", '', case=False)
#for i in range(1600000):
    #raw_train[i] = emoji.demojize(raw_train[i])

#raw_train = raw_train.str.replace("_", ' ', case=False)

my_stopwords = list(stopwords.words('english'))
ps = PorterStemmer()
temp_list = []
temp_temp_list = []
for i in range(1600000):

    for word in TreebankWordTokenizer().tokenize(raw_train[i]) :

        if word not in my_stopwords:
            temp_list.append(ps.stem(word))


    temp_temp_list.append(TreebankWordDetokenizer().detokenize(temp_list))
    temp_list = []


print(temp_temp_list)