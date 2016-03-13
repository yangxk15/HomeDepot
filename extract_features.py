import numpy as np
import pandas as pd

from difflib import SequenceMatcher

df_train 	= pd.read_csv('train.csv')
df_all 		= pd.read_csv('pairs.csv')
df_product	= pd.read_csv('product_info.csv')

num_train = df_train.shape[0]

def str_common_word(str1, str2):
	return sum(int(str2.find(word)>=0) for word in str1.split())

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def msimilar(a, b):
    return max([similar(a, w) for w in b.split()])

def mmsimilar(a, b):
    if a and b:
        return sum([msimilar(w, b) for w in a.split()])
    return 0

df_all = pd.merge(df_all, df_product, how='left', on='product_uid')

df_all['len_of_query'] 		= df_all['search_term']		.map(lambda x:len(x.split())).astype(np.int64)
df_all['len_of_title'] 		= df_all['product_title']	.map(lambda x:len(x.split())).astype(np.int64)
df_all['len_of_description'] 	= df_all['product_description']	.map(lambda x:len(x.split())).astype(np.int64)
df_all['len_of_brand'] 		= df_all['brand']		.map(lambda x:len(x.split())).astype(np.int64)
df_all['len_of_name'] 		= df_all['name']		.map(lambda x:len(x.split())).astype(np.int64)
df_all['len_of_value'] 		= df_all['value']		.map(lambda x:len(x.split())).astype(np.int64)

df_all['product_info'] 		= 	 df_all['search_term']\
				+ "\t" + df_all['product_title']\
				+ "\t" + df_all['product_description']\
				+ "\t" + df_all['brand']\
				+ "\t" + df_all['name']\
				+ "\t" + df_all['value']

df_all['word_in_title'] 	= df_all['product_info'].map(lambda x:str_common_word(x.split('\t')[0],x.split('\t')[1]))
df_all['word_in_description'] 	= df_all['product_info'].map(lambda x:str_common_word(x.split('\t')[0],x.split('\t')[2]))
df_all['word_in_brand'] 	= df_all['product_info'].map(lambda x:str_common_word(x.split('\t')[0],x.split('\t')[3]))
df_all['word_in_name'] 		= df_all['product_info'].map(lambda x:str_common_word(x.split('\t')[0],x.split('\t')[4]))
df_all['word_in_value'] 	= df_all['product_info'].map(lambda x:str_common_word(x.split('\t')[0],x.split('\t')[5]))

df_all['similar_title'] 	= df_all['product_info'].map(lambda x:mmsimilar(x.split('\t')[0],x.split('\t')[1]))
df_all['similar_description'] 	= df_all['product_info'].map(lambda x:mmsimilar(x.split('\t')[0],x.split('\t')[2]))
df_all['similar_brand'] 	= df_all['product_info'].map(lambda x:mmsimilar(x.split('\t')[0],x.split('\t')[3]))
df_all['similar_name'] 		= df_all['product_info'].map(lambda x:mmsimilar(x.split('\t')[0],x.split('\t')[4]))
df_all['similar_value'] 	= df_all['product_info'].map(lambda x:mmsimilar(x.split('\t')[0],x.split('\t')[5]))

df_all = df_all.drop(['search_term','product_title','product_description','product_info','brand','name','value'],axis=1)

df_all.to_csv('df_all.csv',index=False);

