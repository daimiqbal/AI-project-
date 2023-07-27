import matplotlib
from IPython.core.interactiveshell import InteractiveShell
from jedi.api.refactoring import inline

InteractiveShell.ast_node_interactivity = "all"
from numpy import count_nonzero, diag, arange, dot
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from scipy.sparse.linalg import svds
import warnings
# Import the dataset and give the column names
columns = ['userId', 'productId', 'ratings', 'timestamp']
electronics_df = pd.read_csv('Electronics-data set.csv', names=columns)
electronics_df.head()
electronics_df.drop('timestamp', axis=1, inplace=True)
electronics_df.info()
def recommend(user_id):
    user_recommendations = popularity_recommendations

    # Add user_id column for which the recommendations are being generated
    user_recommendations['userId'] = user_id

    # Bring user_id column to the front
    cols = user_recommendations.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    user_recommendations = user_recommendations[cols]

    return user_recommendations
def recommend_items(userID, pivot_df, preds_df, num_recommendations):
    # index starts at 0
    user_idx = userID - 1
    # Get and sort the user's ratings
    sorted_user_ratings = pivot_df.iloc[user_idx].sort_values(ascending=False)
    # sorted_user_ratings
    sorted_user_predictions = preds_df.iloc[user_idx].sort_values(ascending=False)
    # sorted_user_predictions
    temp = pd.concat([sorted_user_ratings, sorted_user_predictions], axis=1)
    temp.index.name = 'Recommended Items'
    temp.columns = ['user_ratings', 'user_predictions']
    temp = temp.loc[temp.user_ratings == 0]
    temp = temp.sort_values('user_predictions', ascending=False)
    print('\nBelow are the recommended items for user(user_id = {}):\n'.format(userID))
    print(temp.head(num_recommendations))
