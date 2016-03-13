# read features and train!

import pandas as pd

# import models!
from sklearn.ensemble import RandomForestRegressor, BaggingRegressor

num_train = 74067

df_all = pd.read_csv('df_all.csv')

df_train 	= df_all.iloc[:num_train]
df_test		= df_all.iloc[num_train:]
id_test		= df_test['id']

X_train = df_train	.drop(['id','product_uid','relevance'], axis=1).values
X_test 	= df_test	.drop(['id','product_uid','relevance'],	axis=1).values

y_train	= df_train['relevance'].values

# using RFR and BR to train and predict!
rf = RandomForestRegressor(n_estimators=15, max_depth=6, random_state=0)
clf = BaggingRegressor(rf, n_estimators=45, max_samples=0.1, random_state=25)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

pd.DataFrame({"id": id_test, "relevance": y_pred}).to_csv('submission.csv', index=False)

