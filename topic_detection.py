# One Corpus per podcast, 8 - 10 episodes per corpus
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
import gensim
import string
from gensim import corpora
from gensim.corpora.dictionary import Dictionary
from text import text1, docs
#nltk.download('stopwords') 

# Preprocessing
tokens = word_tokenize(text1)
lowercase_tokens = [t.lower() for t in tokens]
#print(lowercase_tokens)

bagofwords_1 = Counter(lowercase_tokens)
#print(bagofwords_1.most_common(10))

alphabets = [t for t in lowercase_tokens if t.isalpha()]

words = stopwords.words("english")
stopwords_removed = [t for t in alphabets if t not in words]

# LDA 
stopwords = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(document):
    stopwordremoval = " ".join([i for i in document.lower().split() if i not in stopwords])
    punctuationremoval = ''.join(ch for ch in stopwordremoval if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punctuationremoval.split())
    return normalized

for_model = clean(text1).split()

final_doc = [clean(document).split() for document in docs]

print("\n")
print(final_doc)

dictionary = corpora.Dictionary(final_doc)

DT_matrix = [dictionary.doc2bow(doc) for doc in final_doc]

Lda_object = gensim.models.ldamodel.LdaModel

lda_model_1 = Lda_object(DT_matrix, num_topics=5, id2word = dictionary)


print("\nLDA Model Topics")
for idx, topic in lda_model_1.print_topics(-1):
    print("Topic: {} \nWords: {}".format(idx, topic ))
    print("\n")