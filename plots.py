# %% Import libraries and files
import pandas as pd 
import seaborn as sns
from pandas import DataFrame

df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")
sns.set_theme(style="white")
# %% 
print(df.describe())

# %% Histogramas
df['hour'].hist(bins=23)
df[['discount%']].hist()
df[['weekday']].hist(bins=7)
df[['total_items']].hist()
# %% Heatmap
new = df.filter(['weekday','hour'], axis=1)
new2 = new.groupby(['weekday','hour']).size().reset_index(name="count")
heatmap_data = pd.pivot_table(new2, values='count', index=['weekday'], columns='hour')
sns.heatmap(heatmap_data)

# %% Diagrama de caja de bigotes
df[['hour']].plot.box()
df[['discount%']].plot.box()
df[['weekday']].plot.box()
df[['total_items']].plot.box()

# %%
new = df.filter(['order'], axis=1)
new2 = new.groupby(['order']).size().reset_index(name="count")
df.plot.scatter(x='count', y=['order'])
# %%
df.plot.scatter(x="")