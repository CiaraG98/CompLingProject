import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_excel('Political - Measurements.xls')
df2 = pd.read_excel('Comedy_Culture - Measurements.xls')

#sample_politicsl = np.random.choice(a=df1['mltd'], size=100)
#print("Sample Mean:", sample_politicsl.mean())
print("Inferential Statistics...")
print("Political Data:")
for m in df1.keys()[1:]:
    sample_data = np.random.choice(a=df1[m], size=100)
    print("\nSample", m, "mean:", sample_data.mean())
    print("Sample", m, "std:", sample_data.std())
    print("Sample", m, "variance:", sample_data.var())

print("\nCultural Data:")
for m in df2.keys()[1:]:
    sample_data = np.random.choice(a=df2[m], size=100)
    print("\nSample", m, "mean:", sample_data.mean())
    print("Sample", m, "std:", sample_data.std())
    print("Sample", m, "variance:", sample_data.var())