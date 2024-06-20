import pandas as pd

df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSkccFemKSPiThT66-1OFFpuYC7xjfmluk4jKHM3axi2B4fzN2k0PG-DsPx0zrri6jCexpcxBZG4lv0/pub?gid=729112787&single=true&output=csv',  sep=',')
all_brand = df['Brand'].unique()


