"""
@author Ciara Gilsenan
@version 20/04/2021
Inferential Statistics Analysis on the data
"""
import pandas as pd
import numpy as np

# read in excel sheets with linguistic complexity scores
df1 = pd.read_excel('Political - Linguistic Complexity Measurements.xls')
df2 = pd.read_excel('Comedy_Culture - Linguistic Complexity Measurements.xls')

print("Inferential Statistics...")
print("Political Data:")
for m in df1.keys()[1:]:
    # Sample 150 entries, calculate mean and standard deviation
    sample_data = np.random.choice(a=df1[m], size=150)
    print("\nSample", m, "mean:", sample_data.mean())
    print("Sample", m, "std:", sample_data.std())

print("\nCultural Data:")
for m in df2.keys()[1:]:
    # Sample 150 entries, calculate mean and standard deviation
    sample_data = np.random.choice(a=df2[m], size=150)
    print("\nSample", m, "mean:", sample_data.mean())
    print("Sample", m, "std:", sample_data.std())



