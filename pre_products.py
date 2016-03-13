# product infomation preprocessing

import stemmer

df_product 	= pd.read_csv('product_descriptions.csv')
df_attr 	= pd.read_csv('df_attr.csv')
df_attr_count 	= pd.read_csv('attributes_count.csv')
df_brand 	= pd.read_csv('brand.csv')

df_product = pd.merge(df_product, df_attr,		how='left', on='product_uid')
df_product = pd.merge(df_product, df_attr_count, 	how='left', on='product_uid')
df_product = pd.merge(df_product, df_brand, 		how='left', on='product_uid')

df_product['product_description'] 	= df_product['product_description']	.map(lambda x:stemmer.str_stemmer(unicode(x, errors='ignore')) if not pd.isnull(x) else "null")
df_product['name'] 			= df_product['name']			.map(lambda x:stemmer.str_stemmer(unicode(x, errors='ignore')) if not pd.isnull(x) else "null")
df_product['value'] 			= df_product['value']			.map(lambda x:stemmer.str_stemmer(unicode(x, errors='ignore')) if not pd.isnull(x) else "null")
df_product['brand'] 			= df_product['brand']			.map(lambda x:stemmer.str_stemmer(unicode(x, errors='ignore')) if not pd.isnull(x) else "null")

df_product.to_csv('product_info.csv', index=False, encoding='utf-8')
