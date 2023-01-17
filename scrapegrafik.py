import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_tokped_2.csv')
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots()
df['categoryName'].value_counts().sort_values(ascending=True).tail(10).plot(ax = ax, kind = "pie")
plt.title("Rekap Kategori Tokopedia")
plt.show() 