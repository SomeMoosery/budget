import pandas as pandas
from matplotlib.pyplot import pie, axis, show
# %matplotlib inline

df = pandas.read_csv('budget-test.csv')

sums = df.groupby(df["Type"]).sum()
sums = sums.drop(['Rent'])

sums.plot.pie(subplots=True, figsize=(10,10))
show()