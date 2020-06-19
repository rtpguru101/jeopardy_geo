import pandas as pd
import glob
from os import chdir

df_geo_all = pd.DataFrame()
categories_file = 'category_search_terms.txt'
with open(categories_file, 'rt') as cf:
    categories = [line.strip() for line in cf]
categories_str = '|'.join(categories)

data_folder = 'jeopardy_clue_dataset'
chdir(data_folder)
tsv_files = glob.glob('*.tsv')

for tsv_file in tsv_files:
    print(tsv_file)
    df = pd.read_csv(tsv_file, sep='\t')
    df['category'] = df['category'].str.lower()
    df['answer'] = df['answer'].str.lower()
    df['combined'] = df['category'] + ' ' + df['answer'] + ' ' + df['question']
    df_geo = df[df['combined'].str.match(categories_str) == True]
    df_geo = df_geo.drop(['round', 'value', 'daily_double', 'comments', 'combined', 'air_date', 'notes'], axis=1)
    df_geo_all = df_geo_all.append(df_geo)

df_geo_all = df_geo_all.reset_index()
df_geo_all.to_csv('jeopardy_geo.csv')
