"""
print("\nTrying Stanford & Stanza...")
import stanza
sample = text_data[0]
stanza.download('en')
nlp = stanza.Pipeline('en')
doc = nlp(sample)
#print(doc.sentences[0].dependencies)

import stanfordnlp
stanfordnlp.download('en')
nlp = stanfordnlp.Pipeline()
doc2 = text_data[0]
print(doc.sentences[0].print_dependencies())
"""