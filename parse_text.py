import numpy as np
import pandas as pd
import textstat
import os
import stanza
from stanza.server import CoreNLPClient
#stanza.install_corenlp()
#stanza.download('en')

def count_clauses(text):
    annotators="tokenize,ssplit,pos,lemma,parse"
    pattern = 'S'
    matches = client.tregex(text, pattern, annotators=annotators)
    return sum([len(sentence.keys()) for sentence in matches['sentences']])

with CoreNLPClient(timeout=30000, memory='16G') as client:
    for file in sorted(os.listdir('./Data')):
        file_name_xl = './' + file[:-4] + ' - Clause Analysis.xls'
        print('working on:', file)

        #Read in CSV
        df = pd.read_csv('./Data/' + file, header=0)
        text_data = np.array(df.iloc[:, 3])
        pod_id = np.array(df.iloc[:, 0])
        speaker_id = np.array(df.iloc[:, 2])
        sentence_complexity = []
        counted_clauses = []
        instance_ids = []
        for i, instance in enumerate(text_data):
            no_clauses = count_clauses(instance)
            counted_clauses.append(no_clauses)
            sentence_complexity.append(no_clauses/textstat.sentence_count(instance))

            inst_id = str(pod_id[i]) + '_' + str(speaker_id[i])
            instance_ids.append(inst_id)

        clause_analysis = {
            'instance' : instance_ids,
            'number of clauses' : counted_clauses,
            'sentence complexity' : sentence_complexity
        }

        new_df = pd.DataFrame(clause_analysis, columns=['instance', 'number of clauses', 'sentence complexity'])
        new_df.to_excel(file_name_xl, index=False, sheet_name='Clause')
