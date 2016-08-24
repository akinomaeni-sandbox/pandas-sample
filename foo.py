import numpy as np
import pandas as pd

df = pd.read_csv("foo.csv")
print df

df2 = pd.read_csv("foo.csv", index_col=0)
print df2

print df2.ix['tom']
print df2['age']
print df2['age'].values
print df2['age']['tom']
