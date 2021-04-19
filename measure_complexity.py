"""
@authors Ciara Gilsenan
@version 17/04/2021
Text Treatment for Data
"""
import os
from lexicalrichness import LexicalRichness
import textstat
import pandas as pd
import numpy as np
from nltk import RegexpTokenizer
from gensim.parsing.preprocessing import remove_stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

tokenizer = RegexpTokenizer(r"\w+")

for file in sorted(os.listdir('./Data')):
    file_name_csv = './' + file[:-4] + '.csv'
    file_name_xl = './' + file[:-4] + '.xlsx'
    print('working on:', file)

    #Read in CSV
    df = pd.read_csv('./Data/' + file, header=0)
    text_data = np.array(df.iloc[:, 3])
    pod_id = np.array(df.iloc[:, 0])
    speaker_id = np.array(df.iloc[:, 2])

    # measure complexity & record results in csv file
    instance_ids = []
    ttr = []
    mtld = []
    number_of_words = []
    readability = []
    unique_words = []
    avg_sentence_length = []
    avg_word_length = []
    for i, instance in enumerate(text_data):
        lex_with_stopwords = LexicalRichness(instance)
        number_of_words.append(lex_with_stopwords.words)
        
        # mean sentence length
        mean_sentence_len = int(lex_with_stopwords.words / textstat.sentence_count(instance))
        avg_sentence_length.append(mean_sentence_len)
        
        # mean word length
        num_chars = sum([len(w) for w in tokenizer.tokenize(instance)])
        mean_word_len = round(num_chars / lex_with_stopwords.words, 1)
        avg_word_length.append(mean_word_len)

        readability.append(textstat.flesch_reading_ease(instance))
        
        # remove stopwords & lemmatize
        lemmatizer = WordNetLemmatizer()
        instance_no_stopwords = remove_stopwords(instance)
        new_instance = ' '.join([lemmatizer.lemmatize(w) for w in word_tokenize(instance_no_stopwords)])
        
        lex = LexicalRichness(new_instance)
        ttr.append(lex.ttr)
        mtld.append(lex.mtld(threshold=0.72))
        inst_id = str(pod_id[i]) + '_' + str(speaker_id[i])
        instance_ids.append(inst_id)
        unique_words.append(lex.terms)


    measurements = {
        'instance' : instance_ids,
        'mtld' : mtld,
        'ttr' : ttr,
        'readability' : readability,
        'unique_words' : unique_words,
        'avg sentence len' : avg_sentence_length,
        'avg word len' : avg_word_length
    }

    new_df = pd.DataFrame(measurements, columns=['instance', 'mtld', 'ttr', 'readability', 'unique_words', 
        'avg sentence len', 'avg word len'])
    new_df.to_excel(file_name_xl, index=False, sheet_name='Politics')
    new_df.to_csv(file_name_csv, index=False)
