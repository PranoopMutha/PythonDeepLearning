from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import pandas as pd

from sklearn.model_selection import KFold, cross_val_score, RepeatedKFold

#creating a data frame containing our data, each column can be accessed by df['column name']
df = pd.read_csv('C:\\Users\\MuthaNagaVenkataSaty\\Desktop\\Python DL\\Python Lesson 4\\Python_Lesson6\\iris.csv')

# df.loc[df.Species == 'Iris-setosa', 'class'] = 1
# df.loc[df.Species == 'Iris-versicolor', 'class'] = 2
# df.loc[df.Species == 'Iris-virginica', 'class'] = 3

# train data
X = df.as_matrix(
    columns=['sepal length','sepal width','petal length','petal width'])

y = df['Species'].values

kf = RepeatedKFold(n_splits=5, n_repeats=10, random_state=None)
scores = []
for train_index, test_index in kf.split(X):
      #print("Train:", train_index, "Validation:",test_index)
      X_train, X_test = X[train_index], X[test_index]
      y_train, y_test = y[train_index], y[test_index]
      gnb = GaussianNB()
      gnb.fit(X_train, y_train)
      train_predicted_values = gnb.predict(X_test)
      scores.append(metrics.accuracy_score(y_test, train_predicted_values) * 100)

print(pd.np.mean(scores))







