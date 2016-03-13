# search_term-product pair preprocessing

import stemmer

df_train 	= pd.read_csv('train.csv')
df_test		= pd.read_csv('test.csv')

df_pair = pd.concat((df_train, df_test), axis=0, ignore_index=True)

df_pair['search_term']		= df_pair['search_term']	.map(lambda x:stemmer.str_stemmer(x))
df_pair['product_title']	= df_pair['product_title']	.map(lambda x:stemmer.str_stemmer(x))

df_pair.to_csv('pairs.csv', index=False, encoding='utf-8')
