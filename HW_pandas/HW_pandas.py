import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler

url = "https://raw.githubusercontent.com/Serfentum/bf_course/master/14.pandas/train.csv"
train_df = pd.read_csv(url)

cols = ['pos', 'A', 'C', 'T', 'G']
nucleotides = train_df[cols].groupby('pos').sum()
nucleotides.plot.bar(stacked=True, xlabel='pos', ylabel='number of reads', rot=50, figsize=(40, 10),
                     fontsize=30)

cols = ['pos', 'reads_all', 'mismatches', 'deletions', 'insertions']
train_part = train_df.query('matches > matches.mean()')[cols]
train_part.to_csv('Data/train_part.csv')

wine_set = pd.read_csv('Data/WineQT.csv')
wine_set.head()
wine_set.info()
wine_set.shape
wine_set.size
wine_set.iloc[:, 1:].describe()
wine_set.isnull().sum()
wine_set.duplicated()
wine_set = wine_set.set_index('Id')
scaler = StandardScaler()
scaler.fit(wine_set)
wine_set = pd.DataFrame(scaler.transform(wine_set))
wine_set.hist(figsize(40, 50))
sns.pairplot(wine_set.iloc[:, 1:], kind='kde')


def read_gff(file, columns_names=['chromosome', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase',
                                  'attributes']):
    return pd.read_table(file, sep='\t', names=columns_names, comment='#')


rrna_ano = read_gff('Data/rrna_annotation.gff')


def read_bed6(file, columns_names=['chromosome', 'start', 'end', 'name', 'score', 'strand']):
    return pd.read_table(file, sep='\t', names=columns_names, comment='#')


alignment = read_bed6('Data/alignment.bed')


rrna_ano.attributes = rrna_ano.attributes.str.extract(r'([1-6]{1,2}S)')
rrna_ano_RNA_type = rrna_ano.groupby(['chromosome']).agg({'attributes': 'value_counts'})
rrna_ano_RNA_type.unstack().plot(kind='bar', figsize=(30,10))
rrna_ano_RNA_type.unstack().plot(kind='bar', figsize=(30,10), stacked=True)


def intersect_full(gff_file, alingment):
    intersect = gff_file.merge(alingment, how='outer', on='chromosome')
    full_intersect = intersect[(intersect.start_x >= intersect.start_y+1) & (intersect.end_y+1 >= intersect.end_x)]
    return intersect, full_intersect

intersect_rrna, full_intersect_rrna = intersect_full(rrna_ano,alignment)
